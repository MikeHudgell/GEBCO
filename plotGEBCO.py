
import matplotlib
import matplotlib.pyplot as plt

import netCDF4
print(matplotlib.__version__)
gebco = netCDF4.Dataset('/media/mike/HDD/git/GEBCO/data/GEBCO_2014_2D.nc')
elevations = gebco.variables['elevation'][14000:19000,19000:22000]
print(elevations.shape)
print(elevations[1,1])
plt.pcolormesh(elevations, cmap='Accent')
plt.show()

