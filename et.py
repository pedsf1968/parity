#! /usr/bin/env python3
# coding: utf-8

def decorator(func):
    def inner():
        return func()
    return inner


@decorator
def karadoc():
    print("Le gras c'est la vie.")


def e_t(func):
    def inner():
        print("Maison... Téléphone... Maison...")
        return func()
    return inner


def gertie():
    print("Je lui ai appris à parler ! Ecoute !")


@e_t
def elliott():
    print("Il veut rentrer chez lui !")


if __name__ == "__main__":
    gertie()
    elliott()
