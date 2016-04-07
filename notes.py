#!/usr/bin/env python
# -*- coding: utf-8 -*-

odgovor = 'da'
seznam = []

while odgovor != 'ne':
    odgovor = raw_input("Ali želiš dodati kakšen izdelek na seznam? ")
    if odgovor == 'da':
        seznam.append(raw_input("Prosim napiši izdelek ki ga želiš dodati: "))
        print("Seznam: %s" % seznam )
    elif odgovor == 'ne':
        print("Kupiti moraš: \n")
        for izdelek in seznam:
            print izdelek
        break
    else:
        print('Prosim odgovori z "da" ali "ne"!')

print'\nVeselo nakupuj!'