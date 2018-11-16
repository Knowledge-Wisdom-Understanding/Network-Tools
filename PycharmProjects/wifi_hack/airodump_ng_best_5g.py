#!/usr/bin/env python

import subprocess as s

interface = "wlan0"
airmon_interface = "wlan0mon"

print("[+] Changing MAC address for " + interface + " to random MAC")

s.call("ifconfig " + interface + " down", shell=True)
s.call("macchanger -r " + interface, shell=True)

print("[+] Starting Monitor mode on " + interface)

s.call("airmon-ng check kill", shell=True)
s.call("airmon-ng start " + interface, shell=True)
s.call("ifconfig " + airmon_interface, shell=True)
s.call("iwconfig " + airmon_interface, shell=True)
s.call("airodump-ng --band a " + airmon_interface, shell=True)
