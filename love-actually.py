
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

df = pd.read_csv('love_actually_adjacencies.csv')

print(list(df))

# all right we handled this with js. can we learn to do it here?
