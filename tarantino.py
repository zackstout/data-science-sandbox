
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
# curses = 0
# deaths = 0
movies = []
totals = []

curses = []
dead = []

df = pd.read_csv('tarantino.csv')

style.use('ggplot')

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

# print(totals)

# ugh this is disgusting... but it works at least:
for index, row in df.iterrows():
    m = row['movie']
    t = row['type']
    for tot in totals:
        if tot['title'] == m:
            if t == 'word':
                tot['swears'] += 1
            else:
                tot['deaths'] += 1

print(totals)

# why not just do another loop....:
for t in totals:
    curses.append(t['swears'])
    dead.append(t['deaths'])



# prepare for double-bar chart:
num_groups = len(totals);

# still don't understand this double assignment syntax:
fig, ax = plt.subplots()
index = np.arange(num_groups)
bar_width = 0.30
# opacity: 0.66

rects1 = plt.bar(index, curses, bar_width, color='b', label='curses')

rects2 = plt.bar(index + bar_width, dead, bar_width, color='r', label='dead')

plt.xlabel('Movie')
plt.ylabel('Stats')
plt.title("Tarantino: you filthy man")
plt.xticks(index + bar_width, movies)
plt.legend()

plt.tight_layout()
plt.show()


# print(movies)

# This works:
# for t in df['type']:
#     if t == 'word':
#         curses += 1
#     elif t == 'death':
#         deaths += 1
#
# print(curses, deaths)
