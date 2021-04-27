#/bin/bash

# reject ingress telnet packets
iptables -A INPUT -p tcp --dport telnet -j REJECT

# reject egress telnet packets
iptables -A OUTPUT -p tcp --dport telnet -j REJECT

# block egress packets to external website - www.facebook.com
iptables -A OUTPUT -p tcp -m string --string "facebook.com" --algo kmp -j DROP

# block egress packet to external website - www.google.com
iptables -A OUTPUT -p tcp -m string --string "google.com" --algo kmp -j DROP
