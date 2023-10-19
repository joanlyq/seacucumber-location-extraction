# Sea Cucumber Location Extraction from ROV Data

This code is used specifically to extract sea cucumber location data on Remotely Operated Vehicle (ROV) missions through a collaboration between Macquarie University (MQ), GeoNadir, and the University of Newcasctle (UoN). It matches items in a CSV file with the closest timestamps in shapefiles and saves the results to a new CSV file.

## Installation

To run this code, you should follow these steps to set up the necessary environment:

## Installation

To run this code, you need to set up the necessary environment. Here's how to do it:

1. **Install Miniconda (Optional)**

   If you don't have Miniconda or Anaconda installed, you can download and install Miniconda, a minimal installer for Conda. Visit the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions for your operating system.

2. **Create a Conda Environment (Optional)**

   Once Miniconda is installed, you can create a new Conda environment for this project. Open your terminal or command prompt and execute the following commands:

   - Create a new environment:

     ```bash
     conda create -n seacucumber-env python=3.7
     ```

   - Activate the environment:

     ```bash
     conda activate seacucumber-env
     ```

3. **Install Required Libraries**

   Install the necessary libraries using `pip` or `conda` in your environment:

   ```bash
   pip install geopandas pandas shapely argparse fiona pyogrio
   ```

   or with Conda:

   ```bash
   conda install -c conda-forge geopandas pandas shapely fiona pyogrio
   ```

4. **Download and Organize Your Data**

   - Prepare your CSV file with item data and **ensure it has a 'datetime' column**. The format of the date and time shoud be compatible with [ISO format](https://en.wikipedia.org/wiki/ISO_8601), e.g. YYYY-DD-MM hh:mm:ss
   - All rov gps track has been renamed and organised in the [./rov_trackpts](./rov_trackpts) folder, with each shapefile containing a 'ltime' (timestamp) field.


## Running the Code

To execute the code, follow these steps:

1. Open your terminal or command prompt.

2. Download the code from the GitHub repository to your desired location using the `git clone` command. Use the download button above or specify the directory where you want to save the code with the command below:

   ```bash
   git clone repository_url /path/to/your/code-directory
   ```
   and navigate to the directory where the code script is located:
   ```bash
   cd /path/to/your/code-directory
   ```

3. Run the code with the following command, replacing the placeholders with your specific file paths:

   ```bash
   python main.py /path/to/your/csv_file.csv /path/to/your/shapefile_folder /path/to/output_csv_file.csv
   ```

   Example:

   ```bash
   python main.py ./test/gouldreef-rov-id.csv ./rov_trackpts ./test/gouldreef-output-test.csv
   ```

4. The code will process the data and generate the output CSV file with sea cucumber locations.

5. You can visualise the cuke location in QGIS or other gis platform that can read csv files.

---

**Note:** This code is designed for a specific collaborative project and may require customization for use in other contexts.

© Joan Li, 2023

*Make sure to customize the installation and usage instructions with your specific file paths and script name.*