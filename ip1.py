import ipaddress
net = ipaddress.ip_network('192.168.0.0/17')
for i in net:
    print(i)

