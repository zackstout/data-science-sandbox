
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

df = pd.read_csv('comma-survey-data.csv')

caresAboutGrammar = []
eds = []
gens = []
color = ''

for index, row in df.iterrows():
    cares = row['In your opinion, how important or unimportant is proper use of grammar?']
    gender = row['Gender']
    ed = row['Education']
    # if index < 8:
    #     print(row)
    # caresAboutGrammar.append(row['In your opinion, how important or unimportant is proper use of grammar?'])

    if (cares == 'Very important'):
        caresAboutGrammar.append(3)
    elif (cares == 'Somewhat important'):
        caresAboutGrammar.append(2)
    elif (cares == 'Neither important nor unimportant (neutral)'):
        caresAboutGrammar.append(1)
    # We could also just ignore nan values. Oh no we can't, arrays must be same length:
    else:
        caresAboutGrammar.append(0)

    # print(ed)
    # print(gender)

    if (ed == 'Graduate degree'):
        eds.append(3)
    elif (ed == 'Bachelor degree'):
        eds.append(2)
    elif (ed == 'Some college or Associate degree'):
        eds.append(1)
    elif (ed == 'High school degree'):
        eds.append(0)
    else:
        eds.append(-1)


    if (gender == 'Male'):
        gens.append(0)
    elif (gender == 'Female'):
        gens.append(1)
    else:
        gens.append(-1)


# This isn't working because dots don't represent the amount of each at that point.
plt.scatter(eds, caresAboutGrammar, c=gens, alpha=0.5)
plt.show()

# print(list(df))

# Let's do a features/values regression. Values can be male vs female. Features can be cares about debate, etc etc

# print(caresAboutGrammar)
# print(eds)
# print(gens)
