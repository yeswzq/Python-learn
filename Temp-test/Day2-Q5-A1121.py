import re

str1 = 'Port-channel1.189  192.168.189.254 YES CONFIG  up'

#re.match的匹配必须是双引号。matc匹配出字符的话必须由头到位给匹配出来。

interface = re.match("(\w*.\w*\.\w*)",str1).groups()
ipadd = re.match("(\w*.\w*\.\w*)\s*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*(up|down)",str1).groups()
ipadd_type = (type(ipadd))

#re.findall可以是匹配出自己想要的字符内容即可。例如下面这段就是匹配出192.168.189.254，加上了|up，这个可以研究下。
ipaddf = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|up",str1)


#下面的案例中如果我想匹配答案中的三个结果，那么我就必须要分开写3条规则才能实现。不是统一的字符，本题不适用。
ipaddf1 = re.findall(r"(\w*.\w*\.\w*)\s*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*(up|down)",str1)[0]

#re.findall的匹配思想是匹配指定的字符，然后帮你以逗号分段。然后你再引用
#ipv4_gw = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',route)[1]
# ['0.0.0.0', '10.0.20.254', '0.0.0.0', '10.0.20.0', '0.0.0.0', '255.255.255.0'] 以，为分段。

print(ipaddf)
print(ipaddf1)
#拼接的后面还要加上+号
print('通过正则表达式匹配后输出的变量类型是:' + str(ipadd_type))
#或者不需要那么麻烦，直接一句话解决就好了。
print('通过正则表达式匹配后输出的变量类型是:' + str(type(ipadd)))


print('{:<20s}: {:<20s} \n{:<20s}: {:<20s} \n{:<20s}: {:<20s}'.format('接口',ipadd[0],'IP地址',ipadd[1],'状态',ipadd[2]))



