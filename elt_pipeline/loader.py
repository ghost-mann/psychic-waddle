import pandas as pd

class Loader:
    @staticmethod
    def to_csv(df: pd.DataFrame, path):
        df.to_csv(path, index=False)

    @staticmethod
    def to_json(df: pd.DataFrame, path):
        df.to_json(path, orient='records')