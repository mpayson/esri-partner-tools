"""Functions that I want to remember and hopefully you will too!"""

import glob
import os
import pandas as pd

def chunk(row, n=1000):
    """chunk generator function for breaking up requests
    such as for Esri's geocoder
    
    args:
    row - the object to be chunked
    n - chunk size
    """
    for i in range(0, len(row), n):
        yield row[i:i + n]

def chunk_df(df, n=1000):
    """chunk generator function for breaking up requests with dataframes

    args:
    df - the dataframe to be chunked
    n - chunk size
    """
    
    for i in range(0, len(df), n):
        yield df.iloc[i:i + n].copy()

def csvs_to_df(dir_path):
    """concats all csvs in a directory to one dataframe
    
    args:
    dir_path - path to dir containing csvs
    """

    all_csvs = glob.glob(os.path.join(dir_path, '*.csv'))
    return pd.concat((pd.read_csv(f) for f in all_csvs if os.stat(f).st_size > 0))