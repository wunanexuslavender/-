b={'l':5,'i':2,'a':0,'n':1,'h':4}
a={5:'l',2:'i',0:'a',1:'n',4:'h'}
#password='lianh'    #不打引号会当作专词而非字符串
password=52014
jiami_password=''  #赋值空的字符串
for n in str(password):     #加密过程
    jiami_password+=a[int(n)]
print(f'加密后的密码:{jiami_password}')    #f就可以用花括号里的内容了
jiemi_password=''
for i in jiami_password:
    jiemi_password+=str(b[i])
print(f'解密后的密码:{int(jiemi_password)}')

