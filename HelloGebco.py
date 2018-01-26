import netCDF4
from mpl_toolkits.basemap import Basemap
import numpy as np

# Load data
dataset = netCDF4.Dataset('/media/mike/HDD/git/gebco/data/GEBCO_2014_2D.nc')

for attr in dataset.ncattrs():
    print(attr, '=', getattr(dataset, attr))

print(dataset.dimensions)
print(dataset.dimensions.keys())
print(dataset.dimensions['lon'])
print(dataset.dimensions['lat'])

print(dataset.variables['lon'])
print(dataset.variables['lat'])

print(dataset.data_model)
print(dataset.variables)
print(dataset)

mylat = 51
mylon = -1

print(dataset.variables['elevation'][10,10])
print(dataset.variables['lat'][10])
print(dataset.variables['lon'][10])
# results
#
#  2797
# -89.9125
# -179.9125
print(dataset.variables['lon'] == -179.9125)

