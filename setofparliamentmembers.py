#! /usr/bin/env python3
# coding: utf-8

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        # seperate women and men in two dataframes
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

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
            autopct="%1.1f pourcents"
        )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        # select all distinct values for feild parti_ratt_financier
        # remove null with dropna()
        all_parties = data["parti_ratt_financier"].dropna().unique()

        # for each party of the list
        for party in all_parties:
            # select all tuples with party_ratt_financier equal to the selected party
            data_subset = data[data.party_ratt_financier == party]
            # create group with the name MPs from party + party
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            # add members to dataframe
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result

    def launch_analysis(data_file, by_party = False):
        sopm = SetOfParliamentMembers("All MPs")
        sopm.data_from_csv(os.path.join("data",data_file))
        sopm.display_chart()

        if by_party:
            for party, s in sopm.split_by_political_party().items():
                s.display_chart()

