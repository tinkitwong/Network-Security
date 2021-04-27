#/bin/bash

# reject ingress tcp packets for port 80 from 10.0.2.10
iptables -A INPUT -s 10.0.2.10 -p tcp --dport 80 -j REJECT

# reject ingress tcp packets for port 22 from 10.0.2.10
iptables -A INPUT -s 10.0.2.10 -p tcp --dport ssh -j REJECT

