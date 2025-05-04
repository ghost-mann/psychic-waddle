from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class DatabaseConnection:
    def __init__(self, env_var_name="DB_CONNECTION"):
        self.connection_string = os.getenv(env_var_name)
        if not self.connection_string:
            raise ValueError(f"{env_var_name} environment variable is not set")
        self.engine = None

    def connect(self):
        if not self.engine:
            self.engine = create_engine(self.connection_string)
        return self.engine