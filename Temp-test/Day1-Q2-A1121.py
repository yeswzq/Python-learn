import random
address1 = random.randint(1,255)
address2 = random.randint(1,255)
address3 = random.randint(1,255)
address4 = random.randint(1,255)
address4_str = address4.__str__()
print(type(address4))
print(type(address4_str))

print(address1)

#这是解法1，直接调用函数然后打印，全部转换成字符串格式。
print(str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)))

#解法2，这是新发现的一个转换字符串的方法。如7、8行对比所示，打印的时候在变量后面加_str_可以将数字转换成字符串格式，然后再进行拼接。
print(address1.__str__() + '.' + address2.__str__() + '.' + address3.__str__() + '.' + address4.__str__())

#解法3，利用字符串格式化的方法，进行打印。字符串格式化看来真的是好使很多。
print('%d.%d.%d.%d'%(address1,address2,address3,address4))

#方法4,通过变量调用模块，然后直接拼接。该方法其实和解法1一样。我引入的目的就是为了能够参考\这个换行符。
ip = str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'\
     +str(random.randint(0,255))+'.'+str(random.randint(0,255))
print(ip)
