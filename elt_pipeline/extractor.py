import pandas as pd
import requests

class Extractor:
    @staticmethod
    def to_csv(file_path):
        return pd.read_csv(file_path)

    @staticmethod
    def from_api(url):
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.json_normalize(data)
