
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
curses = 0
deaths = 0
movies = []
totals = [];


df = pd.read_csv('tarantino.csv')

# print(df['type'].head())
# for m in df['movie']:
#     if m not in movies:
#         movies.append(m)

# print(movies)



# We do need index:
for index, row in df.iterrows():
    # print(df['movie'])
    if row['movie'] not in movies:
        movies.append(row['movie'])

for m in movies:
    totals.append({
        'title': m,
        'swears': 0,
        'deaths': 0,
    })

print(totals)

for index, row in df.iterrows():
    m = row['movie']
    t = row['type']



# print(movies)

# This works:
# for t in df['type']:
#     if t == 'word':
#         curses += 1
#     elif t == 'death':
#         deaths += 1
#
# print(curses, deaths)
