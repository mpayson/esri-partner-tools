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

def extract(obj, keys, **kwargs):
    """returns a nested object value for the specified keys
    
    args:
    obj -- the nested object containing the desired value
    keys -- list of keys to drill through object
    """
    required = kwargs.pop('required', False)
    default = kwargs.pop('default', None)
    warn = kwargs.pop('warn', False)
    
    o = obj
    for i in range(0, len(keys)):
        try:
            o = o[keys[i]]
        except (KeyError, IndexError):
            if warn:
                print('Warning key does not exist. Key: {0} in Keys: {1}'.format(keys[i], keys))
            if required and default == None:
                raise KeyError('Required key does not exist in object and no default')
            return default
    return o

def d_extract(obj, keys_delimited, **kwargs):
    """returns a nested object value for '.' delimited keys
    
    args: 
    obj -- the nested object containing the desired value
    keys -- a '.' delimited string of keys to drill through"""
    keys = keys_delimited.split('.')
    return extract(obj, keys, **kwargs)