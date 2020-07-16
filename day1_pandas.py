import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,33,1])
print(s)
dates = pd.date_range('20160101',periods=6)
print(dates)
print(np.random.randn(6,4))
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)#先生成6行4列的数据，再令index变成对应行数的array，列名为a,b,c,d
df1 = pd.DataFrame(np.random.randn(3,4))
print(df1)
d = np.arange(12).reshape(3,4)
print(d.__add__([1]))
print(d+[1])
print(df.dtypes)#返回每一列的数据类型
print(df.columns)
print(df.values)
print(df.describe())#只能对数字进行各种数学运算运算
print(df.describe().iloc[2])#指定取通过哪个类型计算的数据

print(df.sort_index(axis=1,ascending=False))
#对列名进行排序，且为倒序，如果是0就是行名排序,如下

print(df.sort_index(axis=0,ascending=False))

print(df.sort_values(by='E'))#对单行值进行排序