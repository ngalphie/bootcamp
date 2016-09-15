#Lesson 32: Practice with Pandas
import numpy as np
import pandas as pd

#Practice 1a
df_strong_impact_time = df.loc[np.absolute(df['adhesive strength (Pa)'])>2000, ['impact time (ms)']]

#Practice 1b
df_all_force_II = df.loc[df['ID'] == 'II', ['ID', 'impact force (mN)', 'adhesive force (mN)']]

#Practice 1c
df_ad_ft_juv = df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['ID', 'adhesive force (mN)', 'time frog pulls on target (ms)']]

#Practice 2-1
df_I_if = np.mean(df.loc[df['ID']=='I', ['impact force (mN)']])
df_II_if = np.mean(df.loc[df['ID']=='II', ['impact force (mN)']])
df_III_if = np.mean(df.loc[df['ID']=='III', ['impact force (mN)']])
df_IV_if = np.mean(df.loc[df['ID']=='IV', ['impact force (mN)']])
