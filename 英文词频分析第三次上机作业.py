f=open("D:\python老师发的辅助文件\新建 Text Document.txt",'r',encoding='ansi')
speech_text=f.read()         #英文编码用ansi
f.close()
speech=speech_text.lower().split()   #变小写后排序
dic={}
for word in speech:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1
swd=sorted(list(dic.items()),key=lambda lst:lst[1],reverse=True)
f1=open('D:\python老师发的辅助文件\英语虚词_实际上是个空文件_因为我没有包含英语虚词的txt文件_所以只能用这个了.txt','r',encoding='ansi')
f2=f1.read()
f1.close()
for kword,times in swd:
    print(kword,times)