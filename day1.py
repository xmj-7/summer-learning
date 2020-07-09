#-*- coding: UTF-8 -*-
#pyhton3以下的版本不会默认UTF-8编码，需要加上上述内容
print("你好，世界");

def main():#函数名
    print("in main\n")#若写成print(r"in main\n"),则换行符无效，r可替换为R
    print('='*10)
    print("this " " is " " string")#可自动级联字符串
    food=["1","2","3","4"]
    for i in food:
        print(i+" ", end="")#后面添加end="",避免换行，print会默认换行
    print()
    foo(10,5)
    pr3 = """这是一个段落
这是第二行"""#可利用"""进行换行
    print(pr3)
def foo(first,second):
    res = first*second;
    total = res+\
        first+\
            second;'''利用\进行多行显示'''
    print("total="+str(total))#类型转换
    print("%s * %s = %s "%(first,second,res))
    if(res>50):
        print(">50")
    elif(res==50):
        print("==50")
    else:
        print("<50")

'''
行注释
'''
if __name__ == '__main__':
    main()
    i1=1
    print("this value is",i1)#自动拼接,且会填充空格
    b=2
    while b<1000:
        print(b,end=",")#可将结尾换行用,替换掉
        b*=10
    a,b1,c,d = 20,5.5,True,4+3j#python支持复数
    print(type(a),type(b1),type(c),type(d))
    word = 'ilovepython'
    print(word[1:5])#区间是[1,5),字符串从左到右是0开始递增，从右到左是-1开始递减
    #替换操作如下：
    ww = list(word)
    ww[0]='q'
    word = ''.join(ww)
    print(word)
    #单独的word[i]不可被改变word[i]='1'是错的

    #list列表
    a = ['him', 25, 100, 'her']
    a+=a#列表可直接进行+运算
    print(a)
    a=a*2#支持*操作
    print(a)

    b = (1991, 2014, 'physics', 'math')
    print(len(b))

    #集合Set
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}#集合的两种创建方式
    b = set('alacazam')
    a = set('abracadabra')
    #差集
    print(a-b)
    #并集
    print(a|b)
    #交集
    print(a&b)
    #a和b中不同时存在的元素
    print(a^b)

    #字典
    tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
    print(tel['Jack'])
    tel['Mary']=4127#添加一个键值对
    print('Tom' in tel)
    print('Tom' not in tel)

    #可以这样创建字典
    tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    dic = {x: x**2 for x in (2, 4, 6)}
    dic2 = dict(sape=4139, guido=4127, jack=4098)


    #最开始的这个转移符，是保证不会多出一个无用的换行符
    print("""\
    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
    """)

    