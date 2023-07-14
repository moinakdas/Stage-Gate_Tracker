import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
# Read the Excel file into a DataFrame
df = pd.read_excel("C:\\Users\\pbesser\\Downloads\\Stage gates cleaned data.xlsx")

# create data
x = pd.to_datetime(df['Proposed Sub Date '])
y = pd.to_datetime(df['Submittal Date'])
xnum = pd.to_numeric(df['Proposed Sub Date '])
ynum = pd.to_numeric(df['Submittal Date'])

#set starting point for line as Jan 1, 2023
q=[1672531200000000000,max(xnum+ynum)]
# # modify the line attribute of the trace to have a slope of 1 and an intercept of 0

# create figure
scatter_data = go.Scatter(x=x, y=y, mode='markers', marker=dict(color='DarkSlateGrey'))
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=x, y=x, name = "line", marker=dict(color='Red'))
)
fig.add_trace(
    go.Scatter(x=x, y=y, mode='markers', marker=dict(color='DarkSlateGrey'))
)
fig1 = px.scatter(df,x=x,y=y)
fig1 = go.Figure(data=scatter_data)
fig.show()