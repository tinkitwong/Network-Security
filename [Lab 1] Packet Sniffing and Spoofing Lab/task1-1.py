#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
	pkt.show()
 
# filter: icmp 
#pkt = sniff(filter='proto ICMP',prn=print_pkt)

# filter: tcp, specific src ip and dest. port 23
pkt = sniff(filter='dst host 10.0.2.8 or src host 10.0.2.8 and tcp dst port 23',prn=print_pkt)
#pkt = sniff(filter='tcp and (host 10.0.2.8 and dst port 23)', prn=print_pkt)

# filter: bidirectional pkts for a particular subnet.
#pkt = sniff(filter='net 172.217.194.0/24',prn=print_pkt)		  
