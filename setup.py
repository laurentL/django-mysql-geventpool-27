from setuptools import setup, find_packages

setup(
    name='django-db-geventpool',
    version='0.01',
    install_requires=['django>=2.1', 'greenlet', 'gevent'],
    description='Add a MySQL connection pool for django using gevent',
    long_description=open("README.md").read(),
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    lassifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    author='aihara',
    author_email='aihara@argmax.jp'
)