import numpy as np
import sympy as sp    #这个是待具体数值进入求解的包
x=sp.symbols('x')    #定义符号变量  即让x成为函数f(x)的自变量
y=x**3-7*x**2+2*x+40   #定义函数
y1=y.diff(x)      #y对x求一次导数
print('函数的一阶导数为:',y1)
y2=y1.diff(x)    #对y1求一阶导   注意，括号里是x不是y1,意思为y1对x求导
print('函数的二阶导数为：',y2)
