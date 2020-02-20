import time
import os

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
import numpy as np
import glob

import psycopg2
from sqlalchemy import create_engine

import mm_plot as mmplt
import mm_math

def analyze(n_minutes):

    # Create an engine instance
    alchemyEngine   = create_engine('postgresql+psycopg2://antoine:@127.0.0.1:5432/test_ccm');

    # Connect to PostgreSQL server
    postgreSQLConnection    = alchemyEngine.connect();
    postgreSQLTable         = "ccm";

    # find most recent timestamped data
    df = pd.read_sql("SELECT * FROM ccm ORDER BY timestamp DESC LIMIT 1", postgreSQLConnection)
    last_timestamp = df.iloc[0]['timestamp']

    # Read data from PostgreSQL database table and load into a DataFrame instance
    psql_request_str = "SELECT * FROM ccm WHERE timestamp >='" + str(last_timestamp-datetime.timedelta(minutes=n_minutes)) + "'"
    df = pd.read_sql(psql_request_str, postgreSQLConnection);
    #pd.set_option('display.expand_frame_repr', False);
    
    # Close connection
    postgreSQLConnection.close();
    
    return df   
