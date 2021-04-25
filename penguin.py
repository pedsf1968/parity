#! /usr/bin/env python3
# coding: utf-8

class Penguins:
    TOTAL = 2

    def trace(func):
        def inner(*args, **kwargs):
            print("Nombre de manchots:{}".format(args[0].TOTAL))
            return func(*args, **kwargs)

        return inner

    @classmethod
    def total(self):
        return self.TOTAL

    @trace
    def add(self):
        self.TOTAL += 1

    @trace
    def remove(self):
        self.TOTAL -= 1


if __name__ == "__main__":
    p = Penguins()
    p.add()
    p.remove()
    print(Penguins.total())
