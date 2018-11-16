#!/usr/bin/env python

import subprocess
import argparse
import re
import sys
import random

'''
   A MAC address changing script.
   Usage: python mac_changer.py -i "NetworkInterfaceHere" -m "NewMACHere"
   Help: python mac_changer.py --help
'''


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface for which MAC address should be changed")
    mutually_exclusive_options = parser.add_mutually_exclusive_group()
    mutually_exclusive_options.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    mutually_exclusive_options.add_argument("-r", "--random", dest="random", action="store_true",
                                            help="Generate a random MAC address")
    mutually_exclusive_options.add_argument("-s", "--show", dest="show", action="store_true",
                                            help="Print current MAC address and exit")
    mutually_exclusive_options.add_argument("-p", "--permanent", action="store_true",
                                            help="Reset MAC address back to permanent")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif options.new_mac == "":
        parser.error("[-] Please specify a MAC address, use --help for more info.")
    return options


def get_permanent_mac(interface):
    ethtool_result = subprocess.check_output(["ethtool", "-P", interface])
    permanent_mac_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ethtool_result)

    if permanent_mac_search_result:
        return permanent_mac_search_result.group(0)
    else:
        print("[-] Could not fetch permanent MAC address for " + interface)
        sys.exit()


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not fetch MAC address for " + interface)
        sys.exit()


def create_random_mac():
    random_mac = [0x00, 0x16, 0x3e,
                  random.randint(0x00, 0x7f),
                  random.randint(0x00, 0xff),
                  random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, random_mac))


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def check_change_mac(interface, mac_before):
    current_mac = get_current_mac(interface)
    if current_mac == mac_before:
        print("[+] MAC was successfully changed to " + current_mac)
        return True
    else:
        print("[-] MAC was not changed.")
        return False


def print_permanent_and_current_macs(interface):
    print("Permanent MAC address:\t" + get_permanent_mac(interface))
    print("Current MAC address:\t" + get_current_mac(interface))


def process_change(interface, new_mac):
    change_mac(interface, new_mac)
    current_mac = get_current_mac(interface)
    check_change_mac(interface, current_mac)


if __name__ == "__main__":
    options = get_arguments()
    PERMANENT = get_permanent_mac(options.interface)
    current_mac = get_current_mac(options.interface)

    if options.show:
        print_permanent_and_current_macs(options.interface)

    elif options.permanent:
        print_permanent_and_current_macs(options.interface)
        process_change(options.interface, PERMANENT)

    elif options.new_mac:
        print_permanent_and_current_macs(options.interface)
        process_change(options.interface, options.new_mac)

    elif options.random:
        print_permanent_and_current_macs(options.interface)
        random_mac = create_random_mac()
        process_change(options.interface, random_mac)