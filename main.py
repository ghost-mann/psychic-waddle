from elt_pipeline.extractor import Extractor
from elt_pipeline.db_connection import DatabaseConnection
from elt_pipeline.loader import Loader
from elt_pipeline.transformer import Transformer

def main():

    # extract data
    df = Extractor.from_csv('spotify.csv')

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