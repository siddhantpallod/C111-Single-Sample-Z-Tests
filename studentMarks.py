import csv
import pandas as pd
import statistics
import plotly.figure_factory as pf
import random
import plotly.graph_objects as pg

df = pd.read_csv('studentMarks.csv')

data = df['Math_score'].tolist()

mean = statistics.mean(data)
print("Mean is", mean)
std = statistics.stdev(data)
print("Std is ", std)

def randomSetOfMeans(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    
    mean = statistics.mean(dataSet)
    return mean

meanList = []

for i in range(0,1000):
    setOfMeans = randomSetOfMeans(100)
    meanList.append(setOfMeans) 

mean1 = statistics.mean(meanList)
print("Sampling Distribution Mean Is", mean1)

std1 = statistics.stdev(meanList)
print("Sampling Std is" , std1)


# fig = pf.create_distplot([meanList],['Student Marks'], show_hist = False)
# fig.add_trace(pg.Scatter(x = [mean1, mean1], y = [0,0.20], mode = 'lines', name = 'Mean'))
# fig.show()