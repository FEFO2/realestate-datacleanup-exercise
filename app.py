import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#SET AND SUBSET
ds = pd.read_csv('assets/real_estate.csv', sep=';')
ds['pps'] = ds['price'] / ds['surface']
popul_filter = ds['level5'].isin(['Fuenlabrada','Leganés','Getafe','Alcorcón'])
sbmadrid = ds[popul_filter]

#SET A DICTIONARY
# df = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
#                    'col2': ['a', 'b', 'c', 'd', 'e']})
# print(df)
# dict_df = df.set_index('col1')['col2'].to_dict()
# print(dict_df)

print(sbmadrid[['latitude','longitude']])

test_lat = 40.28674
test_lon = -3.79351