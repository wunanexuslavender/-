import numpy as np
np.random.seed(0)         #随机种子
A=np.random.randint(0,7,size=(5,5))   #size(行数，列数)   0,7指的是数值0到6
print('随机数矩阵为 A:')
print(A)

try:               #这个try是在网上搜的，我忘了有奇异矩阵这个事所以之前程序是错的
    B=np.linalg.inv(A)     #求逆矩阵的代码
    print(f'矩阵A的逆矩阵为{B}')
except np.linalg.LinAlgError:
    print('矩阵A为奇异矩阵，没有逆矩阵')

lianhua=np.linalg.eigvals(A)    #求特征值的代码
print(lianhua)