
import xarray as xr

'''
import cdsapi

dataset = "cams-global-reanalysis-eac4"
request = {
    "variable": [
        "black_carbon_aerosol_optical_depth_550nm",
        "total_aerosol_optical_depth_469nm",
        "total_column_ethane"
    ],
    "date": ["2018-01-01/2023-12-31"],
    "time": ["12:00"],
    "data_format": "grib",
    
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
'''

# Load your GRIB file using xarray
grib_file_path = '/home/guerrero/Documents/UNAM/9TH-SEMESTER/SpaceApps/cd9e9434c008897708fb23c25e857ef7.grib'

ds = xr.open_dataset(grib_file_path, engine='cfgrib')

# Convert the xarray dataset to a Pandas DataFrame
df = ds.to_dataframe().reset_index()

# Save the DataFrame to a CSV file for easy import into R
df.to_csv('output_data_pollution.csv', index=False)
