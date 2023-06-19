import mysql.connector as mc


class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class DBConnection(object):

    def __init__(self):
        try:
            self.db = mc.connect(
                host="localhost",
                username="root",
                password="1234321",
                database="bradam"
            )
        except mc.Error:
            print("DB connection failed")

    def __str__(self):
        return self.db
