#/bin/bash

# reject egress telnet packets
iptables -A OUTPUT -p tcp --dport telnet -j REJECT

# block egress packets to external website - www.facebook.com
#iptables -A OUTPUT -p tcp -m string --string "facebook.com" --algo kmp -j DROP

# block egress packet to 1 of the many IPs of external wesbite - www.facebook.com (157.240.217.35)
iptables -A OUTPUT -p tcp --destination 157.240.217.35 -j DROP

# block egress packet to static website - www.syr.edu (128.230.18.63)
iptables -A OUTPUT -p tcp --destination 128.230.18.63 -j DROP
