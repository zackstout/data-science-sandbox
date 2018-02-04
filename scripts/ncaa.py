
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

df = pd.read_csv('csvs/ncaa-predictions.csv')

# Ok this is working: I guess you don't need the .. before /csvs, because python is being executed from the root folder.
print(df.head())
