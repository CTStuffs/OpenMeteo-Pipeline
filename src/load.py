
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy_utils import database_exists, create_database

import logging

logger = logging.getLogger(__name__)

def load_to_db(df):
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_database_name = os.getenv('DB_DATABASE_NAME')

    logger.info("Connecting to database...")
    try:
        engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_database_name}")

        if not database_exists(engine.url):
            create_database(engine.url)

        table_name = os.getenv('DB_TABLE_NAME')

        logger.info("Loading data into database...")
        with engine.begin() as conn:
            df.to_sql(table_name, conn, if_exists="append", index=False)
    except SQLAlchemyError as e:
        logger.error("Error occurred while loading data into database: %s", e)
    else:
        logger.info("Load success!")
