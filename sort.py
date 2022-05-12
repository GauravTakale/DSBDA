import pandas as pd
import glob
import os

df = pd.read_csv("data3.csv")

print(df)

print("sort")

df = df.sort_values(by=['name'])

print(df)

print("transpose")

result = df.transpose()

print(result)

print("shape and reshape")

# reshape the dataframe using stack() method
df_stacked = df.stack()
  
print(df_stacked.head(7))

df_unstacked = df_stacked.unstack()
print(df_unstacked.head(4))

