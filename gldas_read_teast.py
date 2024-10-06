import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
#from nasaLib import getNasaData 
import pandas as pd

# Using netCDF4 to read the .nc4 file
file_path = '/home/guerrero/Downloads/GLDAS_NOAH025_3H.A19480101.0300.020.nc4'
ds = nc.Dataset(file_path)

# Explore the dataset
print(ds.variables.keys())  # Check available variables

# Access a specific variable, e.g., soil moisture
soil_moisture = ds.variables['SoilMoi0_10cm_inst'][:]  # Example variable name
np.shape(ds)
np.shape(soil_moisture)
# Plotting the soil moisture (assuming it's 2D data)

inverted_image = np.flipud(soil_moisture[0, :, :])
print(np.shape(inverted_image))
plt.imsave('test_NASA.png', inverted_image)
plt.imshow(soil_moisture[0, :, :], cmap='viridis')  # Modify for the time index
plt.colorbar()
plt.title("Soil Moisture 0-10cm Layer")
plt.gca().invert_yaxis()
plt.show()


# Alternatively, using xarray for higher-level manipulation
ds_xr = xr.open_dataset(file_path)
print(ds_xr)
soil_moisture_xr = ds_xr['SoilMoi0_10cm_inst']
soil_moisture_xr[0].plot()
plt.show()


# Iterative 

links = pd.read_csv('~/Documents/UNAM/9TH-SEMESTER/SpaceApps/links.csv')
links = links.to_numpy()
rows = len(links)





