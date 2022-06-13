'''
사용라이브러리
'''

import numpy as np
from numpy.random import randint
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
from matplotlib import font_manager, rc
import sys
import os


'''
데이터셋 합치기
'''

path = '/2022-06/2022-06-08_2_TRN/Dataset_simul/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')]
df = pd.DataFrame()

for i in file_list_py:
    data = pd.read_csv(path + i)
    df = pd.concat([df, data])

df.columns = ['TIME', 'T_indoor', 'T_HPout', 'T_HPin', 'T_ambi', 'T_ERVea', 'T_ERVsa',
              'RH_indoor', 'E_HP', 'E_FCU', 'E_pump', 'E_ERVea', 'E_ERVsa', 'ERV_flow', 'RH_ambi', 'Radi_ambi']

df = df.iloc[:,1:]
df.index = df.index/5
df = df.reset_index()
df = df.rename(columns={'index':'TIME'})

'''
Time table 생성
'''
pr_12min = pd.period_range(start = '1900-01-01', end = None, periods = len(df), freq = '12T')

df['TIME'] = pr_12min
df['Month'] = df['TIME'].dt.month
df.set_index('TIME', inplace=True)

col1 = df.columns[-1:].to_list()
col2 = df.columns[:-1].to_list()
new_col = col1 + col2
df = df[new_col]

'''
데이터 정규화
'''
df = df[df.ERV_flow != 0]
df['E_HP'] = df['E_HP'].astype('float')
df['ERV_flow'] = df['ERV_flow'].astype('float')

'''
데이터 구간 분할
'''
count, bin_dividers = np.histogram(df['ERV_flow'], bins = 7)
bin_names = ['0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1']
df['ERV_FP'] = pd.cut(x=df['ERV_flow'], bins = bin_dividers, labels = bin_names, include_lowest = True)

'''
데이터 전처리
'''
df['System_COP'] = 1/(abs(df['T_ERVea']-df['T_ERVsa']) * 3.6) * 100
# df['System_COP'] = (abs(df['T_HPout']-df['T_HPin']) * 1500 * 4.186 / 3.6 + abs(df['T_ERVea']-df['T_ERVsa']) * df['ERV_flow'] * 1.2 * 1.01 / 3.6) / ((df['E_HP'] + df['E_ERVea'] + df['E_ERVsa']) / 3.6)
df.T_ambi = np.round(df.T_ambi, decimals = 1)
df.T_indoor = np.round(df.T_indoor, decimals = 1)

'''
냉난방기간 구분하여 데이터 저장
'''
df_1 = df.loc[df.Month == 1]
df_2 = df.loc[df.Month == 2]
df_3 = df.loc[df.Month == 3]
df_4 = df.loc[df.Month == 4]
df_5 = df.loc[df.Month == 5]
df_6 = df.loc[df.Month == 6]
df_7 = df.loc[df.Month == 7]
df_8 = df.loc[df.Month == 8]
df_9 = df.loc[df.Month == 9]
df_10 = df.loc[df.Month == 10]
df_11 = df.loc[df.Month == 11]
df_12 = df.loc[df.Month == 12]

df_heating = pd.concat([df_1, df_2, df_11, df_12])
df_cooling = pd.concat([df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])

'''
냉난방 데이터 세트 마련
'''
df_heating = df_heating.sort_values(['T_ambi', 'System_COP'], ascending = False)
df_cooling = df_cooling.sort_values(['T_ambi', 'System_COP'], ascending = False)

df_heating = df_heating.drop_duplicates(['T_ambi'])
df_cooling = df_cooling.drop_duplicates(['T_ambi'])
df_year = pd.concat([df_heating, df_cooling])

'''
출력
'''
print(df_heating)
print(df_cooling)

'''
데이터 저장
'''
df.to_csv('D:\\AI_python\\2022-06\\2022-06-08_2_TRN\\Dataset_simul\\results_csv\\dataset_erv.csv')
df_year.to_csv('D:\\AI_python\\2022-06\\2022-06-08_2_TRN\\Dataset_simul\\results_csv\\year_dataset_erv.csv')
df_heating.to_csv('D:\\AI_python\\2022-06\\2022-06-08_2_TRN\\Dataset_simul\\results_csv\\heating_dataset_erv.csv')
df_cooling.to_csv('D:\\AI_python\\2022-06\\2022-06-08_2_TRN\\Dataset_simul\\results_csv\\cooling_dataset_erv.csv')