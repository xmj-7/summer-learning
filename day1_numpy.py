import numpy as np
a = np.array([1,2,3])
print(a)
print(a.shape)

a = np.array([[1,2,3],[3,4,5]])
print(a)
print(a.shape)

a = np.array([1,2,3,4,5],ndmin = 2)#指定结果数组应具有的最小维数。根据需要，将根据需要预先设置形状。
print(a)
print(a.shape)

a = np.array([1,2,3,4],dtype=complex)#dtype指定数组内的数据类型
print(a)
print(a.shape)


#使用结构化数据类型。声明字段名称和相应的标量数据类型
dt = np.dtype([('age',np.int8)])
print(dt)
print(a.shape)

a = np.array([(10,),(20,),(30,)], dtype = dt)

print (a)
print(a.shape)

print(a['age'])#可以直接类似于字典访问

#定义了一个名为 student 的结构化数据类型，其中包含一个字符串字段'name'，
# 一个 整数字段 'age'和一个 浮点字段 'marks'。 这个dtype被应用于ndarray对象。
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])#分别用来规定不同元素的类型
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print (a)#student的内容相当于加个表名
print(a['name'])
print(a['age'])
print(a['marks'])
print(a.shape)


#调整矩阵大小
a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)#可以重新改变排列
print(a,"shape:",a.shape)
b = a.reshape(2,3)
print (b,"shape:",b.shape)

#维度
a = np.arange(24)
print(a)
print(a.ndim)#返回维度大小
b = a.reshape(2,4,3)
print(b)
print(b.ndim)
