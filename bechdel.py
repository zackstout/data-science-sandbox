
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

budgets = []
passes = []
grosses = []

df = pd.read_csv('movies.csv')

print(df.head(8))

for index, row in df.iterrows():
    # print(df['movie'])
    budgets.append(row['budget'])
    if row['binary'] == 'PASS':
        passes.append(1)
    else:
        passes.append(0)
    grosses.append(row['intgross'])

# print(budgets[:6])
# print(passes[:4])

plt.plot(budgets, grosses, 'ro')
plt.show()
