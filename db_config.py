from sqlalchemy import Table, Column, INT, VARCHAR, FLOAT
import os
from beam_nuggets.io import relational_db


# Define a function to set up the database table
def table_setup(metadata):
    return Table(
        'interview_table', metadata,
        Column('date_key', INT, primary_key=True),
        Column('partner_id', INT, primary_key=True),
        Column('partner', VARCHAR(50)),
        Column('partner_type', VARCHAR(50)),
        Column('country', VARCHAR(50)),
        Column('unique_clicks', INT),
        Column('new_registrations', INT),
        Column('first_time_depositing', INT),
        Column('cpa_triggered', INT),
        Column('cpa_earnings_eur', FLOAT),
        Column('rev_share_earnings_eur', FLOAT),
        Column('amount_deposited_eur', FLOAT),
        Column('net_revenue_eur', FLOAT)
    )


# Define database connection configurations
source_config = relational_db.SourceConfiguration(
    drivername='postgresql+pg8000',
    host='localhost',
    port=5432,
    username='postgres',
    password=os.environ.get("POSTGRESQL_PASSWORD"),
    database='blue_window_db',
    create_if_missing=True  # create the database if not there
)

table_config = relational_db.TableConfiguration(
    name='interview_table',
    create_if_missing=True,
    define_table_f=table_setup
)
