import geopandas as gpd
import webbrowser

# Read in the shapefile
import os
# path =  os.path.dirname(os.path.realpath(__file__))
path = os.getcwd()
sa1s = gpd.read_file(f'{path}/datasa1/2022-federal-election-votes-sa1.shp')

output = sa1s.explore(column="DivisionNm", cmap="tab20")
outfile = f'{path}/docs/index.html'
output.save(outfile)

webbrowser.open(outfile)