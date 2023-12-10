import pandas as pd
import numpy as np

def calculate_distance_matrix(df)->pd.DataFrame():
    
    from scipy.spatial.distance import squareform, pdist
    u2_values = squareform(pdist(df.iloc[:, 1:]))
    u2_index = pd.Index(df['id_start'])

    df = pd.DataFrame(u2_values, columns=u2_index, index=u2_index)

    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    df1 = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])

    for start_id, row in df.iterrows():
        for end_id, distance in row.items():
            if start_id != end_id:
                unrolled_distances = unrolled_distances.append({
                'id_start': start_id,
                'id_end': end_id,
                'distance': distance
                            }, ignore_index=True)

    return df1


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():

    ind1 = np.where(reference_id['reference_id'])        
    avg1 = reference_id['distance'].iloc[ind1].mean()
    lb1 = avg1* 0.90
    up1 = avg1 * 1.10
    a1 = np.where(df1['distance'] >= lb1)
    a2 = np.where(df1['distance'] <= up1)
    unique_ids_a1 = np.unique(df1['id_start'].iloc[a1[0]])
    unique_ids_a2 = np.unique(df1['id_start'].iloc[a2[0]])
    l1 = list(set(l1 + unique_ids_a1.tolist() + unique_ids_a2.tolist()))
    df = pd.DataFrame(l1)
    return df


def calculate_toll_rate(df)->pd.DataFrame():
   rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
   df2= df1.copy()
   for vehicle_type, rate_coefficient in rate_coefficients.items():
    column_name = f"{vehicle_type}_toll"
    df2[column_name] = df2['distance'] * rate_coefficient
        
    return df2


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
