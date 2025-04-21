import sympy as sp
x=sp.symbols('x')
y=(x-1)*(x-2)*(x-3)*(x-4)
y8=y.subs(x,8)    #subs用来将具体数值代入函数(x,8)将8代入x
print('多项式的值为:',y8)