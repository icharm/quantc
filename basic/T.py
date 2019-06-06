# -*- coding: UTF-8 -*- 
# Draw stock charts toolkit.
import pandas as pd
from highcharts import Highstock

from . import log
from . import dateutils as dt

log = log.Log(__name__)

def xy(df, xdate=True):
    '''
    Translate dataframe to list[list] of coordinate.
    Args:
        df: pandas DataFrame.
        xdate: if x format is date, transform date to seconds.
    Returns:
        coordinate list
    '''
    if not isinstance(df, pd.DataFrame):
        log.error('df_xy() method first parameter must be instance of pandas.DataFrame')
        exit()
    # items count.
    rows = len(df)
    # str date to seconds(timestamp)
    if xdate == True :
        for i in range(rows):
            df.iat[i,0] = dt.seconds(df.iloc[i,0], dt.DF_FULL_NORMAL) * 1000 # must muplity 1000.
    # DataFrame to list([[x,y]...]).
    return df.values.tolist() 

def draw(df, xf, yf, tf, title='New Stock Chart'):
    '''
    Draw hight stock chart by pandas.DataFrame
    Args:
        df: dataFrame
        xf: field name of dataFrame to x coordinate, the value of x must be unique datetime.
        yf: field name of dataFrame to y coordinate.
        tf: field name of dataFrame to line title.
    '''
    uniques = df[tf].unique()
    # log.debug(str(uniques))
    c = Highstock()
    for unique in uniques:
        sel_df = df[df[tf] == unique]
        sel_df = sel_df.loc[:, [xf, yf]]
        xyl = xy(sel_df)
        c.add_data_set(xyl, series_type='line', name=unique)
    
    options = {
        'title' : {
            'text' : title
        },
    }
    c.set_dict_options(options)
    c.save_file()
    log.info('Successful completion of drawing.')