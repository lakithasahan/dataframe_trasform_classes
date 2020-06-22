from core_classes.lat_and_log_handling import  lat_and_log_handling_class
import pandas as pd
import numpy as np
from opencage.geocoder import OpenCageGeocode
import plotly.express as px

# getting data from the data_files folder
df = pd.read_csv(r'C:\Users\N\Documents\covid_19.csv')

# class testing starts
class_obj = lat_and_log_handling_class(df)
df = class_obj.main()

fig = px.scatter_mapbox(df, lat="lat", lon="l"
                                           "ng", color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()













