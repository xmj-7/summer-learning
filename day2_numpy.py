import numpy as np
a = np.array([[1,2,3],[4,5,6]])
#itemsize
x = np.array([1,2,3,4,5], dtype = np.int8)#返回数组中每个元素的长度。单位为字节
print (x.itemsize)
print(a.flags)#返回属性

#矩阵创建
x = np.empty([3,2],dtype=int)
print(x)#矩阵中的值都是随机的，x尚未初始化

#创建初值为0的矩阵
#x = np.zeros((5,5),dtype = int)
x = np.zeros((5,5), dtype = [('x', 'i4'), ('y', 'i4')]) 
print(x['x'])

#填充1
x = np.ones((2,2), dtype = [('x', 'i4'), ('y', 'i4')]) 
print(x['x'])

#numpy.asarray与array类似，参数较少，有利于将python序列转化为ndarray


x = [(1,2,3),(4,5)]
a = np.asarray(x)
print (a)

#使用range()进行创建：
list = range(5)
it = iter(list)
x = np.fromiter(it,dtype = float)
print(x)

#arange
x = np.arange(10,20,2,dtype=int)
print(x)

#linspace等差数列
x = np.linspace(10,20,5,dtype=float)#参数3是将此段距离分为5段,且包含起始和终止位置
print(x)

#logspace等比数列，通过base改变基数
x = np.logspace(1,10,10)#logspace(m,n,p)起始点10^m结束点10^n,p：多少个数
print(x)

#切片操作
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
b = a[1:]
print(b)

a = np.array([[1,2,3],[3,4,5],[4,5,6]])

print ('Our array is:')
print (a)

# this returns array of items in the second column
print ('The items in the second column are:')
print (a[...,1])

# Now we will slice all items from the second row
print ('The items in the second row are:')
print (a[1,...])

# Now we will slice all items from column 1 onwards
print ('The items column 1 onwards are:')
print (a[...,1:])

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,1,2], [0,1,0]]#y中第一个方括号内是行号，第二个是列号
#第一个数组中的（0,0），（1,1）和（2,0）元素。


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]

print ('The corner elements of this array are:')
print (y)


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

# using advanced index for column
y = x[1:4,[1,2]]

print ('Slicing using advanced index for column:')
print (y)

#~的使用,使用〜（补数运算符）省略NaN（非数字）元素。
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])

# 从数组中过滤非复杂元素。
a = np.array([1, 2+6j, 5, 3.5+5j])
print (a[np.iscomplex(a)])

#三角函数：
a = np.array([0,30,45,60,90])

print ('Sine of different angles:')
# Convert to radians by multiplying with pi/180
sin = np.sin(a*np.pi/180)
print (np.sin(a*np.pi/180))
print ("sin对应的角：")
inv = np.arcsin(sin)
print(np.degrees(inv))


print ('Cosine values for angles in array:')
cos = np.cos(a*np.pi/180)
print (np.cos(a*np.pi/180))
print("cos对应的角：")
inv = np.arccos(cos)
print(np.degrees(inv))


print ('Tangent values for given angles:')
tan = np.tan(a*np.pi/180)
print (np.tan(a*np.pi/180))
print("cos对应的角：")
inv = np.arctan(tan)
print(np.degrees(inv))
#通过arc与degrees函数得到对应的角



#四舍五入around
print("四舍五入")
a = np.array([1.0,5.55, 123, 0.567, 25.532])
print(np.around(a))

#numpy.around(a,decimals)
#decimals要舍入的小数位数。默认值为0.
#如果为负值，则将整数舍入到位于小数点左侧的位置

print (np.around(a, decimals = 1))#保留到小数点后1位
print (np.around(a, decimals = -1))#对整数部分进行四舍五入


#np.floor,返回不大于输入参数的最大整数
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print("原始输入:",a)
print("np.floor():",np.floor(a))

#np.ceil()，返回不小于输入的值
print("原始输入:",a)
print("np.ceil():",np.ceil(a))

#numpy算术运算

#以下为元素算数
a = np.arange(9,dtype = np.float).reshape(3,3)
print("First array")
print(a)

print("second array")
b = np.array([10,10,10])
print(b)

#矩阵相加
print("add the two arrays:")
print(np.add(a,b))

print("subtract this two arrays:")
print(np.subtract(a,b))

print("multiply this two arrays:")
print(np.multiply(a,b))

print ('Divide the two arrays:')
print (np.divide(a,b))


# 向量算数矩阵乘法：np.dot(a,b) 或 np.matmul(a,b)
#  或 a.dot(b) 或直接用 a @ b !
#转置
print(a.T)

#矩阵中的元素的倒数
print("原始数据：",a)
print("处理后：")
print(np.reciprocal(b))

#np.power,指数
a = np.array([10,100,1000])
print(np.power(a,2))
b = np.array([1,2,3])
print(np.power(a,b))

#np.mod取余
a = np.array([10,20,30])
b = np.array([3,5,7])

print ('First array:')
print (a)

print ('Second array:')
print (b)

print ('Applying mod() function:')
print (np.mod(a,b))

print ('Applying remainder() function:')
print (np.remainder(a,b))#与np.pow()效果一样

# numpy.real（） - 返回复杂数据类型参数的实部。

# numpy.imag（） - 返回复数数据类型参数的虚部。

# numpy.conj（） - 返回通过改变虚部符号得到的复共轭。

# numpy.angle（） - 返回复杂参数的角度。 该功能具有度数参数。如果为true，则返回角度，否则角度以弧度表示。


#angle功能：
# z	数组型变量	一个复数或者复数组成的列表。
# deg	bool型变量，可选参数	若为True，返回值采用角度制；若为False（默认），返回值采用弧度制。

# 变量名	数据类型	功能
# angle	n维数组或标量	复平面上从正实半轴出发沿逆时针方向到复数所在点走过的角度，默认数值类型为numpy.float64。