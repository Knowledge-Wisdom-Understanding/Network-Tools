#!/usr/bin/env python

import socket
from urllib.request import urlopen
from json import load

# Best No Limit Option
my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
print("PUBLIC-IP = " + my_ip)

# For Developers
# my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
# print("PUBLIC-IP = " + my_ip)

# my_ip_json = load(urlopen('http://jsonip.com'))['ip']
# print("PUBLIC-IP = " + my_ip_json)

# my_ip = urlopen('http://ip.42.pl/raw').read()
# print("PUBLIC-IP = " + my_ip)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("PRIVATE-IP = " + s.getsockname()[0])
s.close()
