import numpy as np
import matplotlib.pyplot as plt


# Load position, time, and encounter window data
position = np.load('position_geo.npy')
times_jd = np.load('times_jd.npy')
imaging_windows = np.load('imaging_windows.npy', allow_pickle = True)

LON = position[:, 1]
LAT = position[:, 0]

target_latitude =  43.6532
target_longitude =  -79.3832

for window in imaging_windows:
  plt.plot(LON[window], LAT[window])

plt.scatter(target_longitude, target_latitude)
plt.xlabel("Longitude (Degrees)")
plt.ylabel("Latitude (Degrees)")
plt.show()


# Haversine's formula 

