# Open-Meteo Data Pipeline Demo

A Python-based ETL pipeline that queries data from [Open Meteo](https://open-meteo.com/) applies cleaning and transformation logic, and loads the result a local PostgreSQL database. 


## Project Overview

- Extract: read raw weather data from the Open Meteo API `data/raw/`.
- Transform: clean, normalize, and validate rows in `src/transform.py`.
- Load: append transformed results into a local PostgreSQL table using `src/load.py`.
- Test: unit tests for above three tasks in `test/`

## Architecture

- `main.py` — pipeline orchestrator using environment variables.
- `src/extract.py` — API querying logic.
- `src/transform.py` — data validation, normalization, and type conversion.
- `src/load.py` — Database upload
- `data/` — local data storage
- `test/` — unit tests
- `logging-config.py` — specifies logging features


## Quick Start

1. Install dependencies:

```bash
pip install requests pytest pandas sqlalchemy python-dotenv sqlalchemy-utils
```

2. Setup your local [PostgreSQL](https://www.postgresql.org/) Database

3. Configure environment variables in `.env`:

```text
DB_USERNAME=<Your PostgreSQL DB username>
DB_PASSWORD=<Your PostgreSQL DB password>
DB_HOST=<Your PostgreSQL DB host name>
DB_PORT=<Your PostgreSQL DB host port>
DB_DATABASE_NAME=<DB name>
DB_TABLE_NAME=<table name>
```

3. Run the pipeline:

Ensure that your PostgreSQL DB is running. Then run:

```bash
python main.py
```

## Testing
```
pytest test/
```

## Output

- Cleaned dataset loaded into DB_TABLE_NAME under DB_TABLE_NAME
- Duplicate rows are removed, rows with missing data are dropped, specific column headers are renamed to be more informative and numeric fields are normalized.

