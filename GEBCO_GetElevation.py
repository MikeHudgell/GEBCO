import numpy as np
import netCDF4

def geo_idx(dd, dd_array):
    #
    #   returns the index of the closest degrees decimal value in the array.
    #   dd = degrees decimal (Float64)
    #   dd_array = arrach of degrees decimal values (Float64)
    #
    #
    geo_index = (np.abs(dd_array - dd)).argmin()
    return geo_index

def open_GEBCO_file(filepath):
    #
    #   returns dataset in NetCDF format and from the dataset arrays of the latitudes and longitudes
    #   filepath = filepath to GEBCO file
    #
    #
    NetCDF_dataset = netCDF4.Dataset(filepath)
    lats = NetCDF_dataset.variables['lat'][:]
    lons = NetCDF_dataset.variables['lon'][:]
    return NetCDF_dataset, lats, lons

def get_GEBCO_info(dataset):
    #
    #   prints metadata in GEBCO file
    #
    #
    print(dataset.data_model)

    for attr in dataset.ncattrs():
        print(attr, '=', getattr(dataset, attr))

    print(dataset.variables)
    return

def get_elevation(lat, lon):
    #
    # returns the elevation given a latitude and longitude
    #
    lat_index = geo_idx(lat, lats)
    lon_index = geo_idx(lon, lons)
    return gebco.variables['elevation'][lat_index, lon_index]

#
#
#Sea floor height (above mean sea level)
#
#
#Tests
#
gebco, lats, lons  = open_GEBCO_file('/media/mike/HDD/git/GEBCO/data/GEBCO_2014_2D.nc')
#
#
print(get_elevation(51.65, -3.2))
#
# individual tests
#
get_GEBCO_info(gebco)
lat_index = geo_idx(51.65, lats)
lon_index = geo_idx(-3.2, lons)
print('Latitude index: ', lat_index)
print('Longitude index: ', lon_index)
print('Latitude @ index: ', gebco.variables['lat'][lat_index])
print('Longitude @ index: ', gebco.variables['lon'][lon_index])
print('Elevation at location: ', gebco.variables['elevation'][lat_index, lon_index])


print(get_elevation(51.464, 1.0485))
print(get_elevation(26.259, 52.622))
print(get_elevation(33.474, 120.712))
