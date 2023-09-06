# ETL Pipeline for using Apache Beam

## Overview

This ETL (Extract, Transform, Load) pipeline is designed to process partner data, perform necessary data transformations, and load it into a PostgreSQL database. It uses Apache Beam and pandas to handle data extraction, transformation, and loading tasks efficiently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Configuration](#configuration)
- [Instructions](#instructions)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the ETL pipeline, make sure you have the following prerequisites:

- [Python](https://www.python.org/downloads/) (>= 3.7)
- [Apache Beam](https://beam.apache.org/get-started/quickstart-py/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
- [psycopg2](https://pypi.org/project/psycopg2/)

## Project Structure

The project consists of the following files:

- `data_transformation.py`: Contains custom data transformation functions using Apache Beam.
- `db_config.py`: Configuration file for defining the database table structure.
- `main.py`: The main script for running the ETL pipeline.

## Usage

To use this ETL pipeline, follow the instructions below:

## Configuration

Before running the pipeline, make sure to configure your database connection settings in `db_config.py`. You can define the table structure and database connection parameters.

## Instructions

To run the ETL pipeline:

1. Ensure you've met the prerequisites mentioned above.

2. Set the `POSTGRESQL_PASSWORD` environment variable with your PostgreSQL database password.

3. Save the script to a file (e.g., `etl_pipeline.py`).

4. Replace `'partners_data.xlsx'` in `main.py` with the path to your XLSX file containing partner data.

5. Replace the database connection options in `db_config.py` with your PostgreSQL database details.

6. Run the pipeline with the following command:

   ```sh
   python etl_pipeline.py
