from src.extract import get_request
from src.transform import transform_request
from src.load import load_to_db
from logging_config import setup_logging

import logging

setup_logging()

logger = logging.getLogger(__name__)


def main():
    logger.info("Beginning OpenMeteo pipeline...")
    json = get_request()
    logger.info("Converting data to dataframe...")
    df = transform_request(json)
    logger.info("Loading data into database...")
    load_to_db(df)
    


if __name__ == "__main__":
    main()