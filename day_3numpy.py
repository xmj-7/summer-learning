import numpy as np
from matplotlib import pyplot as plt
import math as m
#最小最大值
a = np.array([[3,7,5],[8,4,3],[2,4,9]])

print("源输出：")
print(a)
print(np.amin(a))#直接输出最小值
print(np.amin(a,1))#1对应的是每一行的最小值
print(np.amin(a,0))#0是对应的列

print(np.amax(a))#直接输出最大值
print(np.amax(a,1))#1对应的是每一行的最大值
print(np.amax(a,0))#0是对应的列


#np.ptp()返回max-min
print(np.ptp(a))#所有数字
print(np.ptp(a,1))#按行来
print(np.ptp(a,0))#按列来


#numpy.percentile(a, q, axis),取在矩阵a中位于q%的数，从该数开始，左边是q%,右边是(100-q)%
print ('Applying percentile() function:')
print (np.percentile(a,50))

print ('Applying percentile() function along axis 1:')
print (np.percentile(a,50, axis = 1))

print ('Applying percentile() function along axis 0:')
print (np.percentile(a,50, axis = 0))

#取中位数
a = np.array([[30,65,70],[80,95,10],[50,90,60]])

print ('Our array is:')
print (a)
print ('\n') 

print ('Applying median() function:')
print (np.median(a))
print ('\n')  

print ('Applying median() function along axis 0:')
print (np.median(a, axis = 0))
print ('\n')  

print ('Applying median() function along axis 1:')
print (np.median(a, axis = 1))

#算数平均数
print(np.mean(a))#全部
print(np.mean(a,axis=1))#行
print(np.mean(a,axis=0))#列

#加权平均数
a = np.arange(6).reshape(3,2)
print(np.average(a))#权重默认全部为1
wt = ([1,2])#权重,当权重矩阵与要计算的矩阵不匹配的时候，要添加axis参数，使其至少与行或者列相匹配
print(np.average(a,weights=wt,axis=1))


#标准差：
a = np.array([1,2,3,4])
print(np.std(a))

#方差
print(np.var(a))


#排序,可通过kind调整排序规则，排序的算法，提供了快排'quicksort'、混排'mergesort'、堆排'heapsort'， 默认为‘quicksort'
a = np.array([[3,7],[9,1]])

print ('Our array is:')
print (a)
print ('\n')

print ('Applying sort() function:')
print (np.sort(a))
print ('\n')

print ('Sort along axis 0:')
print (np.sort(a, kind='heapsort', axis = 0))#列维度，从上到下依次递减
print ('\n')  

# Order parameter in sort function
dt = np.dtype([('name', 'S10'),('age', int)])
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt)

print ('Our array is:')
print (a)
print ('\n') 

print ('Order by name:')
print (np.sort(a, order = 'name'))

#如果a是一个numpy array，a.take(m,1)表示取每一行的第m个值；a.take(m,0)表示取第m行
#索引排序
x = np.array([3, 1, 2])
a=np.argsort(x)#返回值是对应的索引
#argsort函数返回的是数组值从小到大的索引值,[3, 1, 2]
#从小到大为[1，2，3],其对应的索引为[1，2，0]
print(a)

#lexsort按照键值排序
nm = ('raju','anil','ravi','amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
print((dv,nm))
ind = np.lexsort((dv,nm))#返回值是索引，排序主键是nm

print ('Applying lexsort() function:')
print (ind)
print ('\n')  

print ('Use this index to get sorted data:')
print ([nm[i] + ", " + dv[i] for i in ind])

#返回最大值最小值索引argmax,argmin
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.argmax(a))
print(a.flatten())#扁平化

#非0索引
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
x = np.nonzero(a)
print(a[x])#可以直接这样输出非0值
t = list(x)
print(x)
print(t[0])#可得到对应的0非零的位置，返回的是x
print(t[1])#可得到对应的0非零的位置，返回的是y
aa = np.array([t[0],t[1]])
print(aa[:,1])

#where()返回满足给定条件的输入数组中元素的索引
x = np.arange(9.).reshape(3, 3)

print ('Our array is:')
print (x)  

print ('Indices of elements > 3')
y = np.where(x > 3)
print (y)  

print ('Use these indices to get elements satisfying the condition')
print (x[y])

#extract()返回满足任何条件的元素。
print ('Our array is:')
print (x)  

# define a condition
condition = np.mod(x,2) == 0

print ('Element-wise value of condition')
print (condition)  

print ('Extract elements using condition')
print (np.extract(condition, x))

#view()深拷贝
a = np.arange(6).reshape(3,2)

print ('Array a:')
print (a)

print ('Create view of a:')
b = a.view()
print (b)

print ('id() for both the arrays are different:')
print ('id() of a:')
print (id(a) ) 
print ('id() of b:')
print (id(b) ) 

# Change the shape of b. It does not change the shape of a
b.shape = 2,3

print ('Shape of b:')
print (b)

print ('Shape of a:')
print (a)
#深拷贝同样可以使用如下操作
b = a.copy()
a = np.eye(3,3)#对角矩阵
print(a)
# 单位矩阵
a = np.identity(5)#单位矩阵
print(a)
b = np.identity(5)
print(a.dot(b))#向量乘法
a=np.array([[1,2],[3,4]])
b=np.array([[1,2],[3,4]])
print("dot: ",np.dot(a,b))
#vdot用于复数相乘
#inner用于行与行相乘

#logistic函数
x = np.arange(-11,11,dtype = float)
y = 1/(1+np.power(m.e,-x))
y.dtype=float
print(x)
print(y)
plt.title("logistic function")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()