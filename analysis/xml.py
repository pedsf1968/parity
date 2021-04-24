#! /usr/bin/env python3
# coding: utf-8

import os
import logging as log


def launch_analysis(data_file):
    path_to_file = os.path.join("data", data_file)

    file_name = os.path.basename(path_to_file)
    directory = os.path.dirname(path_to_file)
    log.info("Opening data file {} from directory '{}'".format(file_name, directory))

    try:
        with open(path_to_file, 'r') as f:
            preview = f.readline()
            log.debug("We manage to read the file! This is the preview: {}".format(preview))
    except FileNotFoundError as e:
        log.critical("No file found! This is the message : {%s}" % e)
    except:
        log.critical('Destination unknown !')


if __name__ == "__main__":
    launch_analysis('SyceronBrut.xml')