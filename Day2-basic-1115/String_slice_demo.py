#字符串截取切片实验案例
#从前往后索引下标值：  0  1  2  3  4  5
#str_index 字符串:  a  b  c  d  e  f
#从后往前索引小标值:  -6 -5 -4 -3 -2 -1

str_lt = "abcdef"

print(len(str_lt))         #运行结果:6
print(str_lt)              #运行结果:abcdef
print(str_lt[:])           #运行结果:abcdef
print(str_lt[2:4])         #运行结果:cd,会截2之后的，4当前的。
print(str_lt[:3])          #运行结果:abc，会运行包括第3位前面的。
print(str_lt[1:])          #运行结果:bcdef，获取第1位a之后的所有字符。
print(str_lt[-4:-1])       #运行结果:cde，就是反过来的顺序，-1还是之后的，-4是当前的。
print(str_lt[-2:])         #运行结果:ef，-2在前面就是从当前为开始
print(str_lt[:-2])         #运行结果:abcd

str_num = "0123456789"       #字符跳跃截取
print(str_num[1::2])        #运行结果:13579
print(str_num[2::2])        #运行结果2468
print(str_num[-10::2])      #运行结果：02468

#如果  开始索引>=结束索引，返回空
print(str_num[3:4])
print(str_num[4:3])
print(str_num[-3:-4])
