#!/bin/bash
# responsible for installing nat between 2 network interfaces
#  wlx00e04c6770ed (upstream/gateway) <- (NAT) <- en01 <- tp-link <- (192.168.7.0 WORK-E NETWORK)
# on work-e
#
# file : /sbin/nat.sh
# chmod +x /sbin/nat.sh
#
# references :  https://www.howtoforge.com/nat_iptables

echo starting iptables nat

# ipforwarding
sysctl -w net.ipv4.ip_forward=1
# verify
sysctl net.ipv4.ip_forward

iptables --flush            # Flush all the rules in filter and nat tables

iptables --table nat --flush

iptables --delete-chain

# Delete all chains that are not in default filter and nat table

iptables --table nat --delete-chain

# Set up IP FORWARDing and Masquerading
# eno1 is "private" wlx is "public"

iptables --table nat --append POSTROUTING --out-interface wlx00e04c6770ed -j MASQUERADE
iptables --append FORWARD --in-interface eno1 -j ACCEPT

# clean up (deletes) FIXME - perhaps persist via netplan explicit routes
# ip route delete 0.0.0.0/0 dev eno1
# ip route delete 192.168.0.1/32 dev eno1

# end file : /sbin/nat.sh
#########################################################################
