"""
Editor de Spyder
Este es un archivo temporal.
"""

#%% Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/home/daniu/Documents/covid-19/corona_stats-master/csse_covid_19_time_series/'
file = 'time_series_19-covid-Confirmed.csv'

df = pd.read_csv(path + file)

df = df.drop(['Province/State','Lat','Long'], axis=1)
df = df.T
df =

new_header = df.iloc[0]
df = df[1:]
df.columns = new_header
df.index = pd.to_datetime(df.index)
df.index.names = ['Date']


matrix = df.values

jj = np.random.rand(56)

df_jj = pd.DataFrame(jj, index=df.index, columns=['jj fit'])


fig = plt.figure(figsize=(4,3))
ax = plt.axes([0.1, 0.1, 0.85, 0.85])
# [left, bottom, width, height]

df['Argentina'].plot(ax=ax)
df_jj['jj fit'].plot(ax=ax)

df['China'].sum(axis=1).plot()
