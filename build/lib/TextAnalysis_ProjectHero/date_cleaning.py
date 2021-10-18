"""
This module create a date column for a dataframe based on its "Label" column
"""
import pandas as pd
import datetime

def fill_date(slice,col):
    """Fill in empty rows of a date column in a dataframe

    Parameters
    ----------
    slice : dataframe
        Name of the dataframe 
        
    col : string
        Name of date column that needs to be filled
        

    Returns
    -------
    slice : dataframe
        New dataframe with a filled date column
    """
    slice[col] = slice[col].ffill()
    return slice

def set_date(slice):
    """Extract date information from a column called "Label" in a dataframe

    Parameters
    ----------
    slice : dataframe
        Name of a dataframe
        

    Returns
    -------
    slice : dataframe
        New dataframe with a proper date column

    """
    slice.loc[slice['Label'].ne('null'),'Date']=slice['Label']
    slice = fill_date(slice,'Date')
    slice['Date'] = [slice.loc[i,'Date'][:10] for i in range(len(slice['Date']))]
    slice['Date'] = slice['Date']= slice['Date'].apply(lambda x: x.replace('_','/'))
    slice['Date'] = pd.to_datetime(slice['Date'])
    return slice

