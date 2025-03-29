#11\d可匹配114,,d代表一个数字   \d\d 02          \d
#字符'a'等                                     \w
#.任何字符                                            .
 #     [p|P]athon   [1-9]\d   d{2}#重复2次
#\.#打印/.

#'ab+c'#贪婪匹配
#'ab+?c'

#p=re.compile('''[0-9a-zA-Z\_])

import re
p=re.compile('^[a-zA-Z0-9]{1,10}@[a-zA-Z0-9]{1,10}.(com|org)$',re.I)
while True:
    s=input('请输入测试E-mail地址(输入0退出程序):\n')
    if s=='0':
        break
    m=p.match(s)
    if m:
        print('%s符合规则'%s)
    else:
        print('%s不符合规则'%s)



