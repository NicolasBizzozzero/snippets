import numpy as np
import pandas as pd


def remove_outliers(dataframe, column, tolerance):
    """ Remove all outliers that are not within +`tolerance` to -`tolerance`
    standard deviations in the column `column`.
    """
    return dataframe[np.abs(dataframe[column] - dataframe[column].mean()) <=
                     (tolerance * dataframe[column].std())]


def fill_values(dataframe, value_to_fill, filling_value=np.nan,
                method='ffill', inplace=False):
    if inplace:
        dataframe.replace(value_to_fill, filling_value,
                          inplace=True).fillna(method=method, inplace=True)
    else:
        return dataframe.replace(value_to_fill,
                                 filling_value).fillna(method=method)


if __name__ == '__main__':
    import glob
    dfs = [pd.read_csv(file_name, parse_dates=['creationdate'])
           for file_name in glob.glob('../data/stackoverflow/*.csv')]
    df = pd.concat(dfs)
    df.head()
