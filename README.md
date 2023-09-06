# ETL Pipeline using Apache Beam

## Overview

This ETL (Extract, Transform, Load) pipeline is designed to process data, perform necessary data transformations, and load it into a PostgreSQL database. It uses Apache Beam and pandas to handle data extraction, transformation, and loading tasks efficiently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
  - [Data Transformations](#data-transformations)
  - [Resulting Table Structure](#resulting-table-structure)
  - [Primary Keys](#primary-keys)
- [Configuration](#configuration)
- [Instructions](#instructions)
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

### Data Transformations

2. **Transform**: Once the data is extracted, it undergoes a transformation journey, where it is carefully refined and prepared for its new home in the PostgreSQL database. The transformations applied to the data are designed to ensure consistency, cleanliness, and usefulness. Here's what happens:

   - **Date Formatting**: The 'date' column is formatted as a string in the desired format, using the `pd.to_datetime` function. This ensures that the date data is uniform and suitable for further analysis.

   - **Country Normalization**: The 'country' column is normalized using the `country_alpha2_to_country_name` function from the `pycountry_convert` library. This transformation ensures that country names are consistent and standardized. If a country code is not recognized, it's labeled as 'Other' to maintain data integrity.

   - **Unique Partner Key**: A unique partner key is created by combining the partner's name and the normalized country name. This key is used to identify unique partners and is crucial for tracking partner-specific data.

   - **Partner ID Assignment**: A unique partner ID is assigned based on the partner key. If a partner key is encountered for the first time, a new partner ID is generated and associated with that partner. This step ensures that each partner has a unique identifier for reference in the database.

### Resulting Table Structure

3. **Load**: We usher the transformed data into a PostgreSQL database, following your configuration settings in `db_config.py`.

   **Resulting Table Structure**:

   The transformed data is structured into a table with the following columns:

   - `date_key`: An integer representing the date in the format YYYYMMDD, used as a primary key for time-based queries.

   - `partner_id`: A unique identifier for each partner, assigned based on the partner's name and country. This is used as the primary key for partner-related queries.

   - `partner`: The name of the partner.

   - `partner_type`: The type of partner.

   - `country`: The normalized country name, ensuring consistency.

   - `unique_clicks`: The number of unique clicks associated with the partner.

   - `new_registrations`: The count of new registrations attributed to the partner.

   - `first_time_depositing`: The number of first-time depositing users.

   - `cpa_triggered`: The count of Cost Per Action (CPA) triggers.

   - `cpa_earnings_eur`: Earnings in Euros from CPA activities.

   - `rev_share_earnings_eur`: Earnings in Euros from revenue sharing.

   - `amount_deposited_eur`: The total amount deposited in Euros.

   - `net_revenue_eur`: Net revenue in Euros.

### Primary Keys

The resulting table has two primary keys:

- `date_key`: This primary key enables time-based queries and allows you to retrieve data for specific dates or date ranges efficiently.

- `partner_id`: This primary key facilitates partner-specific analysis, ensuring that each partner's data is uniquely identified and accessible.

These primary keys are vital for database performance and data retrieval, enabling precise and efficient querying of the transformed data.

The transformation process ensures that the data is not only clean and consistent but also structured in a way that supports meaningful analysis and insights.


## Configuration

To set the stage for your data adventure, make sure to configure your database connection settings in `db_config.py`. You can define the table structure and database connection parameters here.

## Instructions

To run the ETL pipeline:

1. Ensure you've met the prerequisites mentioned above.

2. Set the `POSTGRESQL_PASSWORD` environment variable with your PostgreSQL database password.

3. Replace `'partners_data.xlsx'` in `main.py` with the path to your XLSX file.

4. Replace the database connection options in `db_config.py` with your PostgreSQL database details.

5. Run the main.py file.

## License

This project is released under the [MIT License](LICENSE). See the LICENSE file for more details.
