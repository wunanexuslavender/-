import re
p=re.compile('^[a-zA-Z0-9]{1,10}@[a-zA-Z0-9]{1,10}.(com)$',re.I)
while True:
    s=input('请输入你要判断的教育邮箱(输入0退出程序):\n')
    if s=='0':    #这里0要加引号
        break
    m=p.match(s)     #match为匹配   p.match是作为正则表达式实例化对象p使用
    if m:
        print('%s符合规则'%s)
    else:
        print('%s不符合规则'%s)


