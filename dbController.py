

class ObjectController:
    def __init__(self, db_type, name, password):
        self.db_type = db_type
        self.name = name
        self.password = password

    def add_object(self):
        print(self.db_type)
        print(self.name)
