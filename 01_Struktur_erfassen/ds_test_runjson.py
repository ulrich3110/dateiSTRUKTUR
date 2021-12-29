#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_erfassen import *

'''
ds_test_dateiinfo.py - [d]atei[s]strukturen <RunJson> Test
Copyright (c) Dezember 2021: Andreas Ulrich
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
    in_links = 12
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


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    print("DS_TEST_RUNJSON")
    print("---------------")
    print("Objekt:     RunJson")
    print("Methoden:   __init__(), m_reset_befehle(), m_load(),")
    print("            m_run()")
    print("Attribute:  dc_befehle")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    '''
    OBJEKT erzeugen
    '''
    tx_test = "RunJson Objekt erzeugen"
    f_testtitel(tx_test)
    ob_run = RunJson()
    '''
    __STR__ testen
    '''
    tx_test = "RunJson.__str__()"
    f_testtitel(tx_test)
    tx_r = ob_run.__str__()
    # Vergleich
    if bl_modus:
        # Produktiver Test Modus
        if not tx_r:
            in_anzerr = f_fehlertext(in_anzerr, tx_test,
                                     "<test>", tx_r)
        else:
            f_oktext(tx_test)
    else:
        # Dieses Script testen
        in_anzerr = f_testfehlertext(in_anzerr, tx_test,
                                     "<test>", tx_r)
    '''
    RESET testen
    '''
    tx_test = "RunJson.m_reset_befehle()"
    f_testtitel(tx_test)
    ob_run.m_reset_befehle()
    bl_r = ob_run.dc_befehle["TESTMODUS"]
    ls_r = ob_run.dc_befehle["BEFEHLE"]
    # Vergleich
    if bl_modus:
        # Produktiver Test Modus
        if bl_r or not isinstance(ls_r, list):
            # Kontrollwerte und Resulatwerte als Text
            tx_k = "{0}, {1}".format(str(False), str(type([])))
            tx_r = "{0}, {1}".format(str(bl_r), str(type(ls_r)))
            in_anzerr = f_fehlertext(in_anzerr, tx_test, tx_k, tx_r)
        else:
            f_oktext(tx_test)
    else:
        # Dieses Script testen, Kontrollwerte und Resulatwerte als Text
        tx_k = "{0}, {1}".format(str(False), str(type([])))
        tx_r = "{0}, {1}".format(str(bl_r), str(type(ls_r)))
        in_anzerr = f_testfehlertext(in_anzerr, tx_test, tx_k, tx_r)
    '''
    LADEN testen
    '''
    tx_test = "RunJson.m_load()"
    f_testtitel(tx_test)
    ob_run.m_load()
    bl_r = ob_run.dc_befehle["TESTMODUS"]
    ls_r = ob_run.dc_befehle["BEFEHLE"]
    # Vergleich
    if bl_modus:
        # Produktiver Test Modus
        if bl_r or not isinstance(ls_r, list):
            # Kontrollwerte und Resulatwerte als Text
            tx_k = "{0}, {1}".format(str(False), str(type([])))
            tx_r = "{0}, {1}".format(str(bl_r), str(type(ls_r)))
            in_anzerr = f_fehlertext(in_anzerr, tx_test, tx_k, tx_r)
        else:
            f_oktext(tx_test)
    else:
        # Dieses Script testen, Kontrollwerte und Resulatwerte als Text
        tx_k = "{0}, {1}".format(str(False), str(type([])))
        tx_r = "{0}, {1}".format(str(bl_r), str(type(ls_r)))
        in_anzerr = f_testfehlertext(in_anzerr, tx_test, tx_k, tx_r)
    '''
    RUN testen
    '''
    tx_test = "RunJson.m_load()"
    f_testtitel(tx_test)
    ob_run.m_run()
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
