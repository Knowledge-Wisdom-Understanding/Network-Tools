#!/usr/bin/env python

import subprocess

interface = "wlan0"

print("[+] Changing MAC address for " + interface + " to random MAC")

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("macchanger -r " + interface, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)