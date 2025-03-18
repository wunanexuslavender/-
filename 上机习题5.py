lianhua=set()
n=int(input('请输入你要录入的人的个数:'))
for i in range(n):#
    person=str(input(f'请输入第{i+1}位好友的姓名和手机号码:'))
    lianhua.add(person)
print(lianhua)
#while True:    #用这个就可以一直执行了while,for,if,都要冒号

