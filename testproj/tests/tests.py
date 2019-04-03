from django.test import TestCase
import gevent
import gevent.monkey
from django_mysql_geventpool.utils import close_connection
from django.db import connections, transaction

from .models import TestModel

gevent.monkey.patch_all()


@close_connection
def multiple_connections(count, pk):
    for x in range(0, 20):
        assert TestModel.objects.count() == 1


@close_connection
def select_for_update_error(pk):
    try:
        with transaction.atomic():
            obj = TestModel.objects.select_for_update().get(pk=pk)
            gevent.sleep(0.01)
            obj.data = 'a'
            obj.save()
            raise Exception
    except Exception:
        pass


@close_connection
def create_obj(obj):
    setattr(obj, "obj", TestModel.objects.create(data="aaaaa"))


class ModelTest(TestCase):
    def setUp(self):
        gevent.spawn(create_obj, self).join()

    def test_model_save(self):
        obj2 = TestModel.objects.get(pk=self.obj.pk)
        self.assertEqual(self.obj.data, obj2.data)

    def test_connections(self):
        greenlets = []
        for x in range(0, 50):
            greenlets.append(gevent.spawn(multiple_connections, x, self.obj.pk))
        gevent.joinall(greenlets)
        self.assertEqual(connections['default'].pool.maxsize, 20)

    def test_select_for_update(self):
        greenlets = []
        for x in range(0, 100):
            greenlets.append(gevent.spawn(select_for_update_error, self.obj.pk))
        gevent.joinall(greenlets)
        obj2 = TestModel.objects.get(pk=self.obj.pk)
        self.assertEqual(obj2.data, "aaaaa")
