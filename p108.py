import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv("p108.csv")
graph=ff.create_distplot([df["Avg Rating"].tolist()],["Average"],show_hist=False)
graph.show()