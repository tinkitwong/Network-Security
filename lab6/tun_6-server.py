#!/usr/bin/python3

import fcntl
import struct
import os
import time
import select
from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000
IP_A= '10.0.2.13'
PORT= 9090

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tun%d', IFF_TUN | IFF_NO_PI)
ifname_bytes  = fcntl.ioctl(tun, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

# Assign IP address to the interface
os.system("ip addr add 192.168.60.2 peer 192.168.60.1 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))
os.system("ip route add 192.168.53.0/24 dev {} via 192.168.60.2".format(ifname))
os.system("sysctl net.ipv4.ip_forward=1")

# Create UDP Server on VPN Server to recv from Host U
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_A, PORT))

# Create UDP Socket --> Host U's UDP Server
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	# this will block until at least one interface is ready
	ready, _, _ = select.select([sock, tun], [], [])
	for fd in ready:
		if fd is sock:
			# get data from socket interface
			data, (ip, port) = sock.recvfrom(2048)
			pkt = IP(data)
			print("From socket <==: {} --> {}".format(pkt.src, pkt.dst))
			#sock.connect((pkt.dst, pkt))
			os.write(tun, bytes(pkt))
			
		if fd is tun:
			packet = os.read(tun, 2048)
			pkt = IP(packet)
			print("From tun ==>: {} --> {}".format(pkt.src, pkt.dst))
		
			# write packet to tun interface 
			# get pkt and send to the enp0s3 intf.
			ss.sendto(bytes(pkt), ("10.0.2.11", 9000))
			os.write(tun, bytes(pkt))
