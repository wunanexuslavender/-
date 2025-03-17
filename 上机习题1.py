s1=[0,1,2,3,4,5,6]
s2=['SUN','MON','TUE','WED','THU','FRI','SAT']
s5=[]
for i in range(len(s1)):     #多维数组
    b=[s1[i],s2[i]]
    s5.append(b)
print('s5=',s5)
s9=[s1[3],s1[4]]
s3=s9*3
print('s3=',s3)      #引号要打逗号隔开
s4=''.join(str(x) for x in s2)
print(s4)

