#! /usr/bin/env python3
# coding: utf-8


def generator(beginning, end):
    print("    On commence !")

    cpt = beginning
    while cpt <= end:
        if cpt % 2 == 0:
            print("    On s'arrete au yield")
            yield float(cpt)
            print("    On reprend après le yield")
        else:
            print("    On s'arrete au yield")
            yield str(cpt)
            print("    On reprend après le yield")
        cpt += 1
    yield "C'est bientôt la fin"
    yield "C'est VRAIMENT bientôt la fin"
    yield "Là c'est la fin"


def main():
    for i in generator(4,8):
        print(i)


if __name__ == "__main__":
    main()
