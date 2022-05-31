import pandas as pd
import plotly.figure_factory as pf
import statistics as st
import random

df = pd.read_csv("articles.csv")

data = df["reading_time"].tolist()

mean = st.mean(data)
stdev = st.stdev(data)

print("Mean is " , mean)
print("Stdev is " , stdev)

meanList = []

for i in range(100):
    dataSet=[]
    for j in range(30):
        id = random.choice(data)
        dataSet.append(id)

    meanList.append(st.mean(dataSet))

meanOfSample = st.mean(meanList)
stdevOfSample = st.stdev(meanList)

print("Mean of Sample is " , meanOfSample)
print("Stdev of Sample is " , stdevOfSample)

graph = pf.create_distplot( [meanList] , ["Mean"] , show_hist=False)
graph.show()