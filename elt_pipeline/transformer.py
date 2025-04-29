import pandas as pd

class Transformer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def drop_null(self):
        self.df = self.df.dropna()

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()

    # missing values method

    def get_data(self):
        return self.df

