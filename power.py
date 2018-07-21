import pandas as pd
import matplotlib.pyplot as plt


df_pwr = pd.read_csv("C:\\mypythonscripts\\Temp-Py\\usage.csv", usecols=['ended_at','value'])

df_pwr['ended_at'] = pd.to_datetime(df_pwr['ended_at'], dayfirst=True)
df_pwr = df_pwr.rename(columns={'ended_at': 'Date(NZST)'})
df_pwr.index = df_pwr['Date(NZST)']

df_pwr = df_pwr.resample('D').sum()

print(df_pwr)
