import re

str1 = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

session = re.match('\s*(\w+)\s+server\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)\s+localserver\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+),\s+idle\s+(\d+:\d+:\d+),\s+bytes\s+(\d+),\s+flags\s+(\w+)',str1).groups()

split_idle = session[3].split(':')

hour = split_idle[0]
min = split_idle[1]
second = split_idle[2]

print(f'{"protocol":<20}: {session[0]}')
print(f'{"server":<20}: {session[1]}')
print(f'{"localserver":<20}: {session[2]}')
print(f'{"idle":<20}: {hour:<2}小时 {min:<2}分钟 {second:<2}秒')
print(f'{"bytes":<20}: {session[4]}')
print(f'{"flags":<20}: {session[5]}')
