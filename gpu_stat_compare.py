import pandas as pd
import numpy as np
import sys


df = pd.read_csv(sys.argv[1], delimiter=',')

print(df)
#df = df[df["utilization.gpu [%]"] != "0 %"]
df = df[df["utilization.gpu [%]"] != "utilization.gpu [%]"]
print('new')
print(df)

def clean_col(column, col_name):
    lst = []
    for i in range(0, (column.shape[0])):
        elem = (column.iloc[i]).split()[0]
        x = float(elem)
        lst.append(x)
    return lst

def get_col_max(df):
    for i in range(df.columns.shape[0]):
        print(df.columns[i], df[df.columns[i]].max())

def get_col_mean(df):
    for i in range(df.columns.shape[0]):
        print(df.columns[i], df[df.columns[i]].mean())

print(df.shape)

col_names = df.columns
dict = {}
for col_name in col_names:
    dict[col_name] = clean_col(df[col_name], col_name)
    print(col_name," max ",  max(dict[col_name]))
    print(col_name, " mean ",sum(dict[col_name])/len(dict[col_name]))

#second pass

df = df[df["utilization.gpu [%]"] != "0 %"]

print(df.shape)

col_names = df.columns
dict = {}
for col_name in col_names:
    dict[col_name] = clean_col(df[col_name], col_name)
    print(col_name," max ",  max(dict[col_name]))
    print(col_name, " mean ",sum(dict[col_name])/len(dict[col_name]))
