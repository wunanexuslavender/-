# def LIANHUA(x,y):                    #另一种写法用map如下
#     results=[]                       #ctrl+/给一大坨上注释
#     result=x(y)
#     results.append(result)           #列表append加括号
#     return results
#
# def square(x):
#     y=[]
#     for value in x:
#         y.append(value*923)
#     return y
#
# lianhua=[5,2,0,1,3,1,4]
# results = LIANHUA(square,lianhua)
# print(results)


def lianhua(x):
    y=x*923
    return y

b=[5,2,0,1,3,1,4]
#b=input('请输入几个元素:')    #想用键盘输入的话定义空列表向里面添加元素即可
a=list(map(lianhua,b))      #关于map函数，将b中所有元素进行lianhua函数处理后加list生成一个列表
print(a)
