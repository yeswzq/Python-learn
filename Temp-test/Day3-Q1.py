import re
mac = '166 54a2.74f7.0326 DYNAMIC  Gi1/0/11'

mac1 = re.match("(^\d{1,4096})\s([a-zA-Z0-9]{4}.{10})\s(\w*)\s*(.*)",mac).groups()

#拼接写法，要注意的是字符串格式化是不需要再括号起来的。 我这个括号起来是因为print的原因要括起来，变量是不需要的。
print ('{:10}: {:10}'.format('VLAN ID',mac1[0]))
print ('{:10}: {:10}'.format('MAC',mac1[1]))
print ('{:10}: {:10}'.format('Type',mac1[2]))
print ('{:10}: {:10}'.format('Interface',mac1[3]))

#一句话的写法
print('{:10}:{:10}\n {:10}:{:10}\n {:10}:{:10}\n {:10}:{:10}'.format('VLAN ID',mac1[0],'MAC',mac1[1],'Type',mac1[2],\
     'Interface',mac1[3]) )