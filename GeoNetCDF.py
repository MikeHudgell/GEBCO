import numpy as np
import netCDF4

def geo_idx(dd, dd_array):
    print(dd_array - dd)
    print(dd_array.shape, dd_array.dtype)
    geo_index = (np.abs(dd_array - dd)).argmin()
    return geo_index

gebco = netCDF4.Dataset('/media/mike/HDD/git/gebco/data/GEBCO_2014_2D.nc')
lats = gebco.variables['lat'][:]
lons = gebco.variables['lon'][:]
print(lats.shape)
print(lons.shape)

print(gebco.variables['elevation'][10,10])
print(gebco.variables['lat'][10])
print(gebco.variables['lon'][10])
# results
#
#  2797
# -89.9125
# -179.9125
in_lat = -89.9125
in_lon = -179.9125
lat_index = geo_idx(in_lat, lats)
lon_index = geo_idx(in_lon, lons)
print(lat_index)
print(lon_index)
print(gebco.variables['elevation'][lat_index, lon_index])

in_lat = 51.65
in_lon = -3.2
lat_index = geo_idx(in_lat, lats)
lon_index = geo_idx(in_lon, lons)
print(lat_index)
print(lon_index)
print(gebco.variables['lat'][lat_index])
print(gebco.variables['lon'][lon_index])
print(gebco.variables['elevation'][lat_index, lon_index])
