
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

import logging

logger = logging.getLogger(__name__)

def load_to_db(df):
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_database_name = os.getenv('DB_DATABASE_NAME')

    logger.info("Connecting to database...")
    engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_database_name}")

    table_name = os.getenv('DB_TABLE_NAME')

    logger.info("Loading data into database...")
    try:
        with engine.begin() as conn:
            df.to_sql(table_name, conn, if_exists="append", index=False)
    except sqlalchemy.exc.SQLAlchemyError as e:
        logger.error("Error occurred while loading data into database: %s", e)
    logger.info("Load success!")
