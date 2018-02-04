
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

df = pd.read_csv('csvs/hiphop_lyrics.csv')

print(df.head())
