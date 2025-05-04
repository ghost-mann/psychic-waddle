import pandas as pd
import requests
from sqlalchemy import create_engine

class Extractor:
    # from csv
    @staticmethod
    def from_csv(file_path):
        return pd.read_csv(file_path)
    # from api
    @staticmethod
    def from_api(url):
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.json_normalize(data)
    # from db
    @staticmethod
    def from_db(connection_string,query):
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
            return df