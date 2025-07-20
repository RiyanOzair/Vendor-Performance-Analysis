import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Ensure log directory exists
os.makedirs('Logs', exist_ok=True)

logging.basicConfig(
    filename='Logs/ingestion1_db.log',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

engine = create_engine('sqlite:///inventory1.db')

def ingest_db(df, table_name, engine):
    """Ingests DataFrame into SQLite DB"""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    """Loads CSVs from directory and ingests them into the DB"""
    start = time.time()
    for file in os.listdir('Vendor Dataset'):
        if file.endswith('.csv'):
            try:
                file_path = os.path.join('Vendor Dataset', file)
                df = pd.read_csv(file_path)
                table_name = os.path.splitext(file)[0]
                logging.info(f'Ingesting {file} into the DB...')
                ingest_db(df, table_name, engine)
            except Exception as e:
                logging.error(f'Failed to ingest {file}: {e}')
    end = time.time()
    logging.info('--------Ingestion Complete!!!--------')
    logging.info(f'Total Time Taken: {(end - start)/60:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()
