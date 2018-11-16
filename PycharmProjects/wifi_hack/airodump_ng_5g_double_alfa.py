#!/usr/bin/env python

import subprocess as s

interface = "wlan0"

print("[+] Changing MAC address for " + interface + " to random MAC")

s.call("ifconfig " + interface + " down", shell=True)
s.call("macchanger -r " + interface, shell=True)

print("[+] Starting Monitor mode on " + interface)

s.call("ifconfig " + interface + " down", shell=True)
s.call("iwconfig wlan0 mode monitor", shell=True)
s.call("rfkill unblock wifi", shell=True)
s.call("rfkill unblock all", shell=True)
s.call("ifconfig wlan0 up", shell=True)
s.call("airodump-ng --band a wlan0", shell=True)
