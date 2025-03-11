factor=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
last=['1','0','X','9','8','7','6','5','4','3','2']
while True:
    id=input("请输入身份证号,0则退出")
    if id=="0":
        break
    if len(id)!=18:
        print("输入位数不对,请重新输入")
        continue
    else:
        sum=0
        for i in range(17):
            sum=+int(id[i])*factor[i]
            m=sum%11
            lastchar=id[-1]
            lastchar=lastchar.upper()
            if lastchar==last[m]:
                print(id,'为合法身份证号码,',end='')
                if int(id[-2])%2==0:
                    print('为女性')
                else:
                    print('为男性')
            else:
                print(id,"为非法号码")
