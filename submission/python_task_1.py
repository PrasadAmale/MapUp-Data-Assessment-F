import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    
    df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    return df


def get_type_count(df)->dict:
    x = list(df.car)
    y = [ ]
    for i in x:
        if i <= 15:
            y.append("low")
        elif i >= 15 and i <= 25:
            y.append("medium")
        else:
            y.append('high')

    df['car_type'] = y

    dict1 = {}
    set1 = set(y)
    for i in set1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i] = y.count(i)

    dict= dict(sorted(dict1.items(), key=lambda item: item[0]))
    
    return dict()


def get_bus_indexes(df)->list:
    
    import numpy as np
    m1 = df['bus'].mean()
    list = sorted(list((np.where(df['bus'] > 2*m1))[0]))
    
    return list()


def filter_routes(df)->list:
    a1 = df.groupby('route')['truck'].mean()
    list = sorted(list(a1[a1 > 7]))
    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    
    matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25).round(1)
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
