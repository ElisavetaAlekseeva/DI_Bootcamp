import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# INDEXING
df.iloc[50]
df.iloc[50:60]
df.loc[(df['species'] == 'versicolor') and (df['petal_width'] == 1.4)]

df.groupby(by=['species'])

df.sort_values(['petral_width'], ascending=False).groupby(by=['species']).sum()

df.sort_values(['petral_width'], ascending=False)