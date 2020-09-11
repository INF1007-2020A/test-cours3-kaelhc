#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
   for x in nom:
    if ord(nom[0])>=97 and ord(nom[0])<=122 :
        aski=ord(nom[0]) -32
    elif ord(nom[x])>=65 and ord(nom[x])<=90 :
        aski2=ord(nom[x])+32
    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
