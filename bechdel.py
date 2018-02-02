
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
# it's smart enough to autofill tflearn ONLY IF i've already referenced it in the code!
import tflearn

style.use('ggplot')

budgets = []
passes = []
grosses = []

df = pd.read_csv('movies.csv')

# print(df.head(8))

for index, row in df.iterrows():
    # print(df['movie'])
    budgets.append(int(row['budget']))
    if row['binary'] == 'PASS':
        passes.append(1)
    else:
        passes.append(0)
    grosses.append((row['intgross']))

print(budgets[:6])
print(grosses[:4])
#

plt.plot(budgets, grosses, 'ro')
plt.show()

# input_ = tflearn.input_data(shape=[None])
# linear = tflearn.single_unit(input_)
# regression = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
#                                 metric='R2', learning_rate=0.01)
# m = tflearn.DNN(regression)
# m.fit(budgets, grosses, n_epoch=1000, show_metric=True, snapshot_epoch=False)
#
# print("\nRegression result:")
# print("Y = " + str(m.get_weights(linear.W)) +
#       "*X + " + str(m.get_weights(linear.b)))

print("\nTest prediction for x = 3.2, 3.3, 3.4:")
# print(m.predict([3.2, 3.3, 3.4]))
