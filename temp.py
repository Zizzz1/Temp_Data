import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 10)

## Temp df:
df = pd.read_csv('C:\\mypythonscripts\\Temp-Py\\temp.csv', skiprows=2,
                 index_col='Date(NZST)', usecols=['Date(NZST)','Tmin(C)', 'Tmax(C)'],
                 parse_dates=['Date(NZST)'])


df_pwr = pd.read_csv("C:\\mypythonscripts\\Temp-Py\\usage.csv", usecols=['ended_at','value'])

df_pwr['ended_at'] = pd.to_datetime(df_pwr['ended_at'], dayfirst=True)
df_pwr = df_pwr.rename(columns={'ended_at': 'Date(NZST)'})
df_pwr.index = df_pwr['Date(NZST)']
df_pwr = df_pwr.resample('D').sum()


df = pd.merge(df, df_pwr, on='Date(NZST)')

print(df.head())

print(df.corr())

df.plot()
plt.show()


