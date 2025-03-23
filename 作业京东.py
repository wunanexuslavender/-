ls1=[]
for i in range(5):
    a=input('请输入商品及代码')
    ls1.append(a)

for n in ls1:
    print(n)
b=[]
while True:
    lianhua=False
    num=input('请输入你要的编号')
    for n in ls1:
        if num==n[0:4]:
            lianhua=True
            b.append(n)
            print('成功加到购物车')
            break
    if num=='q':
        break
print('您选择的商品为:')
b.reverse()
for n in b:
    print(n)

