#! /usr/bin/env python3
# coding: utf-8

class MyIterator:
    def __init__(self):
        print("Auto initialisation to 40")
        self.i = 40

    def __iter__(self):
        print("Call of __iter__")
        return self

    def __next__(self):
        print("Call of __next__")
        self.i += 2
        if self.i > 56 :
            raise StopIteration()
        return self.i


def main():
    for i in MyIterator():
        print(i)


if __name__ == "__main__":
    main()
