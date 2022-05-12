import pandas as pd
import glob
import os

df = pd.read_csv("data1.csv")
#print(df)
df2 = pd.read_csv("data2.csv")

df_master = pd.DataFrame()

df_master = df_master.append(df)

df_master = df_master.append(df2)

print(df_master)

df_master.to_csv('data3.csv',index=False)
