# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km

# Parameters:
#  lat_deg: Latitude in degrees
#  lon_deg: Longitude in degrees
#  hae_km : Height above ellipsoid in km

# Written by Sean Rockett
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys
import math

# "constants"
R_E_KM = 6378.137
E_E = 0.081819221456

# helper functions
def calc_denom(ecc,lat_deg):
    return math.sqrt(1.0-(ecc**2)*(math.asin(lat_deg))**2)

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
lat_deg = float('nan')
lon_deg = float('nan')
hae_km = float('nan')

# parse script arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print(\
    'Usage: '\
    'python3 arg1 arg2 arg3'\
    )
    exit()

# write script below this line

denom = calc_denom(E_E,lat_deg)
C_E = R_E_KM/denom
S_E = R_E_KM*(1-E_E*E_E)/denom

r_x_km = (C_E+hae_km)*math.acos(lat_deg)*math.acos(lon_deg)
r_y_km = (C_E+hae_km)*math.acos(lat_deg)*math.asin(lon_deg)
r_z_km = (S_E+hae)*math.asin(lat_deg)

print('r_x_km')
print('r_y_km')
print('r_z_km')