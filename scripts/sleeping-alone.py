
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
# from os import path
style.use('ggplot')

# with open('csvs/sleeping-alone-data.csv', 'rb') as f:
#   contents = f.read()
#   df = pd.read_csv(contents)
#   print(contents[:2000])

with open('csvs/sleeping-alone-data.csv', encoding="latin-1") as datafile:
    # df = pd.read_csv('csvs/sleeping-alone-data.csv')
    print(datafile)


# print(df.head())
