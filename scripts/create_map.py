import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

# Load dataset
df = pd.read_csv("data/listings_bali_201804.csv")
# Draw map of Bali
fig, ax = plt.subplots(figsize=(20, 10))
m = Basemap(resolution='f', projection='lcc',
            lon_0=115.1889, lat_0=-8.4095,
            llcrnrlon=114.3531, llcrnrlat=-8.8980,
            urcrnrlon=115.8595, urcrnrlat=-8.0159)
m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
m.drawcoastlines()
for i, row in df.iterrows():
    x, y = m(row.longitude, row.latitude)
    m.plot(x, y, 'o',
           markersize=2, color='#f70000', alpha=.6)
fig.savefig("assets/map.png", bbox_inches='tight', pad_index=0)
