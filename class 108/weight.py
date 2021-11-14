import plotly_express as px
import pandas as pd
import plotly.figure_factory as pff
import csv
df=pd.read_csv("data.csv")
weight=df["Weight(Pounds)"].tolist()
figure=pff.create_distplot([weight],["weight"],show_hist=False)
figure.show()