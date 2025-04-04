#for n in range(1,5,2):
#    print('我爱莲华')

#class animals:
#    pass
#class mammals(animals)         #第一个子类，继承父类全部属性
#    pass
#class dog(mammals)             #第二个子类
#    pass

#class dog(object):               #class也有冒号
#    def  __init__(self,name,kind,month_age):  #每个定义了的属性中有一个self，这里是定义所有属性
#       self.name = name                    #这里记得空格缩进形式全变为self.a=a,a为上述定义的属性
#       self.month_age=month_age
#       self.kind=kind
#    def __str__(self):
#        return'<狗名:%s(%s,%d个月)>'%(self.name,self.kind,self.month_age)
#    def bark(self):                     #所以执行Bob.bark（）时print汪汪
#        print('汪汪')

#if __name__ =='__main__':
#    Bob=dog('Bob','金毛',9)
#    print(Bob)
#    Bob.bark()


#class Company:
 #   def __init__(self,dept,leader):
  #      self.dept=dept
   #     self.leader=leader
    #def show(self):
     #   print(self.dept)
      #  print(self.leader)

#if __name__=='__main__':
 #   obj1=Company('A','莲华')
  #  obj2=Company('B','lianhua')

 #   print(obj1.dept)
  #  print(obj1.leader)    #第一种调用方法，直接调用

#    obj1.show()
 #   obj2.show()        #第二种调用方法，通过self来调用


#创建一个包，只需在这个文件夹中有一个文件名为__int__.py的文件  里面没东西都行


#import math as lianhua #把math命名为lianhua

#import datetime
#from datetime import datetime     #datetime里面还有一个datetime方法  如果不用里面这个方法类，下面会出错
#now=datetime.now()                #获取当前时间 datetime.now()
#print(now)                       #打印当前时间
#b=datetime.timestamp
#t=9235201314.0                    #这种浮点数的格式占储存空间小
#print(b)                          #这里把b进行的操作步骤打印出来了
#print(datetime.fromtimestamp(t))  #将timestamp转化为datetime  fromtimestamp前面加utc化为国际单位
#print(now.strftime('%y %Y %m %d %h %I %M %S %a %A %b %B'))  #

#import  sys
#print(dir(sys))      #dir 是一个自带函数，用于展示所带方法
#print(sys.path)



















