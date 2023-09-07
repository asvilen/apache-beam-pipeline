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
