#x=0
#def outer():
#    x=1
#    def inner():
#        x=2
#        print('local=',x)
#    inner()
#    print('enclosing:x=',x)
#outer()
#print('global:x=',x)

#sum=0
#def func():
#    global sum#用关键词global声明对全局变量的改写操作   即可在函数中改写全局变量
#    print(sum)
#    for i in range(5):
#        sum+=1
#    print(sum)
#func()
#print(sum)


#func=lambda x,y:x+y     #匿名函数
#def add(x,y):           #两个函数等效
#    return x+y


#def lianhua(n):
#    if n==1:
#        return 1
#    else:
#        return n*lianhua(n-1)
#a=5
#print('%d!=%d'%(a,lianhua(a)))


w=100000
b=7000
def lianhua(n):
    if n==1:
        return w+b
    else:
        return lianhua(n-1)-w/(n-1)+w/n+b
min_t=w+b
for i in range(1,10):
    t=lianhua(i)
    print('CPU核心数:',i,'时间:',t)
    if t<min_t:
        min_t=t
        min_n=i
print('最佳CPU核心数为',min_n)




