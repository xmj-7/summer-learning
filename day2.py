'''
import sys
def main():
    #字典
    tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
    print(tuple(tel.items()))
    print(tuple(tel.keys()))

    #判断
    age = int(input("Age of the dog: "))
    print()
    if age < 0:  
        print("This can hardly be true!") 
    elif age == 1:  
        print("about 14 human years")
    elif age == 2:  
        print("about 22 human years") 
    elif age > 2:#判断条件后面的括号可加可不加，判断条件过多时，可以加上，易于阅读
        human = 22 + (age -2)*5
        print("Human years: ", human)

    #循环
    edibles = ["ham", "spam","eggs","nuts"]
    for food in edibles:
        if food == "spam":
            print("No more spam please!")
            break
        print("Great, delicious " + food)
    else:#这种else与for对齐叫做for else循环，：if成立就break，不成立就走else
        print("I am so glad: No spam!")
    print("Finally, I finished stuffing myself")

    #迭代器
    list = [1,2,3,4]
    it = iter(list)
    print(next(it))
    for x in it:
        print(x,end=" ")

    #生成器
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
#yield关键字可参见博客https://blog.csdn.net/mieleizhi0522/article/details/82142856/，这篇解释的很详细

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
if __name__ == "__main__":
    main()
'''

#函数
a = 4  # 全局变量
def area(width,height):
    return width*height

def main():
    width = float(input("请输入宽: "))
    height = float(input("请输入高: "))
    s = area(width,height)
    print(s)
    print_func1()
    print_func2()
    print(arithmetic_mean(45,32,89,78))
    print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
    print(arithmetic_mean(45,32))
    print(arithmetic_mean(45))
    print(arithmetic_mean())


    #列表推导式
    vec = [2, 4, 6]
    vec1 = [3*x for x in vec]
    print(vec1)
    vec2 = [3*x for x in vec if x > 3]
    print(vec2)
    vec3 = [str(round(355/113, i)) for i in range(1, 6)]
    print(vec3)

    #将3x4转变为4x3(矩阵的转置),详细解释参考：https://www.jb51.net/article/84428.htm

    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
    vec4 = [[row[i] for row in matrix] for i in range(4)]
    print(vec4)

    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[2:4]
    print(a)#范围删除

    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i,v)#使用enumerate遍历序列中的元素及下标

    #sorted排序函数
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):       #这里使用了set函数
       print (f)


    #同时遍历多个序列，可使用zip()组合
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
    
    # >>> a = [1,2,3]
    # >>> b = [4,5,6]
    # >>> c = [4,5,6,7,8]
    # >>> zipped = zip(a,b)
    # [(1, 4), (2, 5), (3, 6)]
    # >>> zip(a,c)
    # [(1, 4), (2, 5), (3, 6)]
    # >>> zip(*zipped)
    # [(1, 2, 3), (4, 5, 6)]



    #输入输出
    helloy = "hello\n"
    helloy = repr(helloy)#  repr() 函数可以转义字符串中的特殊字符
    print(helloy)
#     >>> # repr() 的参数可以是 Python 的任何对象
# ... repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))"

    for x in range(1, 11):#rjust将字符串靠右, 并在左边填充空格
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # 注意前一行 'end' 的使用
        print(repr(x*x*x).rjust(4))
    #方法二:数字format用法
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

    #zfill(nofz),左边填充0,个数为nofz-字符串中字符个数
    print('12'.zfill(5))
    print('we'.zfill(5))


    #字符format用法：
    print('{1} and {0}'.format('spam', 'eggs'))#按照序号填充
    #按照关键字填充
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    #按照位置与关键字组合填充
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))


    # 字典的传入
    #方法1
    # >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    # >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    #         'Dcab: {0[Dcab]:d}'.format(table))
    # Jack: 4098; Sjoerd: 4127; Dcab: 8637678

    #方法二
    # >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    # >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
    # Jack: 4098; Sjoerd: 4127; Dcab: 8637678



def print_func1():
    a = 17 # 局部变量
    print("in print_func a = ", a)
def print_func2():   
    print("in print_func a = ", a)

#可变函数调用参数个数
def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print("a = ", a)
if __name__ == "__main__":
    main()
