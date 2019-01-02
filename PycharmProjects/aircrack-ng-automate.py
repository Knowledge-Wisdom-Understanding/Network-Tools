#!/usr/bin/env python

import subprocess as s
from pynput.keyboard import Key, Controller
import time
from termcolor import colored

keyboard = Controller()
aircrack = "aircrack-ng"
rockyou = "/usr/share/wordlist/rockyou.txt"
open_wall = "/usr/share/seclists/Passwords/bt4-password.txt"
common_creds = "/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
bt4 = "/usr/share/seclists/Passwords/bt4-password.txt"

pcap_in = raw_input("Please enter the path to your pcap file: ")
print(colored('[+] ', 'green'), colored('Starting Aircrack-ng !', 'blue'))

try:
    s.call("airmon-ng " + pcap_in + " -w " + rockyou, shell=True)
    time.sleep(2)
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press('r')
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release('r')
    time.sleep(2)
    s.call("airmon-ng " + pcap_in + " -w " + open_wall, shell=True)
    time.sleep(2)
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press('d')
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release('d')
    time.sleep(2)
    s.call("airmon-ng " + pcap_in + " -w " + common_creds, shell=True)
    time.sleep(2)
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press('r')
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release('r')
    time.sleep(2)
    s.call("airmon-ng " + pcap_in + " -w " + bt4, shell=True)
    time.sleep(2)

except IOError:
    print('\n File not found.')
    quit()
