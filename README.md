# ETL pipeline 

A simple ETL (Extract,Transform,Load) pipeline package for CSV, API, and Database operations.

- db_connection.py - Creates the engine to your database

- extractor.py - Uses the engine to extract data into a DataFrame

- transformer.py - Cleans and prepares the DataFrame

- loader.py - Saves the cleaned DataFrame to CSV or JSON