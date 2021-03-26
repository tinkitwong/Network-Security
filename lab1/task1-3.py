#!/usr/bin/python3
from scapy.all import *
import sys

MAXTTL=255
hostname = sys.argv[1]
ttl=1

while ttl < MAXTTL:
	a=IP(dst=hostname,ttl=ttl)
	b = ICMP()
	reply=sr1(a/b, verbose=0, timeout=2)
	if reply is None:
		print(ttl, '...') # handles router that don't send pkts
	elif reply[ICMP].type == 11: # exceeded ttl
		print(ttl, 'src: ', reply.src)
	elif reply[ICMP].type == 0:
		print(ttl, 'Done. src: ', reply.src)
		break	
	ttl+=1
	
