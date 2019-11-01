"""utility functions to assist with features and feature data types"""

from arcgis.geometry import SpatialReference, Point
import pandas as pd

def sdf_from_xyz(df, x_col, y_col, z_col=None, sr=None):
    """builds a SpatialDataFrame from DataFrame with
    x, y, and z columns
    
    args:
    df - the dataframe
    x_col - the dataframe column corresponding to x coordinate
    y_col - the dataframe column corresponding to y coordinate
    z_col - optional, the dataframe column corresponding to z coordinate
    sr - the spatial reference for the spatial data frame
    """

    if not z_col:
        return pd.DataFrame.spatial.from_xy(df, x_col, y_col, sr)
    
    def point_for_row(x, y, z, sr):
        return Point({'x' : x, 'y' : y, 'z': z, "spatialReference" : sr})
    
    if sr is None:
        sr = SpatialReference({'wkid' : 4326})

    df_geom = df.apply(lambda row: point_for_row(row[x_col],
                                                row[y_col],
                                                row[z_col],
                                                sr), axis=1)
    sdf = df.spatial.set_geometry(df_geom, sr=sr)
    return sdf

