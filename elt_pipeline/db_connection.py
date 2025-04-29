from sqlalchemy import create_engine

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = None

    def connect(self):
        if not self.engine:
            self.engine = create_engine(self.connection_string)
        return self.engine