import numpy as np
import pandas as pd
import seaborn as sns


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


def correlation_heatmap(dataframe):
    """ Compute and show a correlation heatmap for all attribute in
    `dataframe`.
    """
    correlation = dataframe.corr()
    sns.heatmap(correlation, xticklabels=correlation.columns.values,
                yticklabels=correlation.columns.values)


if __name__ == '__main__':
    pass
