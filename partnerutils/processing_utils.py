"""********************************************
* A couple utility functions to help with processing data
********************************************"""
from arcgis.geocoding import batch_geocode
from partnerutils.cool_utils import memoize, chunk

@memoize
def batch_geocode_memo(addresses, **kwargs):
    """Batch geocodes a list of addresses and memoizes the results
    to avoid repeated calls and credit consumption.

    args: 
    addresses - the addresses to geocode
    
    **kwargs:
    cache_path - persist the results to a file
    get_key - function to uniquely identify each address
    all others from here:
    https://developers.arcgis.com/python/api-reference/arcgis.geocoding.html?highlight=batch_geocode#arcgis.geocoding.batch_geocode"""

    output = []
    for c in chunk(addresses): # split into chunks for large volumes
        results = batch_geocode(addresses=c, **kwargs)
        output += results

    return output