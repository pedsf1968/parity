#! /usr/bin/env python3
# coding: utf-8

import os
import logging as log
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

log.basicConfig(level=log.DEBUG)

# create a list (legs, hair, tail, belly)
un_panda = [100, 5, 20, 80]

# create a list of lists
famille_panda = [
    [100, 5, 20, 80],  # mum
    [50, 2.5, 10, 40],  # bay
    [110, 6, 22, 80],  # dad
]


def single_list():
    # transform list in array
    un_panda_numpy = np.array(un_panda)
    print("One list : \n{}\n".format(un_panda))
    print("One Array : \n{}\n".format(un_panda_numpy))
    # can divide array
    print("Half of the Array : \n{}\n".format(un_panda_numpy / 2))


def list_of_lists():
    print("One list of lists : \n{}\n".format(famille_panda))
    # transform list of list in array
    famille_panda_numpy = np.array(famille_panda)
    print("One Array : \n{}\n".format(famille_panda_numpy))
    # access to baby data
    print("Dad element of the Array : \n{}\n".format(famille_panda_numpy[2]))
    print("Dad legs size : \n{}\n".format(famille_panda_numpy[2][0]))
    print("Dad legs size with numpy method : \n{}\n".format(famille_panda_numpy[2, 0]))
    print("All legs size : \n{}\n".format(famille_panda_numpy[:, 0]))


def array_operations():
    famille_panda_numpy = np.array(famille_panda)
    print("One Array : \n{}\n".format(famille_panda_numpy))
    famille_panda_numpy_df = pd.DataFrame(famille_panda_numpy,
                                          index=['mum', 'baby', 'dad'],
                                          columns=['legs', 'hair', 'tail', 'belly'])
    print("One pandas DataFrame : \n{}\n".format(famille_panda_numpy_df))

    # Different way to access a column
    print("Legs column by name with point notation : \n{}\n".format(famille_panda_numpy_df.legs))
    print("Legs column by name with quotes and braquet : \n{}\n".format(famille_panda_numpy_df["legs"]))

    # Get tuples in itération with for
    for line in famille_panda_numpy_df.iterrows():
        line_index = line[0]
        line_content = line[1]
        print("This is the panda %s :" % line_index)
        print(line_content)
        print("\n")

    # Access one tupple by is index
    print("Dad panda by is index : \n{}\n".format(famille_panda_numpy_df.iloc[2]))
    # Access one tupple by is line name
    print("Dad panda by is line name : \n{}\n".format(famille_panda_numpy_df.loc["dad"]))

    test_result = famille_panda_numpy_df["belly"] == 80
    print("Result of test :\n{}\n".format(test_result))
    panda_80 = famille_panda_numpy_df[test_result]
    print("Result of filter :\n{}\n".format(panda_80))
    # Reverse filter with ~
    panda_not_80 = famille_panda_numpy_df[~test_result]
    print("Result of reverse filter ~ :\n{}\n".format(panda_not_80))

    others_pandas = pd.DataFrame([[105,4,19,80],[100,5,20,80]], columns= famille_panda_numpy_df.columns)
    all_pandas = famille_panda_numpy_df.append(others_pandas)
    print("All pandas :\n{}\n".format(all_pandas))
    print("All pandas with no duplicates :\n{}\n".format(all_pandas.drop_duplicates()))


def csv_operations():
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "parity", "data", "current_mps.csv")

    try:
        with open(path_to_file, 'r') as f:
            mps = pd.read_csv(path_to_file, sep=";")
            print(mps.iloc[0])

    except FileNotFoundError as e:
        log.critical('No file found! This is the message : {}'.format(e))


def main():
    single_list()
    list_of_lists()
    array_operations()
    csv_operations()


if __name__ == "__main__":
    main()
