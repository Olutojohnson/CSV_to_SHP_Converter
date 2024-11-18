# CSV to Shapefile Converter

This Python script converts a CSV file containing geographic data (latitude and longitude) into a shapefile (.shp) using the **pandas** and **GeoPandas** libraries.

## Features

| Feature                     | Description                                                       |
|-----------------------------|-------------------------------------------------------------------|
| **Input**                   | Reads geographic data (latitude, longitude) from a CSV file.      |
| **Output**                  | Generates a shapefile (.shp) with geographic points as features.  |
| **Projection Support**      | Includes a Coordinate Reference System (CRS) for the shapefile.   |

## Prerequisites

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

## Usage
1. Input File Format
Prepare your CSV file (data.csv) with the following structure:

| Column Name                 | Description                                         |
|-----------------------------|-----------------------------------------------------|
| **latitude**                | Latitude of the location.                           |
| **longitude**               | Longitude of the location.                          |
| **(Other data)**            | Any additional columns you want in the shapefile.   |

Example:
|  latitude   |  longitude  |      name      |
|-------------|-------------|----------------|
|   -1.2921   |   36.8219   |   Location A   |
|   40.7128   |  -74.0060   |   Location B   |

2. Running the Script
Run the script using the following command:

```bash
python csv_to_shapefile.py
```

3. Output File
The script generates a shapefile named data.shp in the current working directory.

## Workflow Overview
1. **Load CSV**: Reads the input CSV file containing latitude and longitude.
2. **GeoDataFrame Creation**:
   - Converts the data into a GeoDataFrame with geometric points.
   - Ensures the correct CRS is specified using the ESRI WKT format.
3. Shapefile Export: Saves the GeoDataFrame as a shapefile (data.shp).

## Troubleshooting
Issue	Possible Cause	Solution
Missing CRS in Shapefile	CRS was not specified.	Ensure the crs_wkt variable is correctly defined.
Invalid File Format	Incorrect data format in the CSV file.	Ensure the file has latitude and longitude.

|  Issue                 |  Possible Cause                      |      Solution                             |
|------------------------|--------------------------------------|-------------------------------------------|
|Missing CRS in Shapefile|CRS was not specified.                |Ensure the crs_wkt variable is correctly defined.|
|Invalid File Format     |Incorrect data format in the CSV file.|Ensure the file has latitude and longitude.|







