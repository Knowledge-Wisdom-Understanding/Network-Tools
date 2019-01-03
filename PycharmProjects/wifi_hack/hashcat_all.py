#!/usr/bin/env python

import subprocess as s


top4800 = "/usr/share/seclists/Passwords/WiFi-WPA/probable-v2-wpa-top4800.txt"
bt4 = "/usr/share/seclists/Passwords/bt4-password.txt"
common_creds = "/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
dark_c0de = "/usr/share/seclists/Passwords/darkc0de.txt"
dark_web = "/usr/share/seclists/Passwords/darkweb2017-top10000.txt"
fasttrack = "/usr/share/wordlists/fasttrack.txt"
fern = "/usr/share/wordlists/fern-wifi/common.txt"
metasploit_burnett = "/usr/share/wordlists/metasploit/burnett_top_1024.txt"
metasploit_password = "/usr/share/wordlists/metasploit/password.lst"
most_popular = "/usr/share/seclists/Passwords/Most-Popular-Letter-Passes.txt"
open_wall = "/usr/share/seclists/Passwords/openwall.net-all.txt"
probable = "/usr/share/seclists/Passwords/probable-v2-top12000.txt"
rockyou = "/usr/share/wordlists/rockyou.txt"



wordlists = [top4800, bt4, common_creds, dark_c0de, dark_web, fasttrack, fern, metasploit_burnett, metasploit_password, most_popular, open_wall, probable, rockyou]

pmkid_in = raw_input("Please enter the path to your pmkid file: ")

for i in wordlists:
    try:
        s.call("hashcat -m 16800 -a 0 -w 3 --status " + pmkid_in + " " + i + " --force", shell=True)
    except IOError:
        print('\n File not found.')
        quit()
