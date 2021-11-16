import re

mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

mac1 = re.match(r'(\d{1,3})\s+(\w{1,4}.\w{1,4}.\w{1,4}.\w{1,4})\s+(\w+)\s+(\w.*)',mac).groups()


print('%-10s : %s' % ('VLAN ID', mac1[0]))
print('%-10s : %s' % ('MAC', mac1[1]))
print('%-10s : %s' % ('Type', mac1[2]))
print('%-10s : %s' % ('Interface', mac1[3]))