import numpy as np
A=np.array([[1,2],[4,1]])    #定义系数矩阵A,这里是大矩阵中套行矩阵的写法  用array
b=np.array([3,4])   #右边的
x=np.linalg.solve(A,b)    #solve函数解方程
print('x=',x[0])   #0是第一个元素
print('y=',x[1])

  #阶数更高的线性方程组就是x1,x2,x3那些而不是x,y了,