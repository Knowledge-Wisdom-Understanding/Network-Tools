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

    pbar = progressbar.ProgressBar(widgets=widgets, maxval=500).start()

    downloaded_size = bitmath.Byte(0)
    for filesize in range(len(path)):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())
        downloaded_size += filesize
        pbar.update(int(downloaded_size))

    pbar.finish()


my_file = '/root/Downloads/passwords.list'
download(my_file)
