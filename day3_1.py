import datetime
import pickle
import pprint
class MyError(Exception):#自定义error
    def __init__(self, value):#value是用户传入的数据，__init__这个魔法方法用于初始化
        self.value = value
    def __str__(self):#用于返回异常类对象的说明信息
        return repr(self.value)
def main():
    #文件读写
    f = open('D:\\VSCode\\tfexe\\.python_base\\day3_1.txt','r+')
    a=7
    #f.read()，读所有内容
    #f.readline()读一行，如果f.readline()为空，代表此时已经读完了
    f.write('i will write 8 in this txt\n')#返回写入的
    print(f.read())
    print(' im reading')
    f.close()
    v=('the answer',42)
    s = str(v)
    print(s)


    #序列化与反序列化
    data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)

    output = open('data.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)

    # Pickle the list using the highest protocol available.
    pickle.dump(selfref_list, output, -1)

    output.close()

    #反序列化
    pkl_file = open('data.pkl', 'rb')

    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)#pprint规范输出，参考：https://blog.csdn.net/qq_24185239/article/details/80977556

    pkl_file.close()

    # print(data1)
    # print(data2)



    #异常处理
    try:
        x=int(input("Please enter a number:"))
    except (ValueError,TypeError):#可用括号将多种错误括起来
        print("Oops! That was no valid number. Try again")
    else:
        print("try except 语句还有一个可选的else子句，",
         "如果使用这个子句，那么必须放在所有的except子句之后。",
        "这个子句将在try子句没有发生任何异常的时候执行")
    #可使用raise 语句抛出异常：raise NameError('HiThere)

    #自动清理
    # with open("myfile.txt") as f:#文件使用完毕后，自动close
    #     for line in f:
    #         print(line, end="")

if __name__ == "__main__":
        main()







# time1 = str(input())
# time2 = str(input())
# dt1 = datetime.datetime(1010,10,10,int(time1[0:2]),int(time1[3:5]),int(time1[6:8]),0)
# dt2 = datetime.datetime(1010,10,10,int(time2[0:2]),int(time2[3:5]),int(time2[6:8]),0)
# if time1>time2:
#     sub = str(dt1-dt2)
# else:
#     sub = str(dt2-dt1)
# all_in = 0
# print(sub)
# if(sub[1]!=':'):
#     all_in = int(sub[0:2])*3600+int(sub[3:5])*60+int(sub[6:8])
# else:
#     all_in = int(sub[0:1])*3600+int(sub[2:4])*60+int(sub[5:7])
# print(all_in)