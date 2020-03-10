import datetime

import pandas as pd
from sqlalchemy import create_engine


def analyze(n_minutes):
    # Create an engine instance
    alchemy_engine = create_engine('postgresql+psycopg2://antoine:@127.0.0.1:5432/test_ccm')

    # Connect to PostgreSQL server
    psql_connection = alchemy_engine.connect()
    psql_table_name = "ccm"

    # Query most recent timestamp-ed data
    df = pd.read_sql("SELECT * FROM ccm ORDER BY timestamp DESC LIMIT 1", psql_connection)

    # Save timestamp value
    last_timestamp = df.iloc[0]['timestamp']

    # Read data from PostgreSQL database table and load into a DataFrame instance
    psql_request_str = "SELECT * FROM ccm WHERE timestamp >='" + str(
        last_timestamp - datetime.timedelta(minutes=n_minutes)) + "'"
    df = pd.read_sql(psql_request_str, psql_connection);

    df.sort_values(by=['timestamp'], inplace=True)
    df['data_toggle'] = df['data_counter'].diff()
    df.query('data_toggle>0', inplace=True) # inplace=True to modify df and not returning a modified copy

    phys_data_list = ['cbpm_x', 'cbpm_y']
    res_data_list = ['cpbm_xres', 'cbpm_yres']
    for x, y in zip(phys_data_list, res_data_list):
        # df[x] -= df[x].loc[:100].mean()
        df[y] = df[x].rolling(100).std()

    # Close connection to PostgreSQL server
    psql_connection.close()

    return df
