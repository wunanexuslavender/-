import copy
import calendar
#d={}
#print(d.get('name'))

#d={'lianhua':123}
#d['lian']=3
#y=d.copy()
#print(y)

#print('{lianhua}')
#键是唯一的，不可重复
y=input("请输入年:")
m=input("请输入月:")
d=input("请输入日:")
dic={0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期天'}
if y.isdigit() and m.isdigit() and d.isdigit and 1<=int(m)<=12 and 1<=int(d)<=31:
    w=calendar.weekday(int(y),int(m),int(d))
    print('您输入的%s年%s月%s日是%s'%(y,m,d,dic[w]))
else:
    print(您输入的日期有误)

    # d={key1:value1,key2:value2}
    # dict1={'alsk':4098,[3,3]:(3,4)}
    # print(dict1)
    # 'name' in d








