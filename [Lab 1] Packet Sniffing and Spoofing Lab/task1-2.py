#!/usr/bin/python3
from scapy.all import *

a = IP()
# spoof ip src. 
a.src = '1.2.3.4'
a.dst = '10.0.2.6'
b = ICMP()
p = a/b
send(p)
