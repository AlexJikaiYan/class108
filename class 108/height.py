import plotly_express as px
import pandas as pd
import plotly.figure_factory as pff
import csv
df= pd.read_csv("data.csv")
height=df["Height(Inches)"].tolist()
figure=pff.create_distplot([height],["height"],show_hist=False)
figure.show()