
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()



def load_to_db(df):
    # connect to db
    # load the new data
    # handle duplicates/errors
    
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_database_name = os.getenv('DB_DATABSE_NAME')

    engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_database_name}")

    table_name = "mytable"

    df.to_sql(table_name, engine, if_exists="append", index=False)

