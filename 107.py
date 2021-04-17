import csv
import pandas as pd
import plotly_express as px
df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"]["student_id"].mean())
fig = px.scatter(df,x ="student_id",y ="level",color="attempt",size_max=60)
fig.show()