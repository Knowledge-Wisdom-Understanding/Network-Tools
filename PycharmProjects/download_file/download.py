#!/usr/bin/env python

import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download(
    "https://www.nissanusa.com/content/dam/Nissan/us/vehicles/gtr/r35/2_minor_change/overview/18tdi-gtrhelios104.jpg.ximg.l_full_m.smart.jpg"
)
