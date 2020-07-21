"""Functions that I want to remember and hopefully you will too!"""

import glob
import os
import json
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

def read_json(path):
    """Read in a JSON file as a dictionary
    
    args:
    path - path to the JSON file"""
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def write_json(path, obj):
    """Write a dictionary to a file

    args:
    path -- path to the output JSON file
    obj -- dictionary to write"""
    with open(path, 'w') as f:
        json.dump(obj, f)

def memoize(f):
    """Decorator to memoize function calls that receive a list
    as their first argument, useful to avoid expensive operations
    
    args:
    f -- the function to memoize"""

    cache = {}

    def execute(input_list, *args, **kwargs):
        cache_path = kwargs.pop('cache_path', None)
        get_key = kwargs.pop('get_key', lambda i: str(i))
        
        if cache_path:
            cache.update(read_json(cache_path))

        keys = set()
        process = []
        for i in input_list:
            key = get_key(i)
            if key not in cache and key not in keys:
                process.append(i)
                keys.add(key)

        if len(process) > 0:
            results = f(process, *args, **kwargs)
            for i, p in enumerate(process):
                cache[get_key(p)] = results[i]

        if cache_path:
            write_json(cache_path, cache)

        return [cache[get_key(i)] for i in input_list]

    return execute