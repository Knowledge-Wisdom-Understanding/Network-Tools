#!/usr/bin/env python

import progressbar
import base64
import bitmath


def download(path):
    widgets = [
        '[Downloading File:   ] ',
        progressbar.Percentage(),
        ' ',
        progressbar.Bar(marker=u'\u2588', left='[', right=']'),
        ' ',
        progressbar.ETA(),
        ' ',
        progressbar.FileTransferSpeed(),
    ]

    pbar = progressbar.ProgressBar(widgets=widgets, maxval=1000000000).start()

    downloaded_size = bitmath.Byte(0)

    with open(path, 'rb') as file:
        for filebit in file:
            downloaded_size += filebit
            pbar.update(int(downloaded_size))
            pbar.finish()

        return base64.b64encode(file.read())


my_file = '/root/Downloads/netgear.txt'
download(my_file)
