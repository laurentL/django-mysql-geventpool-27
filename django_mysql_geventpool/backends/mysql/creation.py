from django.db.backends.mysql.creation import DatabaseCreation as OriginalDatabaseCreation


class DatabaseCreation(OriginalDatabaseCreation):
    def _create_test_db(self, verbosity, autoclobber, keepdb=False):
        self.connection.closeall()
        return super(DatabaseCreation, self)._create_test_db(verbosity, autoclobber, keepdb)

    def _destroy_test_db(self, test_database_name, verbosity):
        self.connection.closeall()
        return super(DatabaseCreation, self)._destroy_test_db(test_database_name, verbosity)
