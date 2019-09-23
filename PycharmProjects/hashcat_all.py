from subprocess import Popen, PIPE, call
import os
import argparse
import sys
import time
import signal
from sty import fg, bg, ef, rs
import platform

# This script is intended for windows and hasn't been ported to a linux
# compatible version yet.
# Also, THis script uses hashid. So make sure if you don't have it installed to do,
# python3 -m pip install hashid     or depending on python path in windows,
# py -m pip install hashid      # etc... etc..
if os.name == "nt" and platform.release() == "10" and platform.version() >= "10.0.14393":
    # Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

path_to_wordlist_folder = os.path.normpath("D:/Wordlists/Found-Lists")
path_to_hashcat_folder = os.path.normpath("C:/Users/USERNAME/Downloads/hashcat-5.1.0")
cmd_info = "[" + fg.li_magenta + "+" + fg.rs + "]"
purp = fg.li_magenta
reset = fg.rs
cwd = os.getcwd()

intervals = (
    ("weeks", 604800),  # 60 * 60 * 24 * 7
    ("days", 86400),  # 60 * 60 * 24
    ("hours", 3600),  # 60 * 60
    ("minutes", 60),
    ("seconds", 1),
)


def display_time(seconds, granularity=2):
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append(f"{value} {name}")
    return ", ".join(result[:granularity])


def signal_handler(sig, frame):
    print(" ")
    print(f"{purp}See you Space Cowboy...{reset}")
    sys.exit(0)


def main():
    startTimer = time.time()
    parser = argparse.ArgumentParser(
        conflict_handler="resolve",
        description="Runs hashcat on a supplied hashfile with all wordlists in the supplied directory",
        usage="python3 hashcat_run_all.py -t 0 -w C:/Users/Username/Path/To/Wordlists -e C:/Users/Username/Path-to-hashcat.exe -H C:/Users/Username/Path-to-target-Hash.txt",
    )
    parser.add_argument("-w", "--wordlists", help="Path to wordlists folder")
    parser.add_argument("-e", "--executable", help="Path to Hashcat executable folder")
    parser.add_argument("-f", "--filehash", help="Path to target hash to try and crack", nargs="+")
    parser.add_argument("-t", "--type", help="Type of hash for hashcat -m argument. Ex. -t 500")
    args = parser.parse_args()
    if args.filehash:
        arg_hash = f"""\"{args.filehash[0]}\""""

    def getHash(fhash):
        try:
            counter = 0
            with open(fhash) as h:
                for line in h:
                    htype = line.rstrip()
                    counter += 1
                    if counter == 1:
                        break
            return htype
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            exit()

    def cmdline(command):
        process = Popen(args=command, stdout=PIPE, shell=True)
        return process.communicate()[0]

    def getHashMode(command):
        hashid_output = [i.strip() for i in cmdline(command).decode("utf-8").split("\n")]
        hash_id_filtered = [i.split() for i in hashid_output]
        hash_mode = [i[-1] for i in hash_id_filtered if "Mode:" in i]
        mode_num = [i.replace("]", "") for i in sorted(set(hash_mode))]
        return mode_num[0]

    def walker(wordlists):
        extensions = (".txt", ".lst")
        wordlist_files = [
            os.path.join(dirpath, wordlist)
            for dirpath, subdirs, files in os.walk(wordlists, topdown=False)
            for wordlist in files
            if wordlist.endswith(extensions)
        ]
        return wordlist_files

    def run_hashcat():
        try:
            hash_type = getHash(args.filehash[0])
            hashcat_mode = getHashMode(f"hashid -m {hash_type}")
            os.chdir(args.executable)
            for w in walker(args.wordlists):
                hashcat_cmd = (
                    f"hashcat64.exe -m {hashcat_mode} -a 0 -w 3 -O --status {arg_hash} {w}"
                )
                print(cmd_info, hashcat_cmd)
                call(hashcat_cmd, shell=True)
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            exit()

    def run_hashcat2():
        try:
            os.chdir(args.executable)
            for w in walker(args.wordlists):
                hashcat_cmd = f"hashcat64.exe -m {args.type} -a 0 -w 3 -O --status {arg_hash} {w}"
                print(cmd_info, hashcat_cmd)
                call(hashcat_cmd, shell=True)
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            exit()

    if (
        args.wordlists is None
        and (args.executable is None)
        and (args.filehash is None)
        and (args.type is None)
    ):
        print("Must supply a hash file")
        parser.print_help(sys.stderr)
    elif (
        args.wordlists is None
        and (args.executable is None)
        and args.filehash
        and (args.type is None)
    ):
        args.wordlists = path_to_wordlist_folder
        args.executable = path_to_hashcat_folder
        run_hashcat()
    elif args.wordlists and (args.executable is None) and args.filehash and (args.type is None):
        args.executable = path_to_hashcat_folder
        run_hashcat()
    elif args.wordlists and args.executable and args.filehash and (args.type is None):
        parser.print_help(sys.stderr)
        run_hashcat()
    elif args.wordlists is None and (args.executable is None) and args.filehash and args.type:
        args.wordlists = path_to_wordlist_folder
        args.executable = path_to_hashcat_folder
        run_hashcat2()
    else:
        parser.print_help(sys.stderr)

    end = time.time()
    time_elapsed = end - startTimer
    durationMSG = fg.cyan + f"All Scans Completed in: " + fg.rs
    print(durationMSG, display_time(time_elapsed))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
