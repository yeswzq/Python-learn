#摘抄案例
import re
import os
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
# suppose_ifconfig_output = '''ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
#               inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
#               inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
#               ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
#               RX packets 174598769 bytes 1795658527217 (1.6 TiB)
#               RX errors 1 dropped 24662 overruns 0 frame 0
#               TX packets 51706604 bytes 41788673420 (38.9 GiB)
#               TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0'''
ipv4_add = re.findall('inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall('netmask\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
broadcast = re.findall('broadcast\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
mac_addr = re.findall('ether\s([0-9a-fA-F]{2}[:][0-9a-fA-F]{2}[:][0-9a-fA-F]{2}[:][0-9a-fA-F]{2}[:][0-9a-fA-F]{2}[:][0-9a-fA-F]{2})',ifconfig_result)[0]

format_string = '{0:10}:{1}'

print(format_string.format('ipv4_add',ipv4_add))
print(format_string.format('netmask',netmask))
print(format_string.format('broadcast',broadcast))
print(format_string.format('mac_addr',mac_addr))

ipv4_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.',ipv4_add)[0]+'254'       #原来还可以再后面继续加数字。

print('\n我们假设网关的IP地址最后一位为254，因此网关IP地址为：' + ipv4_gw + '\n')

suppose_ping_result = """PING 172.16.66.254 (172.16.66.254) 56(84) bytes of data.
64 bytes from 172.16.66.254: icmp_seq=1 ttl=52 time=54.2 ms
--- 172.16.66.254 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 54.157/54.157/54.157/0.000 ms"""             #os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result = re.search('1\sreceived',suppose_ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达')