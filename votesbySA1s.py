import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webbrowser

# Read in the shapefile
import os
path =  os.path.dirname(os.path.realpath(__file__))




sa1s = gpd.read_file(f'{path}/data/datasa1/2022-federal-election-votes-sa1.shp')

output = sa1s.explore(column="DivisionNm", cmap="tab20")
outfile = f'{path}/data/datasa1/output.html'
output.save(outfile)

webbrowser.open(outfile)