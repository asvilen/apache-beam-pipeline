# Custom imports
from data_transformation import MissingValueFilter, TextColumnCleaner, TransformData
from db_config import source_config, table_config
# Beam imports
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from beam_nuggets.io import relational_db
# Other imports
import pandas as pd


# Define the main function for the data pipeline
def run_pipeline():
    # Define the pipeline options
    options = PipelineOptions()

    # Create a pipeline
    with beam.Pipeline(options=options) as p:
        # Read data from the XLSX file using pandas
        data = (
                p
                | 'Read from XLSX' >> beam.Create(pd.read_excel('partners_data.xlsx').to_dict(orient='records'))
                | 'Filter Missing Values' >> beam.ParDo(MissingValueFilter())
                | 'Clean Text Columns' >> beam.ParDo(TextColumnCleaner())
                | 'Transform Data' >> beam.ParDo(TransformData())
        )

        # Write transformed data to the Database
        data | 'Writing to DB table' >> relational_db.Write(
            source_config=source_config,
            table_config=table_config
        )


if __name__ == "__main__":
    run_pipeline()

# Instructions for running the pipeline:
# 1. Ensure Apache Beam, pandas, and psycopg2 are installed.
# 2. Set the DB_PASSWORD environment variable with your database password.
# 3. Save the script to a file (e.g., etl_pipeline.py).
# 4. Replace 'your_sample_data.xlsx' with the path to your XLSX file.
# 5. Replace the other database connection options with your PostgreSQL database details.
# 6. Run the pipeline with the following command:
#    python etl_pipeline.py
