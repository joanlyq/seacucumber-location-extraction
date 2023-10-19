import os
import shutil
import argparse

# Function to find and copy shapefiles with specific keywords in their names
def find_and_copy_shapefiles_with_keywords(root_folder, keywords, destination_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.shp'):
                # Construct the full path to the shapefile
                shp_path = os.path.join(root, file)
                

                # Check if the keywords are in the filename
                if all(keyword in file for keyword in keywords):
                    # Copy the shapefile and related files to the destination folder
                    print(shp_path)
                    prj_path = shp_path.replace(".shp", ".prj")
                    shx_path = shp_path.replace(".shp", ".shx")
                    dbf_path = shp_path.replace(".shp", ".dbf")

                    # Copy the files
                    for source_file in [shp_path, prj_path, shx_path, dbf_path]:
                        destination_file = os.path.join(destination_folder, os.path.basename(source_file))
                        shutil.copy2(source_file, destination_file)

def main():
    parser = argparse.ArgumentParser(description="Find and copy shapefiles with specific keywords.")
    parser.add_argument("root_folder", help="Root folder to start searching for shapefiles.")
    parser.add_argument("keywords", nargs="+", help="Keywords to search for in shapefile names.")
    parser.add_argument("destination_folder", help="Destination folder to copy shapefiles to.")
    args = parser.parse_args()

    if not os.path.exists(args.destination_folder):
        print("not exist {}".format(args.destination_folder))
        os.makedirs(args.destination_folder)

    find_and_copy_shapefiles_with_keywords(args.root_folder, args.keywords, args.destination_folder)

    print("Shapefiles copied to the destination folder.")

if __name__ == "__main__":
    main()
