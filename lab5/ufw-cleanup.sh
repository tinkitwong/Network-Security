#!/bin/bash
for ufw in `iptables -L | grep 'Chain ufw' | awk '{ print $2 }'`; do iptables -F $ufw; done

for ufw in `iptables -L | grep 'Chain ufw' | awk '{ print $2 }'`; do
  iptables -D INPUT -j $ufw
  iptables -D FORWARD -j $ufw
  iptables -D OUTPUT -j $ufw
done

for ufw in `iptables -L | grep 'Chain ufw' | awk '{ print $2 }'`; do iptables -X $ufw; done
