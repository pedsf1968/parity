#! /usr/bin/env python3
# coding: utf-8

import argparse
import logging as log

import analysis.csv as c_an
import analysis.xml as x_an

HELP_EXTENTION = "Specify the type of file to analyse. CSV or XML?"
HELP_DATAFILE = "Specify the name of the file to be analysed."
HELP_BYPARTY = "Display a chart for each party."
HELP_SEARCH_BY_NAME = "Get parlementary member by his name."
HELP_SEARCH_BY_INDEX = "Get parlementary member by his index."
HELP_DISPLAY_NAME = "Displays the names of all the mps."
HELP_N_FIRST_GROUP = "Get the list of N first groups."
HELP_INFO = "Display file information."
HELP_VERBOSE = "Specify to run the program in DEBUG level. "


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--extention", help=HELP_EXTENTION)
    parser.add_argument("-d", "--datafile", help=HELP_DATAFILE)
    parser.add_argument("-s", "--searchname", help=HELP_SEARCH_BY_NAME)
    parser.add_argument("-I", "--index", help=HELP_SEARCH_BY_INDEX)
    parser.add_argument("-g", "--groupfirst", help=HELP_N_FIRST_GROUP)

    parser.add_argument("-p", "--byparty", action='store_true', help=HELP_BYPARTY)
    parser.add_argument("-n", "--displaynames", action='store_true', help=HELP_DISPLAY_NAME)
    parser.add_argument("-i", "--info", action='store_true', help=HELP_INFO)
    parser.add_argument("-v", "--verbose", action='store_true', help=HELP_VERBOSE)

    return parser.parse_args()


def main():
    args = parse_arguments()

    try:
        datafile = args.datafile
        if datafile is None:
            raise Warning('No data file specified !')
    except Warning as e:
        log.warning(e)
    else:
        if args.verbose:
            log.basicConfig(level=log.DEBUG)
        else:
            log.basicConfig(level=log.WARNING)

        if args.extention == 'csv':
            c_an.launch_analysis(datafile, args.byparty, args.info, args.displaynames,
                                 args.searchname, args.index, args.groupfirst)
        elif args.extention == 'xml':
            x_an.launch_analysis(datafile)
    finally:
        log.info('Analysis is done')


if __name__ == "__main__":
    main()
