import subprocess, os, sys

import folium
import pandas as pd

# Get data files
zip_geo = 'ca-zip.geojson'
data_file = 'example-data.csv'
zip_data = pd.read_csv(data_file, dtype={'zipcode': object})

# Create map
m = folium.Map(
    location=[37.7799, -121.9780],
    tiles='CartoDB Positron',
    zoom_start=8)

# Plot choropleth on map
m.choropleth(
    geo_data=zip_geo,
    name='choropleth',
    data=zip_data,
    columns=['zipcode', 'number'],
    key_on='feature.properties.GEOID10',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number'
)

# Write the map to a file and open it
filepath = 'out.html'
m.save(filepath)
if sys.platform.startswith('darwin'):  # Mac OS X
    subprocess.call(('open', filepath))
elif os.name == 'nt':  # Windows
    os.startfile(filepath)
