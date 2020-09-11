#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
   for x in nom:
    if ord(nom[0])>=97 and ord(chaine_1[0])<=122 :
        aski=ord(chaine_1[0]) -32
    elif ord(chaine_1[x])>=65 and ord(chaine_1[x])<=90 :
        aski2=ord(chaine_1[x])+32
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
