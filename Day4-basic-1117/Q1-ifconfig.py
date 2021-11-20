import os
import re

ifconfig_result = os.popen('ifconfig '+'ens33').read()

addr = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)

ipv4_addr = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[1]
broadcast = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[2]
mac_addr = re.findall(r'([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',ifconfig_result)[0]

print(type(ifconfig_result))
# format_string = '{ipv4_addr},{netmask},{broadcast},{mac_addr}'

# print('mac-')
# print(format_string.format(%(0)))