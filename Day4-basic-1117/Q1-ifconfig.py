import os
import re

ifconfig_result = os.popen('ifconfig '+'ens33').read()


ipv4_addr = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[1]
broadcast = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[2]
mac_addr = re.findall(r'([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',ifconfig_result)[0]


print('%-10s: %-15s' %('ipv4_addr',ipv4_addr))
print('%-10s: %-15s' %('netmask',netmask))
print('%-10s: %-15s' %('broadcast',broadcast))
print('%-10s: %-15s' %('mac_addr',mac_addr))

route = os.popen('route '+'-n').read()
ipv4_gw = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',route)[1]

print('\n我们假设网关IP地址为最后一位是254，因此网关地址为:' + ipv4_gw +'\n')

ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall(r'(1 received)',ping_result)


if re_ping_result:
    print('网关可达!')
else:
    print('网关不可达!')