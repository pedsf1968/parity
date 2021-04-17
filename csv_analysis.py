#! /usr/bin/env python3
# coding: utf-8

import os


def launch_analysis(data_file):
    directory = os.path.dirname(__file__)
    
    path_to_file = os.path.join(directory, "data", data_file)
    with open(path_to_file, 'r') as f:
        preview = f.readline()

    print("We manage to read the file! This is the preview: {}".format(preview))


def main():
    launch_analysis('current_mps.csv')


if __name__ == "__main__":
    main()
