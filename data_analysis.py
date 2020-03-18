# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#%% Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
my_dpi=72
#%% Read csv (Daniu style)
path = 'csse_covid_19_data/csse_covid_19_time_series/'
file = 'time_series_19-covid-Confirmed.csv'
Df = pd.read_csv(path+file)
Df = Df.drop(['Province/State','Lat','Long'],axis=1)
Df = Df.T
Df.columns = Df.iloc[0]
Df = Df[1:]

#%% Making some plots
data = pd.read_csv("time_series_19-covid-Confirmed.csv")
data_hed = list(data.columns.values)

data_arg = data.loc[data['Country/Region']=='Argentina']
data_arg = data_arg.to_numpy().tolist()
data_chi = data.loc[data['Country/Region']=='Chile']
data_chi = data_chi.to_numpy().tolist()
data_bra = data.loc[data['Country/Region']=='Brazil']
data_bra = data_bra.to_numpy().tolist()
data_ecu = data.loc[data['Country/Region']=='Ecuador']
data_ecu = data_ecu.to_numpy().tolist()
data_ita = data.loc[data['Country/Region']=='Italy']
data_ita = data_ita.to_numpy().tolist()
data_hun = data.loc[data['Country/Region']=='Hungary']
data_hun = data_hun.to_numpy().tolist()
#%%
fig = plt.figure(1,figsize=(1200/my_dpi, 600/my_dpi), dpi=my_dpi)
ax  = fig.add_subplot(111)
ax.plot(data_arg[0][5:],'-o',label='Argentina')
ax.plot(data_chi[0][5:],'-o',label='Chile')
ax.plot(data_bra[0][5:],'-o',label='Brasil')
ax.plot(data_ecu[0][5:],'-o',label='Ecuador')
ax.set_xlabel(r'Dias', fontsize=18)
ax.set_ylabel(r'infectados', fontsize=18)
ax.tick_params(labelsize=14)
ax.legend(loc='best',fontsize=20)
ax.grid(linestyle='--')
plt.tight_layout()

fig = plt.figure(2,figsize=(1200/my_dpi, 600/my_dpi), dpi=my_dpi)
ax  = fig.add_subplot(111)
ax.plot(np.diff(data_arg[0][5:]),label='Argentina',linewidth=2)
ax.plot(np.diff(data_chi[0][5:]),label='Chile',linewidth=2)
ax.set_xlabel(r'Dias', fontsize=18)
ax.set_ylabel(r'Nuevos infectados', fontsize=18)
ax.tick_params(labelsize=14)
ax.legend(loc='best',fontsize=20)
ax.grid(linestyle='--')
plt.tight_layout()

#%%
fig = plt.figure(11,figsize=(1200/my_dpi, 600/my_dpi), dpi=my_dpi)
ax  = fig.add_subplot(111)
ax.plot(data_arg[0][5:],'-o',label='Argentina')
ax.set_xlabel(r'Dias', fontsize=18)
ax.set_ylabel(r'infectados', fontsize=18)
ax.tick_params(labelsize=14)
ax.legend(loc='best',fontsize=20)
ax.grid(linestyle='--')
plt.tight_layout()

fig = plt.figure(22,figsize=(1200/my_dpi, 600/my_dpi), dpi=my_dpi)
ax  = fig.add_subplot(111)
ax.plot(np.arange(54),np.diff(data_arg[0][5:]),label='Argentina',linewidth=2)
ax.set_xlabel(r'Dias', fontsize=18)
ax.set_ylabel(r'Nuevos infectados', fontsize=18)
ax.tick_params(labelsize=14)
ax.legend(loc='best',fontsize=20)
ax.grid(linestyle='--')
plt.tight_layout()

#%%
fig = plt.figure(44,figsize=(1200/my_dpi, 600/my_dpi), dpi=my_dpi)
ax  = fig.add_subplot(111)
ax.plot(data_ita[0][5:],'-o',label='Italia',linewidth=2)
ax.set_xlabel(r'Dias', fontsize=18)
ax.set_ylabel(r'infectados', fontsize=18)
ax.tick_params(labelsize=14)
ax.legend(loc='best',fontsize=20)
ax.grid(linestyle='--')

ax1 = ax.twinx()  # instantiate a second axes that shares the same x-axis
ax1.set_ylabel('New infected', color='C1')  # we already handled the x-label with ax1
ax1.plot(np.diff(data_ita[0][5:]),'-o',color='C1',label='Italia',linewidth=2)
ax1.tick_params(axis='y', labelcolor='C1')

plt.tight_layout()