#! /usr/bin/env python3
# coding: utf-8

import os
import pprint
import logging as log
import datetime as dt

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_DIRECTORY = "data"
AGE_COLUMN_NAME = "age"  # Name of the new column (containing the age of the MP)
AGE_YEARS_COLUMN_NAME = "age_in_years"
BIRTH_COLUMN_NAME = "birth"
MINIMUM_MP_AGE = 18

FIELD_PARTY = "parti_ratt_financier"
FIELD_NAME = "nom"
FIELD_LASTNAME = "nom_de_famille"

SEXE_FEMALE = "F"
SEXE_MALE = "H"


class SetOfParliamentMembers:
    ALL_REGISTERED_PARTIES = []  # This is a class attribute

    def __init__(self, name):
        self.name = name

    def total_mps(self):
        return len(self.dataframe)

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        # separate women and men in two dataframes
        female_mps = data[data.sexe == SEXE_FEMALE]
        male_mps = data[data.sexe == SEXE_MALE]

        # calculate the percents
        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()

        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
            proportions,
            labels=labels,
            autopct="%1.1f percents"
        )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        # select all distinct values for field parti_ratt_financier
        # remove null with dropna()
        all_parties = data[FIELD_PARTY].dropna().unique()

        # for each party of the list
        for party in all_parties:
            log.info("Curent party : {}".format(party))
            data_subset = data[data[FIELD_PARTY] == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            log.info("subset : {}".format(subset))
            result[party] = subset

        return result

    def __repr__(self):
        return "SetOfParliamentMembers : {}".format(len(self.dataframe))

    def __len__(self):
        return self.number_of_mps

    def __contains__(self, name):
        return name in self.dataframe[FIELD_LASTNAME].values

    def __getitem__(self, index):

        if index < 0:
            raise Exception("An index can't be negative!")
        elif index >= len(self.dataframe):
            raise Exception("There are only {} MPs!".format(len(self.dataframe)))

        try:
            result = dict(self.dataframe.iloc[index])
        except:
            raise Exception("Wrong Index")

        return result

    def __add__(self, other):
        if not isinstance(other, SetOfParliamentMembers):
            raise Exception("Can not add a SetOfParliamentMember with an object of type {}".format(type(other)))

        df1, df2 = self.dataframe, other.dataframe
        df = df1.append(df2)
        df = df.drop_duplicates()

        s = SetOfParliamentMembers("{} - {}".format(self.name, other.name))
        s.data_from_dataframe(df)
        return s

    def __radd__(self, other):
        if not isinstance(self, type(other)):
            raise Exception("Can not add a SetOfParliamentMember to the object of type {}".format(type(other)))

        df1 = self.dataframe
        df = df1.append(other.dataframe)
        df = df.drop_duplicates()

        s = SetOfParliamentMembers("{} - {}".format(other.name, self.name))
        s.data_from_dataframe(df)
        return s

    def __lt__(self, other):
        return self.number_of_mps < other.number_of_mps

    def __gt__(self, other):
        return self.number_of_mps > other.number_of_mps

    # The following 2 methods are a way to simulate a calculated attribute
    # (attribute 'number_of_mps' is calculated from attribute 'seld.dataframe')
    # There is a much better way to do it, using decorator '@property'
    def __getattr__(self, attr):
        if attr == "number_of_mps":  #todo: faire la version avec @property
            return len(self.dataframe)

    def __setattr__(self, attr, value):
        if attr == "number_of_mps":
            raise Exception("You can not set the number of MPs!")
        self.__dict__[attr] = value  # todo: c'est l'occasion de parler de __dict__ dans le cours ;)


def launch_analysis(data_file, by_party=False, info=False, displaynames=False,
                    searchname=None, index=None, groupfirst=None):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join(DATA_DIRECTORY, data_file))

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()
    else:
        sopm.display_chart()

    if info:
        log.info(sopm.number_of_mps)
        print()
        print(repr(sopm.total_mps()))

    if displaynames:
        log.info("Display names")
        print()
        print(repr(sopm.dataframe[FIELD_NAME]))

    if searchname is not None:
        log.info("searchname : {}".format(searchname))
        is_present = searchname in sopm
        print()
        print("Testing if {} is present: {}".format(searchname, is_present))

    if index is not None:
        index = int(index)
        log.info("index : {}".format(index))
        print()
        pprint.pprint(sopm[index])  # prints the dict a nice way

    if groupfirst is not None:
        groupfirst = int(groupfirst)
        log.info("groupfirst : {}".format(groupfirst))
        parties = sopm.split_by_political_party()
        parties = parties.values()
        parties_by_size = sorted(parties, reverse=True)

        print()
        print("Info: the {} biggest groups are :".format(groupfirst))
        for p in parties_by_size[0:groupfirst]:
            print(p.name)

        s = sum(parties_by_size[0:groupfirst])

        s.display_chart()


if __name__ == "__main__":
    launch_analysis('current_mps.csv')
