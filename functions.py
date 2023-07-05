import pandas as pd
import numpy as np
from typing import Optional
import glob
import math
from hard_coded_variables import TRAIL_FOLDER_PATH, TRIP_INFO_DATA_PATH
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")


def get_trail_data(start_time:Optional[int],end_time:Optional[int]):
    folder_path = TRAIL_FOLDER_PATH
    csv_files = glob.glob(folder_path)
    filtered_dataframes = []
    for file in csv_files:
        df = pd.read_csv(file,dtype={'lname':str,'osf':str})
        df.sort_values(by='tis',inplace=True)
        if end_time is None and start_time is None:
            filtered_df = df
        elif start_time is not None and end_time is not None:
            filtered_df = df[(df['tis'] >= start_time) & (df['tis'] <= end_time)]
        elif end_time is None or start_time is None:
            filtered_df = df[(df['tis'] >= start_time) | (df['tis'] <= end_time)]
        else:
            pass
        # filtered_df['lat'].fillna(0.00,inplace=True)
        # filtered_df['lon'].fillna(0.00,inplace=True)
        filtered_dataframes.append(filtered_df)
    
    combined_data = pd.concat(filtered_dataframes, ignore_index=True)
    return combined_data



def haversine_formula(lat1, lat2, lon1, lon2):
    if pd.isnull(lat1) or pd.isnull(lon1) or pd.isnull(lat2) or pd.isnull(lon2):
        return 0
    # Haversine formula after converting degrees to radians
    dlat = math.radians(lat2) -  math.radians(lat1)
    dlon = math.radians(lon1) - math.radians(lon2)
    a = abs(math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    radius = 6371  # Earth's radius in kilometers
    # Calculate the distance
    distance = radius * c
    return distance




def aggregate_trail_data(start_time,end_time):
    trail_data = get_trail_data(start_time,end_time) 
    if trail_data.empty:
        raise Exception("no data available for given date range")
    trail_data['Distance_Travelled'] = np.nan
    aggregations = {
    
    'osf': lambda row: row[row=='True'].count(),
    'spd': 'mean'
        }
    result = trail_data.groupby('lic_plate_no').agg(aggregations)
    result['Distance_Travelled'] = trail_data.loc[(trail_data[['lat', 'lon']].notnull()).all(axis=1) &
                                (trail_data[['lat', 'lon']] != 0).all(axis=1)].groupby('lic_plate_no').apply(
    lambda group: haversine_formula(group.loc[group['tis'].idxmin(), 'lat'], 
                                    group.loc[group['tis'].idxmax(), 'lat'],
                                   group.loc[group['tis'].idxmin(), 'lon'],
                                     group.loc[group['tis'].idxmax(), 'lon'])
    if len(group) > 1 else 0)
    result.reset_index(inplace=True)
    return result





def aggregate_trip_info_data():
    df = pd.read_csv(TRIP_INFO_DATA_PATH)
    aggregation = {'transporter_name':'first','trip_id':'count'}
    result = df.groupby('vehicle_number').agg(aggregation)
    result.reset_index(inplace=True)
    return result



def merge_trails_trip_df(start_time,end_time):
    try:
        trails_data = aggregate_trail_data(start_time,end_time)
        # if not isinstance(trails_data,pd.DataFrame):
        #     raise Exception(e)
        aggregate_trip_info_df = aggregate_trip_info_data()
        merged_df = pd.merge(trails_data,aggregate_trip_info_df,
                            left_on='lic_plate_no',right_on='vehicle_number',how='left')
        merged_df.rename(columns={"osf":"Number of Speed Violations","spd":"Average Speed",
                                "vehicle_number":"License plate number",
                                "transporter_name":"Transporter Name",
                                "trip_id":"Number of Trips Completed",
                                "Distance_Travelled":"Distance"},inplace=True)
        return merged_df
    except Exception as e:
        return e


