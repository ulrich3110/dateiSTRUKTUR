#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_erfassen import *

'''
ds_test_dateiinfo.py - [d]atei[s]strukturen <DateiInfo> Test
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
    print("DS_TEST_DATEIINFO")
    print("-----------------")
    print("Objekt:     DateiInfo")
    print("Methoden:   __init__(), __str__(), m_clear(), m_get_dc(),")
    print("            m_set_dc(<dict>)")
    print("Attribute:  tx_name, tx_typ, tx_datum, in_groesse")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    '''
    OBJEKT erzeugen
    '''
    tx_test = "DateiInfo Objekt erzeugen"
    f_testtitel(tx_test)
    ob_datinf = DateiInfo()
    '''
    __STR__ testen
    '''
    tx_test = "DateiInfo.__str__()"
    f_testtitel(tx_test)
    tx_r = ob_datinf.__str__()
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
    SET WÖRTERBUCH testen
    '''
    tx_test = "DateiInfo.m_set_dc(<dict>)"
    f_testtitel(tx_test)
    # Testliste definieren, [[Schlüssel, Wert]
    ls_testdaten = [
        ["NAME", "Test_Datei"],
        ["TYP", ".txt"],
        ["DATUM", "21.12.2021 23:11:00"],
        ["GROESSE", 64]
    ]
    # Test Wörterbuch
    dc_daten = {}
    for ls_t in ls_testdaten:
        dc_daten[ls_t[0]] = ls_t[1]
    # Wörterbuch setzen
    ob_datinf.m_set_dc(dc_daten)
    '''
    GET WÖRTERBUCH testen
    '''
    tx_test = "DateiInfo.m_get_dc()"
    f_testtitel(tx_test)
    dc_daten = ob_datinf.m_get_dc()
    # Daten testen mit Schlüssel und Soll Resultat
    for ls_t in ls_testdaten:
        tx_k, vl_w = ls_t
        tx_test = "Schlüssel: '{0}'".format(tx_k)
        # Vergleich
        if bl_modus:
            # Produktiver Testmodus
            if dc_daten[tx_k] != vl_w:
                in_anzerr = f_fehlertext(in_anzerr, tx_test, str(vl_w),
                                         str(dc_daten[tx_k]))
            else:
                f_oktext(tx_test)
        else:
            # Dieses Script testen
            in_anzerr = f_testfehlertext(in_anzerr, tx_test, str(vl_w),
                                         str(dc_daten[tx_k]))
    '''
    CLEAR testen
    '''
    tx_test = "DateiInfo.m_clear()"
    f_testtitel(tx_test)
    ob_datinf.m_clear()
    '''
    Werte direkt eintragen
    '''
    tx_test = "Werte direkt eintragen"
    f_testtitel(tx_test)
    # Testliste definieren, [[Testbezeichnung, Wert]
    ls_testdaten = [
        ["DateiInfo.tx_name", "Test_2"],
        ["DateiInfo.tx_typ", ".tx$"],
        ["DateiInfo.tx_datum", "23.12.2021 13:28:00"],
        ["DateiInfo.tx_groesse", 32]
    ]
    ob_datinf.tx_name = ls_testdaten[0][1]
    ob_datinf.tx_typ = ls_testdaten[1][1]
    ob_datinf.tx_datum = ls_testdaten[2][1]
    ob_datinf.tx_groesse = ls_testdaten[3][1]
    '''
    Werte direkt abfragen
    '''
    tx_test = "Werte direkt abfragen"
    f_testtitel(tx_test)
    for ls_t in ls_testdaten:
        tx_t, vl_w = ls_t
        if tx_t.endswith(".tx_name"):
            vl_r = ob_datinf.tx_name
        elif tx_t.endswith(".tx_typ"):
            vl_r = ob_datinf.tx_typ
        elif tx_t.endswith(".tx_datum"):
            vl_r = ob_datinf.tx_datum
        elif tx_t.endswith(".tx_groesse"):
            vl_r = ob_datinf.tx_groesse
        # Vergleich
        tx_test = "Attribut: {0}".format(tx_t)
        if bl_modus:
            # Produktiver Test Modus
            if vl_w != vl_r:
                in_anzerr = f_fehlertext(in_anzerr, tx_test, str(vl_w),
                                         str(vl_r))
            else:
                f_oktext(tx_test)
        else:
            # Dieses Script testen
            in_anzerr = f_testfehlertext(in_anzerr, tx_test, str(vl_w),
                                         str(vl_r))
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
