import re
session = 'TCP server 172.16.1.101:443 localserver 172.22.66.1:53710, idle 0:22:09, bytes 27575949, flags UIO'

#可以优化的点，就是 server 匹配前面这个字段，可以不用那么复杂。直接.*\s然后匹配。
asasession = re.match('(^TCP|UDP)\s*\w*\s*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,5})\s*\w*\s*(\d{1,3}.\d{1,3}.\d\
{1,3}.\d{1,3}):(\d{1,5}).\s\w*\s*(\d*):(\d*):(\d*).\s*bytes\s*(\d{1,10}).\s*flags\s(\w{1,4})',session).groups()
print(asasession)

# ('TCP', '172.16.1.101', '443', '172.16.66.1', '53710', '0', '01', '09', '27575949', 'UIO')



print("{:20}:{}".format('Protocol',asasession[0]))
print("{:20}:{}:{}".format('server',asasession[1],asasession[2]))
print("{:20}:{}:{}".format('localserver',asasession[3],asasession[4]))
print("{:20}:{}小时{}分钟{}秒".format('idle',asasession[5],asasession[6],asasession[7]))
print("{:20}:{}".format('bytes',asasession[8]))
print('{:20}:{}'.format('flags',asasession[9]))