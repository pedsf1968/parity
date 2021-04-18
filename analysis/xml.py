#! /usr/bin/env python3
# coding: utf-8

import os
import logging as log


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))

    path_to_file = os.path.join(directory, "data", data_file)
    try:
        with open(path_to_file, 'r') as f:
            preview = f.readline()
            log.debug("We manage to read the file! This is the preview: {}".format(preview))
    except FileNotFoundError as e:
        log.critical('No file found! This is the message : {}'.format(e))


def main():
    launch_analysis('SyceronBrut.xml')


if __name__ == "__main__":
    main()