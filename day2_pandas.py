import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

date = pd.date_range("20200716",periods=6)
print(date)
print(np.arange(0,24))
df = pd.DataFrame(data=np.arange(0,24).reshape(6,4),index=date,columns=['a','b','c','d'])
print(df)
print(df['a'],df.a)#获取'a'列数据,第二种也可以获取
print(df[0:3],df['20200716':'20200718'])#取0到3行的数据

#select by label:loc,根据标签选择
print(df.loc['20200716'])#根据行号选择
print(df.loc[:,['a','b']])#保存所有行的项目，打印列'a'与列'b'之间的数据
print(df.loc['20200716','a'])#特定某行某列

#select by position ：iloc 选择对应的位置
print(df.iloc[3])#第三行数据
print(df.iloc[3,1])#特定行列
print(df.iloc[3:5,1:3])#切片操作

print(df.iloc[[1,3,5],[1,2]])#不连续的选择

# #mixed selection:ix综合loc 和 iloc
# print(df[:3,['a','c']])#标签和位置混合筛选
#ix方法被弃用

#Boolean indexing 
print(df)
print(df[df.a>8])#筛选a列中所有大于8的数据


#值的修改
df.iloc[2,2]=111
df.loc['20200716','b']=222
df.a[df.a>4]=0#df.b[df.a>4]=0#b里面的也可以改
#df[df.a>4]#与上面的是有区别的，这个是a中大于4的部分,包括b,c,d都得修改，上面的只针对于a这一列
print(df)
#添加新列
df['f'] = np.nan
df['e'] = pd.Series([1,2,3,4,5,6],index=df.index)#需要添加index来对齐，直接df,index就行
print(df)

print(df.dropna(axis=0,how='all'))#丢掉行中存在nan的数据,how={'any','all'}#全部是nan或者存在一个nan
print(df.dropna(axis=1,how='any'))#不会改变原值
print(df.fillna(value=0))#所有nan替换为0
print(df.isnull())#返回True或者false来判断是否缺失值
print(np.any(df.isnull()) == True)#至少有一个丢失的值，就是返回True

#数据的保存与读取
# data = pd.read_csv('D:\\VSCode\\tfexe\\.python_base\\students.csv')
# print(data)
# data.to_csv("student.csv")

#数据合并
#concatenationg
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))* 2, columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#竖向合并，axis=1是横向合并
#ignor是对行描述重新排序,axis默认为0
print(res)
df2.columns=['b','c','d','e']
df2.index=[2,3,4]
#join功能 ['inner','outer']
print(df1)
print(df2)
res=pd.concat([df1,df2],ignore_index=True)#默认为outer的连接模式
print(res)
res = pd.concat([df1,df2],join='inner',ignore_index=True)#只输出都有的部分(指列名相同)
print(res)

#左右合并
res = pd.concat([df1,df2],axis=1,join='inner')#同样的只用相同的
print(res)


#append,添加数据
res = df1.append([df2,df3],ignore_index=True)
print(res)
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True)#添加一行数据
print(res)

#merging two df by key/keys.(may be used in database)
#simple example
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key':['K0',' K1', 'K2', 'K3'],
                    'C': ['C0','C1', 'C2','C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)
res = pd.merge(left,right,on="key")#后面的on是指基于什么进行合并
print(res)
left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                    'key2': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    })
right = pd.DataFrame({'key1': ['K0', 'K0', 'K2', 'K3'],
                    'key2': ['K0', 'K0', 'K2', 'K3'],
                    'A': ['C0','C1', 'C2','C3'],
                    })

#how={'inner','outer','left','right'}
res = pd.merge(left,right,on=['key1','key2'],suffixes=['1','2'],how='outer')
print(res)#考虑两个key,默认inner，只有值相同，才会把对应列放下来，how = 'inner
#有一个indercater='name'，指示是如何合并的(name是你要显示出来的名字)
#suffixes在未指定列名后面添加注释，只允许两个


#绘图
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
datat = data.cumsum()#累加,类似于斐波那契
plt.show()


#DataFrame
data = pd.DataFrame(np.random.randn(1000,4),index = np.arange(1000),
columns=list("ABCD"))#分四组数据
data = data.cumsum()
data.plot()
plt.show()
print(data)


#散点图
ax1 = data.plot.scatter(x='A',y='B',color='DarkBlue',label = "Class1")
data.plot.scatter(x='C',y='D',color='DarkGreen',label = "Class2",ax=ax1)#后面的ax是将其附在上面的图中
plt.show()

