#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time

'''
dastalfn.py - dateiSTRUKTUR, Alle Etappen, Funktionsmodul
Copyright (c) Andreas Ulrich, <http://erasand.ch>, <andreas@erasand.ch>

LIZENZ
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

DEUTSCHE ÜBERSETZUNG: <http://www.gnu.de/documents/gpl-3.0.de.html>
'''


def f_loadjson(tx_pfad):
    '''
    Lädt eine JSON Datei und gibt diese zurück als Wörterbuch
    - tx_pfad = Pfad
    - dc_verz = Wörterbuch
    '''
    print("# f_loadjson #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # Json laden
    try:
        with open(tx_pfad) as ob_f:
            dc_verz = json.load(ob_f)
    except Exception as ob_err:
        # Fehlermeldung ausgeben und leeres Wörterbuch erzeugen
        tx_t = "FEHLER -- PFAD: {0} -- ERROR: {1}".format(
            tx_pfad,
            str(ob_err)
        )
        print("#", tx_t, "#")
        dc_verz = {}
    return(dc_verz)


def f_savejson(tx_pfad, dc_verz):
    '''
    Speichert ein Wörterbuch als JSON Datei unter dem Pfad ab.
    - tx_pfad = Pfad
    - dc_verz = Wörterbuch
    '''
    print("# f_savejson #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # JSON speichern
    try:
        with open(tx_pfad, 'w', encoding='utf-8',
                  errors='ignore') as ob_jsonfile:
            json.dump(dc_verz, ob_jsonfile, indent=2, sort_keys=True)
    except Exception as ob_err:
        # Fehlermeldung ausgeben
        tx_t = "FEHLER -- PFAD: {0} -- ERROR: {1}".format(
            tx_pfad,
            str(ob_err)
        )
        print("#", tx_t, "#")
    return()


def f_savetext(tx_pfad, tx_text):
    '''
    Speichert einen Text unter dem Pfad ab.
    - tx_pfad = Pfad
    - tx_text = Text
    '''
    print("# f_savetext #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # Text speichern
    try:
        ob_datei = open(
            tx_pfad,
            'w',
            encoding='utf-8',
            errors='ignore'
        )
        ob_datei.write(tx_text)
        ob_datei.close()
    except Exception as ob_err:
        tx_t = "# FEHLER ## PFAD: {0} ## Error: {1} #".format(
            tx_pfad,
            str(ob_err)
        )
        tx_errpfad = "{0}___error.txt".format(tx_pfad)
        ob_errfile = open(tx_errpfad, 'w')
        ob_errfile.write(tx_t)
        ob_errfile.close()


def f_savecsv(tx_pfad, ls_tabelle):
    '''
    Speichert einen Liste als CSV unter dem Pfad ab.
    - tx_pfad = Pfad
    - ls_tabelle = Liste in Tabellenform:
      [
        ["Spaltentitel 1", "Spaltentitel 2"],
        [Wert Spale 1,     Wert Spalte 2],
      ]
    '''
    print("# f_savecsv #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # CSV speichern
    ob_datei = open(tx_pfad, 'w')
    with ob_datei:
        ob_writer = csv.writer(ob_datei)
        for ls_zeile in ls_tabelle:
            ob_writer.writerow(ls_zeile)


def f_listenvergleich(ls_a, ls_b):
    '''
    Liste A mit Liste B vergleichen. Rückgabe von 3 Listen:
    (ls_beide, ls_nur_a, ls_nur_b)
    ls_beide = In beiden Listen vorhandene Einträge
    ls_nur_a = Einträge nur in der Liste A vorhanden
    ls_nur_b = Einträge nur in der Liste B vorhanden
    '''
    print("# f_listenvergleich #")
    # Mengen aus Listen
    mn_a = set(ls_a)
    mn_b = set(ls_b)
    # Schnittmenge (gemeinsame Elemente in beiden Mengen)
    mn_beide = mn_b.intersection(mn_a)
    # Nur in a vorhanden (Menge a - Menge b)
    mn_nur_a = mn_a.difference(mn_b)
    # Nur in b vorhanden (Menge b - Menge a)
    mn_nur_b = mn_b.difference(mn_a)
    # Sortierte Listen aus Mengen
    ls_beide = sorted(mn_beide)
    ls_nur_a = sorted(mn_nur_a)
    ls_nur_b = sorted(mn_nur_b)
    # Rückgabe der Listen
    return(ls_beide, ls_nur_a, ls_nur_b)


def f_testok(tx_test):
    ''' Gibt den Test OK Text aus '''
    print("## {0} >> OK ##".format(tx_test))


def f_testfehler(tx_test, vl_vorg, vl_resu):
    ''' Gibt den Test Fehler Text aus '''
    print("## {0} >> FEHLER ##".format(tx_test))
    if isinstance(vl_vorg, list):
        # Listen miteinander vergleichen
        ls_b, ls_nv, ls_nr = f_listenvergleich(vl_vorg, vl_resu)
        ls_nv.sort()
        ls_nr.sort()
        # Unterschiede darstellen
        print("## Nur in Vorgabe:  {0} ##".format(ls_nv))
        print("## Nur in Resultat: {0} ##".format(ls_nr))
    else:
        # Werte Unterschiede darstellen
        print("##   {0} --- {1} ##".format(vl_vorg, vl_resu))


def f_test_einzeln(tx_test, bl_test, vl_vorg, vl_resu, in_anzerr):
    ''' Einzeltest '''
    # print("##", tx_test.upper(), "##")
    if bl_test:
        f_testok(tx_test)
    else:
        f_testfehler(tx_test, vl_vorg, vl_resu)
        in_anzerr += 1
    print()
    return(in_anzerr)


def f_test_liste(tx_test, ls_vorg, ls_resu, in_anzerr):
    ''' Testet die Elemente 2'er Listen '''
    # print("##", tx_test.upper(), "##")
    for in_i in range(len(ls_vorg)):
        # Die Vorgabe-Liste und die Resultat-Liste müssen gleich viele
        # Elemente haben; die Element werden nach Indexen geprüft;
        bl_t = ls_resu[in_i] == ls_vorg[in_i]
        if bl_t:
            f_testok(tx_test)
        else:
            f_testfehler(tx_test, ls_resu[in_i], ls_vorg[in_i])
            in_anzerr += 1
    print()
    return(in_anzerr)
