import argparse
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os

def main():
    parser = argparse.ArgumentParser(description="Match items in a CSV file with the closest timestamps in shapefiles and save the result to a new CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file with item data")
    parser.add_argument("shapefile_folder", help="Path to the folder containing shapefiles")
    parser.add_argument("output_csv", help="Path to the output CSV file")

    args = parser.parse_args()

    # Load the CSV file with item data
    csv_df = pd.read_csv(args.csv_file)

    # Extract the date part from the CSV timestamp
    csv_df['date'] = csv_df['datetime'].str.split().str[0]
    csv_df['datetime'] = pd.to_datetime(csv_df['datetime'])  # Replace 'datetime_field' with your datetime column name
    dates = csv_df['date'].unique()
    
    gdfs_shapefiles = gpd.GeoDataFrame()
    for date in dates:
        date = date.replace("-","")
        # List files in the folder
        file_list = os.listdir(args.shapefile_folder)

        # Filter files containing the modified string
        matching_files = [os.path.join(args.shapefile_folder, file) for file in file_list if date in file and file.endswith('.shp')]
        # read shp file that is collected on that day
        for file in matching_files:
            gdf_shapefile = gpd.read_file(file)
            gdfs_shapefiles = pd.concat([gdfs_shapefiles,gdf_shapefile], ignore_index=True)
    
    # Initialize a list to store the results
    nearest_features = []
    closest_lats = []
    closest_lons = []
    closest_timestamps = []

    # Iterate through each item in the CSV and find the nearest feature in the shapefile
    for index, csv_item in csv_df.iterrows():
        target_datetime = csv_item['datetime']
        gdfs_shapefiles['ltime'] = pd.to_datetime(gdfs_shapefiles['ltime'])
        # Calculate the time difference between each feature in the shapefile and the target datetime
        gdfs_shapefiles['time_difference'] = (gdfs_shapefiles['ltime'] - target_datetime).abs()  # Replace 'datetime_column_name' with your shapefile's datetime column

        # Find the feature with the smallest time difference
        closest_feature = gdfs_shapefiles.loc[gdfs_shapefiles['time_difference'].idxmin()]
        closest_lats.append(closest_feature.geometry.y)
        closest_lons.append(closest_feature.geometry.x)
        closest_timestamps.append(closest_feature['ltime'])  # Replace 'datetime_column_name' with your shapefile's datetime column


        # Store the result
        nearest_features.append((csv_item, closest_feature))
    
    csv_df['closest_lat'] = closest_lats
    csv_df['closest_lon'] = closest_lons
    csv_df['closest_timestamp'] = closest_timestamps
        
    print(csv_df)

    csv_df.to_csv(args.output_csv, index=False)

if __name__ == "__main__":
    main()

    print("\n\nDONE")
    print("\n\n\n\t /\_ /\    ♡\n\t(• - • ̳)\n\t |、ﾞ~ヽ\n\t じしf_; )ノ \n    © Joan Li, 2023")

