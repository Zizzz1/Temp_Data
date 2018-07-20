import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 10)

df = pd.read_csv('C:\\mypythonscripts\\Temp-Py\\temp.csv', skiprows=2,
                 index_col='Date(NZST)', usecols=['Date(NZST)','Tmin(C)', 'Tmax(C)'],
                 parse_dates=['Date(NZST)'])

print(df.head())

print(df.corr())

df.plot()
plt.show()


