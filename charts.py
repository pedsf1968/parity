#! /usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt


def simple_circle_chart():
    fig, ax = plt.subplots()
    ax.pie([24, 18], labels=["Womens", "Mens"])
    plt.show()


def simple_histo_chart():
    ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
       25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

    fig, ax = plt.subplots()
    ax.hist(ages)
    plt.show()


def design_circle_chart():
    fig, ax = plt.subplots()
    ax.pie([24, 18],
           labels=["Womens", "Mens"],
           autopct="%1.1f pourcents")
    plt.title("Sample of Men / Women proportions")
    plt.show()


def main():
    simple_circle_chart()
    simple_histo_chart()
    design_circle_chart()


if __name__ == "__main__":
    main()
