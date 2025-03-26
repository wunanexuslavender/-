import jieba
f=open('D:\python老师发的辅助文件\荷塘月色.txt','r',encoding='jbk')
article_text=f.read()
f.close
article=jieba.icut(article_text)
dic={}
for word in article:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1
swd=sorted(list(dic.items()),key=lambda lst:lst[1],reverse=True)
f1=open('中文虚词列表.txt','r',encoding='gbk')
stop_wds=f1read()
f1.close()
for kword,times in swd:
    if kword not in stop_wds:
        print(kword,times)
#记得用pip安装jieba包