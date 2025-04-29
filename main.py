from elt_pipeline.extractor import Extractor
from elt_pipeline.db_connection import DatabaseConnection
from elt_pipeline.loader import Loader
from elt_pipeline.transformer import Transformer

def main():
    db_conn = DatabaseConnection('sqlite:///main.db')
    engine = db_conn.connect()

    # extract data
    query = 'SELECT * FROM songs'
    df = Extractor.from_db('sqlite:///main.db', query)

    # transform data
    transformer = Transformer(df)
    transformer.drop_null()
    transformer.drop_duplicates()
    cleaned_df = transformer.get_data()

    # load data
    Loader.to_csv(cleaned_df, 'cleaned_df.csv')
    Loader.to_json(cleaned_df, 'cleaned_df.json')

    print("pipeline completed")

if __name__ == "__main__":
    main()