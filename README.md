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

## How It Works

Our ETL pipeline follows a simple plot:

1. **Extract**: We source our data from an XLSX file, utilizing pandas' data-handling superpowers.

2. **Transform**: Using Apache Beam, we perform data transformations, clean text columns, and create a transformed dataset ready for action.

3. **Load**: We usher the transformed data into a PostgreSQL database, following your configuration settings in `db_config.py`.

## Configuration

To set the stage for your data adventure, make sure to configure your database connection settings in `db_config.py`. You can define the table structure and database connection parameters here.

## Instructions

To run the ETL pipeline:

1. Ensure you've met the prerequisites mentioned above.

2. Set the `POSTGRESQL_PASSWORD` environment variable with your PostgreSQL database password.

3. Replace `'partners_data.xlsx'` in `main.py` with the path to your XLSX file containing partner data.

4. Replace the database connection options in `db_config.py` with your PostgreSQL database details.

5. Run the pipeline with the following command:

   ```sh
   python main.py
   ```
