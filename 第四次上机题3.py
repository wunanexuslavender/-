
def pr(func):       #用于装饰器的函数函数名若为LIANHUA()，则用于装饰时在被装饰函数上一排加@LIANHUA
    def lianhua(x):    #接下来使用被装饰函数时返回装饰函数的值
        y=func(x)            #注意，装饰器函数里面定义的函数才是执行函数，return的位置在外层函数
        print(f'{x}的平方为{y}')
    return lianhua     #这里return的位置

@pr
def square(x):
    return x*x


a=int(input('请输入x的值:'))
square(a)