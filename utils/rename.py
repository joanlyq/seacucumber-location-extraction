import os
import re

# Function to rename files recursively
def rename_files_recursively(root_directory):
    for root, _, files in os.walk(root_directory):
        for filename in files:
            # Check if the file matches the expected format
            if "DESKTOP-14SK5S9" in filename or ".lock" in filename:
                continue

            match = re.match(r'tracks-points-(\d{6})-rov-(am|pm)', filename)
            if match:
                date_part, am_pm = match.groups()
                yyyymmdd = f"20{date_part[4:6]}{date_part[2:4]}{date_part[:2]}"
                file_extension = os.path.splitext(filename)[1]
                new_filename = f"{yyyymmdd}{am_pm}-rov-trackpts{file_extension}"
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')

# Root directory to start the recursive search
root_directory = "E:\Oct2022"

rename_files_recursively(root_directory)
