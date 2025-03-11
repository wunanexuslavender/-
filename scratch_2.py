import calendar
s=("星期一星期二星期三星期四星期五星期六星期日")
while True:
    y=input("请输入年,x为退出\n")

    if y in ("x","X"):
        break
    else:
        m=input("请输入月\n")
        d=input("请输入日\n")
        i=calendar.weekday(int(y),int(m),int(d))
        print("您所输入的日期{0}年{1}月{2}日是:{3:>5}".format(y,m,d,s[i*3:i*3+3]))
