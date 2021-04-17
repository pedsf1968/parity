#! /usr/bin/env python3
# coding: utf-8

import argparse

# Import des modules
import analysis.csv as c_an
import analysis.xml as x_an


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extention", help="""Specify the type of file to analyse. CSV or XML? """)
    parser.add_argument("-d", "--datafile", help="""Specify the name of the file to be analysed. """)
    return parser.parse_args()


def main():
    args = parse_arguments()
    datafile = args.datafile

    if args.extention == 'csv':
        c_an.launch_analysis(datafile)
    elif args.extention == 'xml':
        x_an.launch_analysis(datafile)


if __name__ == "__main__":
    main()
