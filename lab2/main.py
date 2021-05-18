import numpy as np
import pandas as pd
from matplotlib import colors
import matplotlib.pyplot as plt
import folium
import webbrowser

dataset_path = './Data/Map-Crime_Incidents-Previous_Three_Months.csv'
SF = pd.read_csv(dataset_path)

pd.set_option('display.max_rows', 10)

print(len(SF))
# 30760

SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))

del SF['IncidntNum']
del SF['Location']

CountCategory = SF['Category'].value_counts()

print(CountCategory)
# LARCENY/THEFT - 8205

CountDistrict = SF['PdDistrict'].value_counts()

print(CountDistrict)
# SOUTHERN - 6185

AugustCrimesCounts = SF[SF['Month'] == 8].value_counts()
print(AugustCrimesCounts)
# 9720

AugustCrimesMask = SF['Month'] == 8
BurglaryCrimesMask = SF['Category'] == 'BURGLARY'
AugustBurglary = np.logical_and(AugustCrimesMask, BurglaryCrimesMask)
AugustBurglaryCount = SF[AugustBurglary].value_counts()

print(AugustBurglaryCount)
# 373

plt.plot(SF['X'], SF['Y'], 'ro')
plt.show()

pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))

SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])

plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()

districts = np.unique(SF['PdDistrict'])

color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)]))

map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start=12)
plotEvery = 50
obs = list(zip(SF['Y'], SF['X'], SF['PdDistrict']))
for el in obs[0:-1:plotEvery]:
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2], radius=10).add_to(map_osm)

map_osm.save("map.html")
new = 2
webbrowser.open("map.html", new=new)
