#时间2021-11-13 Day1作业

import random      #导入随机模块
#时间2021-11-13
ipaddress1=random.randint(1,254)  #定义4个变量
ipaddress2=random.randint(1,254)
ipaddress3=random.randint(1,254)
ipaddress4=random.randint(1,254)

#方法1字符串格式化打印
print('%d.%d.%d.%d'%(ipaddress1,ipaddress2,ipaddress3,ipaddress4))

#print(ipaddress)  #方法2
#ipaddress = str(ipaddress1) + '.' + str(ipaddress2) + '.' + str(ipaddress3) + '.' + str(ipaddress4) #方法2转换成字符串格式后拼接


#方法3,通过变量调用模块，然后直接拼接。
ip = str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'\
     +str(random.randint(0,255))+'.'+str(random.randint(0,255))
print(ip)


