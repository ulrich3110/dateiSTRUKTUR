#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ds_test_dateiinfo.py - [d]atei[s]strukturen Test Funktionen
Copyright (c) Januar 2022: Andreas Ulrich
<http://erasand.ch>, <andreas@erasand.ch>

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


def f_formattext(tx_l, tx_r):
    '''
    Formatiert eine Tabelle mit einem linken und einem rechten
    Textteil. Gibt einen String zurück.
    - tx_links = linker Text
    - tx_rechts = rechter Text
    '''
    # Zeilenbreite linker Textteil
    in_links = 15
    # Linker Teil formatieren (1 Leerzeichen als Trennung)
    if len(tx_l) > in_links - 1:
        tx_l = tx_l[0:in_links - 1]
    tx_l = tx_l.ljust(in_links)
    tx_z = "{0}{1}".format(tx_l, tx_r)
    return(tx_z)


def f_fehlertext(in_anz, tx_test, tx_kontroll, tx_resultat):
    '''
    Gibt den Fehlertext aus, erhöht den Zähler und gibt den Zähler
    zurück
    - in_anz = Fehlerzähler
    - tx_test = Test Bezeichnung
    - tx_wert = Vorgabe Wert
    - tx_resultat = Testresultat
    '''
    # Formatierung
    tx_r = "{0}  |  {1} != {2}".format(
        tx_test,
        tx_kontroll,
        tx_resultat
    )
    print(f_formattext("FEHLER", tx_r))
    in_anz += 1
    return(in_anz)


def f_testfehlertext(in_anz, tx_test, tx_kontroll, tx_resultat):
    '''
    Gibt den Fehlertext zum testen des Scripts aus, erhöht den Zähler
    und gibt den Zähler zurück
    - in_anz = Fehlerzähler
    - tx_test = Test Bezeichnung
    - tx_wert = Vorgabe Wert
    - tx_resultat = Testresultat
    '''
    # Formatierung
    tx_r = "{0}  |  {1} != {2}".format(
        tx_test,
        tx_kontroll,
        tx_resultat
    )
    print(f_formattext("TESTFEHLER", tx_r))
    in_anz += 1
    return(in_anz)


def f_oktext(tx_test):
    '''
    Gibt den OK Text aus.
    - tx_test = Test Bezeichnung
    '''
    print(f_formattext("OK", tx_test))


def f_testtitel(tx_test):
    '''  Gibt den Test-Titel aus '''
    print()
    print(f_formattext("TEST", tx_test))


def f_vergleich(bl_modus, bl_test, in_anzerr, tx_test, tx_vorgabe,
                tx_resultat):
    '''
    Prüfen ob die Bedingung erfüllt ist
    - bl_modus = Produktive Tests (True) oder Test-Entwicklung (False)
    - in_anzerr = Anzahl bisherige Fehler
    - tx_test = Test Bezeichnung
    - tx_vorgabe = Vorgabe Wert als Text
    - tx_resultat = Test-Resultat als Text
    Rückgabe der Anzahl Fehler
    '''
    if bl_modus:
        # Produktiver Test Modus
        if not bl_test:
            # Fehlermeldung
            tx_r = "{0} |{1}| <> |{2}|".format(tx_test, tx_vorgabe,
                                               tx_resultat)
            print(f_formattext("FEHLER", tx_r))
            in_anzerr += 1
        else:
            # OK Meldung
            print(f_formattext("OK", tx_test))
    else:
        # Entwicklung Test-Script
        tx_r = "{0} |{1}| <> |{2}|".format(tx_test, tx_vorgabe,
                                           tx_resultat)
        print(f_formattext("TESTFEHLER", tx_r))
        in_anzerr += 1
    # Rückgabe Anzahl Fehler
    return(in_anzerr)
