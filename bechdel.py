
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
# it's smart enough to autofill tflearn ONLY IF i've already referenced it in the code!
import tflearn

import urllib.request, urllib.error

import json
from pandas.plotting import scatter_matrix


style.use('ggplot')

budgets = []
passes = []
grosses = []
passingTitles = []
passingYears = []
failingTitles = []
failingYears = []
s = 0
passesYear = []
failsYear = []
passesAnn = []
failsAnn = []

passingIds = []
failingIds = []

movie_ratings = []

df = pd.read_csv('movies.csv')

# --VISUALIZATIONS--:
# box/whisker -- Wow this is amazing:
# df.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
# plt.show()

# histograms -- Wow this is also nuts:
# df.hist()
# plt.show()

# scatter plot matrix -- WOW --:
# scatter_matrix(df)
# plt.show()



# print(df.head(8))

def checkPasses():
    for index, row in df.iterrows():
        # print(df['movie'])
        budgets.append(int(row['budget']/1000000))
        grosses.append((row['intgross']/1000000))

        if row['binary'] == 'PASS':
            passingIds.append(row['imdb'])
            passes.append(1)
            passingTitles.append(row['title'])
            passingYears.append(row['year'])
            # print(df.iterrows()[index - 1])
        else:
            failingIds.append(row['imdb'])
            passes.append(0)
            failingTitles.append(row['title'])
            failingYears.append(row['year'])

def cleanData():
    for i in range(0, len(df)):
        # print(df.iloc[i]['binary'])
        if df.iloc[i]['year'] == df.iloc[i - 1]['year']:
            s += 1
        else:
            if df.iloc[i]['binary'] == 'PASS':
                passesYear.append(s)
                s = 0
                passesAnn.append(df.iloc[i - 1]['year'])
            else:
                failsYear.append(s)
                s = 0
                failsAnn.append(df.iloc[i - 1]['year'])


# print('passing: ', passingIds)
# print('failing: ', failingTitles)
# print('passes: ', passesYear)
# print('fails: ', failsYear)
# print('passYears: ', passesAnn)
# print('failYears: ', failsAnn)


# Get ratings for each movie:
def getRatings():
    for mov in passingIds:
        link = "http://www.omdbapi.com/?apikey=trilogy&i=%s" % mov
        # info = urllib.request.urlopen(link)
        # print(info)
        data = json.load(urllib.request.urlopen(link))
        # print(data)

        ratings = []

        for r in data["Ratings"]:
            rating = dict()
            # Can't use dot notation to set values:
            rating["source"] = r["Source"]
            rating["value"] = r["Value"]
            ratings.append(rating)
        
        # print(ratings)




# plt.plot(passesAnn, passesYear, 'ro', failsAnn, failsYear, 'bo')
# plt.xlabel('Year')
# plt.ylabel('Number of Movies')

# plt.show()

# print(budgets[:6])
# print(grosses[:4])
#

# plt.plot(budgets, grosses, 'ro')
# plt.show()

# print(passingTitles)

# oooh 'ro' means red circles;
# plt.plot(passingYears, passingTitles, 'ro', failingYears, failingTitles, 'bo')
# plt.show()


# how do we, for each year, sum up how many fails and passes it has, and draw two curves to represent that?




# Hmmm, really unsure why this is giving 'nan':
# input_ = tflearn.input_data(shape=[None])
# linear = tflearn.single_unit(input_)
# regression = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
#                                 metric='R2', learning_rate=0.01)
# m = tflearn.DNN(regression)
# m.fit(budgets[:800], grosses[:800], n_epoch=300, show_metric=True, snapshot_epoch=False)
# #
# print("\nRegression result:")
# print("Y = " + str(m.get_weights(linear.W)) +
#       "*X + " + str(m.get_weights(linear.b)))

# print("\nTest prediction for x = 3.2, 3.3, 3.4:")
# print(m.predict([3.2, 3.3, 3.4]))
