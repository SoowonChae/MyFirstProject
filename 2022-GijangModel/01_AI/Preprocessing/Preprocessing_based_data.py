import pandas as pd
import numpy as np

'''
df100
'''

df100_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_100_1.txt', sep = '\t' ,index_col = None)
df100_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_100_2.txt', sep = '\t', index_col = None)

df100 = pd.concat([df100_1, df100_2], axis = 1, ignore_index=False)
df100 = df100.dropna(axis = 1)
df100.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df100 = df100.drop(['TIME1', 'TIME2'], axis = 'columns')
df100['Q_Source_W'] = abs(df100.P1_F_kg_h * 4.184 * df100.dT_Source_C) / 20
df100['Q_Load_W'] = abs(df100.P2_F_kg_h * 4.184 * df100.dT_Load_C)/ 20
df100['Q_Solar_W'] = abs(df100.P3_F_kg_h * 4.184 * df100.dT_Solar_C) / 20
df100['P1_F_LPM'] = df100.P1_F_kg_h / 60
df100['P2_F_LPM'] = df100.P2_F_kg_h / 60
df100['P3_F_LPM'] = df100.P3_F_kg_h / 60
P1_MAX = df100['P1_F_LPM'].max()
P2_MAX = df100['P2_F_LPM'].max()
P3_MAX = df100['P3_F_LPM'].max()
df100['P1_E_W'] = (1.0642 * pow(df100['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df100['P1_F_LPM']/ P1_MAX + 0.2318) * df100['P1_E_W']
df100['P2_E_W'] = (1.0642 * pow(df100['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df100['P2_F_LPM']/ P2_MAX + 0.2318) * df100['P2_E_W']
df100['P3_E_W'] = (1.0642 * pow(df100['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df100['P3_F_LPM']/ P3_MAX + 0.2318) * df100['P3_E_W']

df100 = df100[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df100 = np.round(df100, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df100), freq = '3T')

df100['TIME'] = pr_3min
df100['Month'] = df100['TIME'].dt.month
df100.set_index('TIME', inplace=True)

col1 = df100.columns[-1:].to_list()
col2 = df100.columns[:-1].to_list()
new_col = col1 + col2
df100 = df100[new_col]

df100 = df100.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV100.csv')

'''
df95
'''

df95_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_95_1.txt', sep = '\t' ,index_col = None)
df95_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_95_2.txt', sep = '\t', index_col = None)

df95 = pd.concat([df95_1, df95_2], axis = 1, ignore_index=False)
df95 = df95.dropna(axis = 1)
df95.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df95 = df95.drop(['TIME1', 'TIME2'], axis = 'columns')
df95['Q_Source_W'] = abs(df95.P1_F_kg_h * 4.184 * df95.dT_Source_C) / 20
df95['Q_Load_W'] = abs(df95.P2_F_kg_h * 4.184 * df95.dT_Load_C) / 20
df95['Q_Solar_W'] = abs(df95.P3_F_kg_h * 4.184 * df95.dT_Solar_C) / 20
df95['P1_F_LPM'] = df95.P1_F_kg_h / 60
df95['P2_F_LPM'] = df95.P2_F_kg_h / 60
df95['P3_F_LPM'] = df95.P3_F_kg_h / 60
df95['P1_E_W'] = (1.0642 * pow(df95['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df95['P1_F_LPM']/ P1_MAX + 0.2318) * df95['P1_E_W']
df95['P2_E_W'] = (1.0642 * pow(df95['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df95['P2_F_LPM']/ P2_MAX + 0.2318) * df95['P2_E_W']
df95['P3_E_W'] = (1.0642 * pow(df95['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df95['P3_F_LPM']/ P3_MAX + 0.2318) * df95['P3_E_W']

df95 = df95[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df95 = np.round(df95, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df95), freq = '3T')

df95['TIME'] = pr_3min
df95['Month'] = df95['TIME'].dt.month
df95.set_index('TIME', inplace=True)

col1 = df95.columns[-1:].to_list()
col2 = df95.columns[:-1].to_list()
new_col = col1 + col2
df95 = df95[new_col]

df95 = df95.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV95.csv')


'''
df90
'''

df90_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_90_1.txt', sep = '\t' ,index_col = None)
df90_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_90_2.txt', sep = '\t', index_col = None)

df90 = pd.concat([df90_1, df90_2], axis = 1, ignore_index=False)
df90 = df90.dropna(axis = 1)
df90.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df90 = df90.drop(['TIME1', 'TIME2'], axis = 'columns')
df90['Q_Source_W'] = abs(df90.P1_F_kg_h * 4.184 * df90.dT_Source_C) / 20
df90['Q_Load_W'] = abs(df90.P2_F_kg_h * 4.184 * df90.dT_Load_C) / 20
df90['Q_Solar_W'] = abs(df90.P3_F_kg_h * 4.184 * df90.dT_Solar_C) / 20
df90['P1_F_LPM'] = df90.P1_F_kg_h / 60
df90['P2_F_LPM'] = df90.P2_F_kg_h / 60
df90['P3_F_LPM'] = df90.P3_F_kg_h / 60
df90['P1_E_W'] = (1.0642 * pow(df90['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df90['P1_F_LPM']/ P1_MAX + 0.2318) * df90['P1_E_W']
df90['P2_E_W'] = (1.0642 * pow(df90['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df90['P2_F_LPM']/ P2_MAX + 0.2318) * df90['P2_E_W']
df90['P3_E_W'] = (1.0642 * pow(df90['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df90['P3_F_LPM']/ P3_MAX + 0.2318) * df90['P3_E_W']

df90 = df90[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df90 = np.round(df90, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df90), freq = '3T')

df90['TIME'] = pr_3min
df90['Month'] = df90['TIME'].dt.month
df90.set_index('TIME', inplace=True)

col1 = df90.columns[-1:].to_list()
col2 = df90.columns[:-1].to_list()
new_col = col1 + col2
df90 = df90[new_col]

df90 = df90.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV90.csv')


'''
df85
'''

df85_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_85_1.txt', sep = '\t' ,index_col = None)
df85_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_85_2.txt', sep = '\t', index_col = None)

df85 = pd.concat([df85_1, df85_2], axis = 1, ignore_index=False)
df85 = df85.dropna(axis = 1)
df85.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df85 = df85.drop(['TIME1', 'TIME2'], axis = 'columns')
df85['Q_Source_W'] = abs(df85.P1_F_kg_h * 4.184 * df85.dT_Source_C) / 20
df85['Q_Load_W'] = abs(df85.P2_F_kg_h * 4.184 * df85.dT_Load_C) / 20
df85['Q_Solar_W'] = abs(df85.P3_F_kg_h * 4.184 * df85.dT_Solar_C) / 20
df85['P1_F_LPM'] = df85.P1_F_kg_h / 60
df85['P2_F_LPM'] = df85.P2_F_kg_h / 60
df85['P3_F_LPM'] = df85.P3_F_kg_h / 60
df85['P1_E_W'] = (1.0642 * pow(df85['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df85['P1_F_LPM']/ P1_MAX + 0.2318) * df85['P1_E_W']
df85['P2_E_W'] = (1.0642 * pow(df85['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df85['P2_F_LPM']/ P2_MAX + 0.2318) * df85['P2_E_W']
df85['P3_E_W'] = (1.0642 * pow(df85['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df85['P3_F_LPM']/ P3_MAX + 0.2318) * df85['P3_E_W']

df85 = df85[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df85 = np.round(df85, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df85), freq = '3T')

df85['TIME'] = pr_3min
df85['Month'] = df85['TIME'].dt.month
df85.set_index('TIME', inplace=True)

col1 = df85.columns[-1:].to_list()
col2 = df85.columns[:-1].to_list()
new_col = col1 + col2
df85 = df85[new_col]

df85 = df85.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV85.csv')

'''
df80
'''

df80_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_80_1.txt', sep = '\t' ,index_col = None)
df80_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_80_2.txt', sep = '\t', index_col = None)

df80 = pd.concat([df80_1, df80_2], axis = 1, ignore_index=False)
df80 = df80.dropna(axis = 1)
df80.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df80 = df80.drop(['TIME1', 'TIME2'], axis = 'columns')
df80['Q_Source_W'] = abs(df80.P1_F_kg_h * 4.184 * df80.dT_Source_C) / 20
df80['Q_Load_W'] = abs(df80.P2_F_kg_h * 4.184 * df80.dT_Load_C) / 20
df80['Q_Solar_W'] = abs(df80.P3_F_kg_h * 4.184 * df80.dT_Solar_C) / 20
df80['P1_F_LPM'] = df80.P1_F_kg_h / 60
df80['P2_F_LPM'] = df80.P2_F_kg_h / 60
df80['P3_F_LPM'] = df80.P3_F_kg_h / 60
df80['P1_E_W'] = (1.0642 * pow(df80['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df80['P1_F_LPM']/ P1_MAX + 0.2318) * df80['P1_E_W']
df80['P2_E_W'] = (1.0642 * pow(df80['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df80['P2_F_LPM']/ P2_MAX + 0.2318) * df80['P2_E_W']
df80['P3_E_W'] = (1.0642 * pow(df80['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df80['P3_F_LPM']/ P3_MAX + 0.2318) * df80['P3_E_W']

df80 = df80[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df80 = np.round(df80, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df80), freq = '3T')

df80['TIME'] = pr_3min
df80['Month'] = df80['TIME'].dt.month
df80.set_index('TIME', inplace=True)

col1 = df80.columns[-1:].to_list()
col2 = df80.columns[:-1].to_list()
new_col = col1 + col2
df80 = df80[new_col]

df80 = df80.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV80.csv')

'''
df75
'''

df75_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_75_1.txt', sep = '\t' ,index_col = None)
df75_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_75_2.txt', sep = '\t', index_col = None)

df75 = pd.concat([df75_1, df75_2], axis = 1, ignore_index=False)
df75 = df75.dropna(axis = 1)
df75.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df75 = df75.drop(['TIME1', 'TIME2'], axis = 'columns')
df75['Q_Source_W'] = abs(df75.P1_F_kg_h * 4.184 * df75.dT_Source_C) / 20
df75['Q_Load_W'] = abs(df75.P2_F_kg_h * 4.184 * df75.dT_Load_C) / 20
df75['Q_Solar_W'] = abs(df75.P3_F_kg_h * 4.184 * df75.dT_Solar_C) / 20
df75['P1_F_LPM'] = df75.P1_F_kg_h / 60
df75['P2_F_LPM'] = df75.P2_F_kg_h / 60
df75['P3_F_LPM'] = df75.P3_F_kg_h / 60
df75['P1_E_W'] = (1.0642 * pow(df75['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df75['P1_F_LPM']/ P1_MAX + 0.2318) * df75['P1_E_W']
df75['P2_E_W'] = (1.0642 * pow(df75['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df75['P2_F_LPM']/ P2_MAX + 0.2318) * df75['P2_E_W']
df75['P3_E_W'] = (1.0642 * pow(df75['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df75['P3_F_LPM']/ P3_MAX + 0.2318) * df75['P3_E_W']

df75 = df75[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df75 = np.round(df75, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df75), freq = '3T')

df75['TIME'] = pr_3min
df75['Month'] = df75['TIME'].dt.month
df75.set_index('TIME', inplace=True)

col1 = df75.columns[-1:].to_list()
col2 = df75.columns[:-1].to_list()
new_col = col1 + col2
df75 = df75[new_col]

df75 = df75.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV75.csv')


'''
df70
'''

df70_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_70_1.txt', sep = '\t' ,index_col = None)
df70_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_70_2.txt', sep = '\t', index_col = None)

df70 = pd.concat([df70_1, df70_2], axis = 1, ignore_index=False)
df70 = df70.dropna(axis = 1)
df70.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df70 = df70.drop(['TIME1', 'TIME2'], axis = 'columns')
df70['Q_Source_W'] = abs(df70.P1_F_kg_h * 4.184 * df70.dT_Source_C) / 20
df70['Q_Load_W'] = abs(df70.P2_F_kg_h * 4.184 * df70.dT_Load_C) / 20
df70['Q_Solar_W'] = abs(df70.P3_F_kg_h * 4.184 * df70.dT_Solar_C) / 20
df70['P1_F_LPM'] = df70.P1_F_kg_h / 60
df70['P2_F_LPM'] = df70.P2_F_kg_h / 60
df70['P3_F_LPM'] = df70.P3_F_kg_h / 60
df70['P1_E_W'] = (1.0642 * pow(df70['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df70['P1_F_LPM']/ P1_MAX + 0.2318) * df70['P1_E_W']
df70['P2_E_W'] = (1.0642 * pow(df70['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df70['P2_F_LPM']/ P2_MAX + 0.2318) * df70['P2_E_W']
df70['P3_E_W'] = (1.0642 * pow(df70['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df70['P3_F_LPM']/ P3_MAX + 0.2318) * df70['P3_E_W']

df70 = df70[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df70 = np.round(df70, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df70), freq = '3T')

df70['TIME'] = pr_3min
df70['Month'] = df70['TIME'].dt.month
df70.set_index('TIME', inplace=True)

col1 = df70.columns[-1:].to_list()
col2 = df70.columns[:-1].to_list()
new_col = col1 + col2
df70 = df70[new_col]

df70 = df70.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV70.csv')

'''
df65
'''

df65_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_65_1.txt', sep = '\t' ,index_col = None)
df65_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_65_2.txt', sep = '\t', index_col = None)

df65 = pd.concat([df65_1, df65_2], axis = 1, ignore_index=False)
df65 = df65.dropna(axis = 1)
df65.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df65 = df65.drop(['TIME1', 'TIME2'], axis = 'columns')
df65['Q_Source_W'] = abs(df65.P1_F_kg_h * 4.184 * df65.dT_Source_C) / 20
df65['Q_Load_W'] = abs(df65.P2_F_kg_h * 4.184 * df65.dT_Load_C) / 20
df65['Q_Solar_W'] = abs(df65.P3_F_kg_h * 4.184 * df65.dT_Solar_C) / 20
df65['P1_F_LPM'] = df65.P1_F_kg_h / 60
df65['P2_F_LPM'] = df65.P2_F_kg_h / 60
df65['P3_F_LPM'] = df65.P3_F_kg_h / 60
df65['P1_E_W'] = (1.0642 * pow(df65['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df65['P1_F_LPM']/ P1_MAX + 0.2318) * df65['P1_E_W']
df65['P2_E_W'] = (1.0642 * pow(df65['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df65['P2_F_LPM']/ P2_MAX + 0.2318) * df65['P2_E_W']
df65['P3_E_W'] = (1.0642 * pow(df65['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df65['P3_F_LPM']/ P3_MAX + 0.2318) * df65['P3_E_W']

df65 = df65[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df65 = np.round(df65, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df65), freq = '3T')

df65['TIME'] = pr_3min
df65['Month'] = df65['TIME'].dt.month
df65.set_index('TIME', inplace=True)

col1 = df65.columns[-1:].to_list()
col2 = df65.columns[:-1].to_list()
new_col = col1 + col2
df65 = df65[new_col]

df65 = df65.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV65.csv')


'''
df60
'''

df60_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_60_1.txt', sep = '\t' ,index_col = None)
df60_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_60_2.txt', sep = '\t', index_col = None)

df60 = pd.concat([df60_1, df60_2], axis = 1, ignore_index=False)
df60 = df60.dropna(axis = 1)
df60.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df60 = df60.drop(['TIME1', 'TIME2'], axis = 'columns')
df60['Q_Source_W'] = abs(df60.P1_F_kg_h * 4.184 * df60.dT_Source_C) / 20
df60['Q_Load_W'] = abs(df60.P2_F_kg_h * 4.184 * df60.dT_Load_C) / 20
df60['Q_Solar_W'] = abs(df60.P3_F_kg_h * 4.184 * df60.dT_Solar_C) / 20
df60['P1_F_LPM'] = df60.P1_F_kg_h / 60
df60['P2_F_LPM'] = df60.P2_F_kg_h / 60
df60['P3_F_LPM'] = df60.P3_F_kg_h / 60
df60['P1_E_W'] = (1.0642 * pow(df60['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df60['P1_F_LPM']/ P1_MAX + 0.2318) * df60['P1_E_W']
df60['P2_E_W'] = (1.0642 * pow(df60['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df60['P2_F_LPM']/ P2_MAX + 0.2318) * df60['P2_E_W']
df60['P3_E_W'] = (1.0642 * pow(df60['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df60['P3_F_LPM']/ P3_MAX + 0.2318) * df60['P3_E_W']

df60 = df60[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df60 = np.round(df60, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df60), freq = '3T')

df60['TIME'] = pr_3min
df60['Month'] = df60['TIME'].dt.month
df60.set_index('TIME', inplace=True)

col1 = df60.columns[-1:].to_list()
col2 = df60.columns[:-1].to_list()
new_col = col1 + col2
df60 = df60[new_col]

df60 = df60.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV60.csv')

'''
df55
'''

df55_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_55_1.txt', sep = '\t' ,index_col = None)
df55_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_55_2.txt', sep = '\t', index_col = None)

df55 = pd.concat([df55_1, df55_2], axis = 1, ignore_index=False)
df55 = df55.dropna(axis = 1)
df55.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df55 = df55.drop(['TIME1', 'TIME2'], axis = 'columns')
df55['Q_Source_W'] = abs(df55.P1_F_kg_h * 4.184 * df55.dT_Source_C) / 20
df55['Q_Load_W'] = abs(df55.P2_F_kg_h * 4.184 * df55.dT_Load_C) / 20
df55['Q_Solar_W'] = abs(df55.P3_F_kg_h * 4.184 * df55.dT_Solar_C) / 20
df55['P1_F_LPM'] = df55.P1_F_kg_h / 60
df55['P2_F_LPM'] = df55.P2_F_kg_h / 60
df55['P3_F_LPM'] = df55.P3_F_kg_h / 60
df55['P1_E_W'] = (1.0642 * pow(df55['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df55['P1_F_LPM']/ P1_MAX + 0.2318) * df55['P1_E_W']
df55['P2_E_W'] = (1.0642 * pow(df55['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df55['P2_F_LPM']/ P2_MAX + 0.2318) * df55['P2_E_W']
df55['P3_E_W'] = (1.0642 * pow(df55['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df55['P3_F_LPM']/ P3_MAX + 0.2318) * df55['P3_E_W']

df55 = df55[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df55 = np.round(df55, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df55), freq = '3T')

df55['TIME'] = pr_3min
df55['Month'] = df55['TIME'].dt.month
df55.set_index('TIME', inplace=True)

col1 = df55.columns[-1:].to_list()
col2 = df55.columns[:-1].to_list()
new_col = col1 + col2
df55 = df55[new_col]

df55 = df55.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV55.csv')

'''
df50
'''

df50_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_50_1.txt', sep = '\t' ,index_col = None)
df50_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_50_2.txt', sep = '\t', index_col = None)

df50 = pd.concat([df50_1, df50_2], axis = 1, ignore_index=False)
df50 = df50.dropna(axis = 1)
df50.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df50 = df50.drop(['TIME1', 'TIME2'], axis = 'columns')
df50['Q_Source_W'] = abs(df50.P1_F_kg_h * 4.184 * df50.dT_Source_C) / 20
df50['Q_Load_W'] = abs(df50.P2_F_kg_h * 4.184 * df50.dT_Load_C) / 20
df50['Q_Solar_W'] = abs(df50.P3_F_kg_h * 4.184 * df50.dT_Solar_C) / 20
df50['P1_F_LPM'] = df50.P1_F_kg_h / 60
df50['P2_F_LPM'] = df50.P2_F_kg_h / 60
df50['P3_F_LPM'] = df50.P3_F_kg_h / 60
df50['P1_E_W'] = (1.0642 * pow(df50['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df50['P1_F_LPM']/ P1_MAX + 0.2318) * df50['P1_E_W']
df50['P2_E_W'] = (1.0642 * pow(df50['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df50['P2_F_LPM']/ P2_MAX + 0.2318) * df50['P2_E_W']
df50['P3_E_W'] = (1.0642 * pow(df50['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df50['P3_F_LPM']/ P3_MAX + 0.2318) * df50['P3_E_W']

df50 = df50[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df50 = np.round(df50, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df50), freq = '3T')

df50['TIME'] = pr_3min
df50['Month'] = df50['TIME'].dt.month
df50.set_index('TIME', inplace=True)

col1 = df50.columns[-1:].to_list()
col2 = df50.columns[:-1].to_list()
new_col = col1 + col2
df50 = df50[new_col]

df50 = df50.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV50.csv')

'''
df45
'''

df45_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_45_1.txt', sep = '\t' ,index_col = None)
df45_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_45_2.txt', sep = '\t', index_col = None)

df45 = pd.concat([df45_1, df45_2], axis = 1, ignore_index=False)
df45 = df45.dropna(axis = 1)
df45.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df45 = df45.drop(['TIME1', 'TIME2'], axis = 'columns')
df45['Q_Source_W'] = abs(df45.P1_F_kg_h * 4.184 * df45.dT_Source_C) / 20
df45['Q_Load_W'] = abs(df45.P2_F_kg_h * 4.184 * df45.dT_Load_C) / 20
df45['Q_Solar_W'] = abs(df45.P3_F_kg_h * 4.184 * df45.dT_Solar_C) / 20
df45['P1_F_LPM'] = df45.P1_F_kg_h / 60
df45['P2_F_LPM'] = df45.P2_F_kg_h / 60
df45['P3_F_LPM'] = df45.P3_F_kg_h / 60
df45['P1_E_W'] = (1.0642 * pow(df45['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df45['P1_F_LPM']/ P1_MAX + 0.2318) * df45['P1_E_W']
df45['P2_E_W'] = (1.0642 * pow(df45['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df45['P2_F_LPM']/ P2_MAX + 0.2318) * df45['P2_E_W']
df45['P3_E_W'] = (1.0642 * pow(df45['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df45['P3_F_LPM']/ P3_MAX + 0.2318) * df45['P3_E_W']

df45 = df45[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df45 = np.round(df45, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df45), freq = '3T')

df45['TIME'] = pr_3min
df45['Month'] = df45['TIME'].dt.month
df45.set_index('TIME', inplace=True)

col1 = df45.columns[-1:].to_list()
col2 = df45.columns[:-1].to_list()
new_col = col1 + col2
df45 = df45[new_col]

df45 = df45.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV45.csv')

'''
df40
'''

df40_1 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_40_1.txt', sep = '\t' ,index_col = None)
df40_2 = pd.read_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\1_data_txt\\CV_40_2.txt', sep = '\t', index_col = None)

df40 = pd.concat([df40_1, df40_2], axis = 1, ignore_index=False)
df40 = df40.dropna(axis = 1)
df40.columns = ['TIME1', 'T_indoor_C', 'T_ambi_C', 'RH_', 'Radi_W_m2', 'PV_gen_W', 'HP_E_W', 'P1_E_W', 'P2_E_W', 'P3_E_W', 'FCU_E_W', 'T_HPout_C',
                 'T_HPin_C', 'T_ST1_C', 'T_ST2_C', 'HP_F_kg_h', 'P1_F_kg_h', 'P2_F_kg_h', 'P3_F_kg_h', 'PVT_AbRadi_kJ_hm2', 'PVT_HeatLoss_kJ_h',
                 'TIME2', 'T_FCUout_C', 'T_FCUin_C', 'PVT_Q_kJ_h', 'T_PVTout_C', 'dT_Solar_C', 'dT_Source_C', 'dT_Load_C', 'T_PVTin_C']

df40 = df40.drop(['TIME1', 'TIME2'], axis = 'columns')
df40['Q_Source_W'] = abs(df40.P1_F_kg_h * 4.184 * df40.dT_Source_C) / 20
df40['Q_Load_W'] = abs(df40.P2_F_kg_h * 4.184 * df40.dT_Load_C) / 20
df40['Q_Solar_W'] = abs(df40.P3_F_kg_h * 4.184 * df40.dT_Solar_C) / 20
df40['P1_F_LPM'] = df40.P1_F_kg_h / 60
df40['P2_F_LPM'] = df40.P2_F_kg_h / 60
df40['P3_F_LPM'] = df40.P3_F_kg_h / 60
df40['P1_E_W'] = (1.0642 * pow(df40['P1_F_LPM']/ P1_MAX, 2) - 0.296 * df40['P1_F_LPM']/ P1_MAX + 0.2318) * df40['P1_E_W']
df40['P2_E_W'] = (1.0642 * pow(df40['P2_F_LPM']/ P2_MAX, 2) - 0.296 * df40['P2_F_LPM']/ P2_MAX + 0.2318) * df40['P2_E_W']
df40['P3_E_W'] = (1.0642 * pow(df40['P3_F_LPM']/ P3_MAX, 2) - 0.296 * df40['P3_F_LPM']/ P3_MAX + 0.2318) * df40['P3_E_W']

df40 = df40[['T_indoor_C', 'T_ambi_C', 'T_ST2_C', 'T_ST1_C', 'dT_Source_C', 'dT_Load_C', 'dT_Solar_C', 'Q_Source_W', 'Q_Load_W', 'Q_Solar_W',
               'P1_E_W', 'P2_E_W', 'P3_E_W', 'HP_E_W', 'Radi_W_m2', 'P1_F_LPM', 'P2_F_LPM', 'P3_F_LPM', 'T_HPout_C', 'T_HPin_C', 'T_FCUout_C', 'T_FCUin_C',
               'T_PVTout_C', 'T_PVTin_C']]

df40 = np.round(df40, 2)

'''
Time table 생성
'''
pr_3min = pd.period_range(start = '1900-01-01', end = None, periods = len(df40), freq = '3T')

df40['TIME'] = pr_3min
df40['Month'] = df40['TIME'].dt.month
df40.set_index('TIME', inplace=True)

col1 = df40.columns[-1:].to_list()
col2 = df40.columns[:-1].to_list()
new_col = col1 + col2
df40 = df40[new_col]

df40 = df40.to_csv(r'D:\\AI_python\\2022-GijangModel\\01_AI\\7.Report\\BS_model\\3_data_csv\\CV40.csv')
