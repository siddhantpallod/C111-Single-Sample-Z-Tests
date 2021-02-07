import csv
import pandas as pd
import statistics
import plotly.figure_factory as pf
import random
import plotly.graph_objects as pg

def randomSetOfMeans(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    
    mean = statistics.mean(dataSet)
    return mean

df = pd.read_csv('studentMarks.csv')

data = df['Math_score'].tolist()

mean = statistics.mean(data)
print("Mean is", mean)
std = statistics.stdev(data)
print("Std is ", std)

meanList = []

for i in range(0,1000):
    setOfMeans = randomSetOfMeans(100)
    meanList.append(setOfMeans) 

firstStdStart, firstStdEnd = mean - std, mean + std
secondStdStart, secondStdEnd =  mean - 2 * std,  mean + 2 * std
thirdStdStart, thirdStdEnd = mean - 3 * std, mean + 3 * std
print(firstStdStart, firstStdEnd)
print(secondStdStart, secondStdEnd)
print(thirdStdStart, thirdStdEnd)



# fig = pf.create_distplot([meanList], ['Student Marks'], show_hist = False)
# fig.add_trace(pg.Scatter(x = [mean, mean], y = [0,0.15], mode = 'lines', name = 'Mean'))
# fig.add_trace(pg.Scatter( x = [firstStdStart, firstStdStart], y = [0,0.15], mode = 'lines', name = 'Std 1 Start'))
# fig.add_trace(pg.Scatter( x = [firstStdEnd, firstStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 1 End'))
# fig.add_trace(pg.Scatter( x = [secondStdStart, secondStdStart], y = [0,0.15], mode = 'lines', name = 'Std 2 Start'))
# fig.add_trace(pg.Scatter( x = [secondStdEnd, secondStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 2 End'))
# fig.add_trace(pg.Scatter( x = [thirdStdStart, thirdStdStart], y = [0,0.15], mode = 'lines', name = 'Std 3 Start'))
# fig.add_trace(pg.Scatter( x = [thirdStdEnd, thirdStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 3 End'))
# fig.show()

# df1 = pd.read_csv('data1.csv')
# data1 = df1['Math_score'].tolist()

# mean1 = statistics.mean(data1)
# print("Mean 1 is", mean1)

# fig1 = pf.create_distplot([meanList], ['Student Marks'], show_hist = False)
# fig1.add_trace(pg.Scatter(x = [mean, mean], y = [0,0.15], mode = 'lines', name = 'Mean'))
# fig1.add_trace(pg.Scatter(x = [mean1, mean1], y = [0,0.15], mode = 'lines', name = 'Mean of students who got tablets'))
# fig1.add_trace(pg.Scatter( x = [firstStdEnd, firstStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 1 End'))
# fig1.show()

# df2 = pd.read_csv('data1.csv')
# data2 = df2['Math_score'].tolist()

# mean2 = statistics.mean(data2)
# print("Mean 2 is", mean2)

# fig2 = pf.create_distplot([meanList], ['Student Marks'], show_hist = False)
# fig2.add_trace(pg.Scatter(x = [mean, mean], y = [0,0.15], mode = 'lines', name = 'Mean'))
# fig2.add_trace(pg.Scatter(x = [mean2, mean2], y = [0,0.15], mode = 'lines', name = 'Mean of students who got extra study material'))
# fig2.add_trace(pg.Scatter( x = [firstStdEnd, firstStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 1 End'))
# fig2.add_trace(pg.Scatter( x = [secondStdEnd, secondStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 2 End'))
# fig2.show()

df3 = pd.read_csv('data1.csv')
data3 = df3['Math_score'].tolist()

mean3 = statistics.mean(data3)
print("Mean 3 is", mean3)

fig3 = pf.create_distplot([meanList], ['Student Marks'], show_hist = False)
fig3.add_trace(pg.Scatter(x = [mean, mean], y = [0,0.15], mode = 'lines', name = 'Mean'))
fig3.add_trace(pg.Scatter(x = [mean3, mean3], y = [0,0.15], mode = 'lines', name = 'Mean of students who got fun sheets'))
fig3.add_trace(pg.Scatter( x = [secondStdEnd, secondStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 2 End'))
fig3.add_trace(pg.Scatter(x = [thirdStdEnd, thirdStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 3 End'))
fig3.show()