#!/usr/bin/python3

import socket
from scapy.all import *

IP_A= '10.0.2.13'
PORT= 9090

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_A, PORT))

while True:
	data, (ip, port) = sock.recvfrom(2048)
	print('{}:{} --> {}:{}'.format(ip, port, IP_A, PORT))
	pkt = IP(data)
	print('...Inside: {} --> {}'.format(pkt.src, pkt.dst))
