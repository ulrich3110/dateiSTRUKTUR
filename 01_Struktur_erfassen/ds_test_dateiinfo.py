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


def f_fehlertext(in_anz, tx_titel, tx_test, tx_wert, tx_resultat):
    '''
    Gibt den Fehlertext aus, erhöht den Zähler und gibt den Zähler
    zurück
    in_anz = Fehlerzähler
    tx_titel = Titel
    tx_test = Test Bezeichnung
    tx_wert = Vorgabe Wert
    tx_resultat = Testresultat
    '''
    print(tx_titel, tx_test, "|", tx_wert, "!=", tx_resultat)
    in_anz += 1
    return(in_anz)


def f_oktext(tx_titel, tx_test):
    '''
    Gibt den OK Text aus.
    tx_titel = Titel
    tx_test = Test Bezeichnung
    '''
    print(tx_titel, " | ", tx_test)


if __name__ == '__main__':
    # Titel
    print("DS_TEST_DATEIINFO")
    print("-----------------")
    print("Objekt:     DateiInfo")
    print("Methoden:   __init__(), __str__(), m_clear(), m_get_dc(),")
    print("            m_set_dc(dc_daten)")
    print("Attribute:  tx_name, tx_typ, tx_datum, in_groesse")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    print()
    print("TEST        DateiInfo Objekt erzeugen")
    ob_datinf = DateiInfo()
    print()
    print("TEST        DateiInfo.__str__()")
    tx_r = ob_datinf.__str__()
    # Vergleich
    if bl_modus:
        # Produktiver Test Modus
        if not tx_r:
            in_anzerr = f_fehlertext(
                in_anzerr,
                "FEHLER     ",
                "DateiInfo.__str__()",
                tx_r,
                ""
            )
        else:
            print("OK          DateiInfo.__str__()")
    else:
        # Dieses Script testen
        in_anzerr = f_fehlertext(
            in_anzerr,
            "TESTFEHLER ",
            "DateiInfo.__str__()",
            tx_r,
            ""
        )
    # Testliste definieren, [[Schlüssel, Wert]
    ls_testdaten = [
        ["NAME", "Test_Datei"],
        ["TYP", ".txt"],
        ["DATUM", "21.12.2021 23:11:00"],
        ["GROESSE", 64]
    ]
    print()
    print("TEST        DateiInfo.m_set_dc(..)")
    dc_daten = {}
    for ls_t in ls_testdaten:
        dc_daten[ls_t[0]] = ls_t[1]
    ob_datinf.m_set_dc(dc_daten)
    print()
    print("TEST        DateiInfo.m_get_dc()")
    dc_daten = ob_datinf.m_get_dc()
    # Daten testen mit Schlüssel und Soll Resultat
    for ls_t in ls_testdaten:
        tx_k, vl_w = ls_t
        tx_test = "Schlüssel = '{0}'".format(tx_k)
        # Vergleich
        if bl_modus:
            # Produktiver Testmodus
            if dc_daten[tx_k] != vl_w:
                in_anzerr = f_fehlertext(
                    in_anzerr,
                    "FEHLER     ",
                    tx_test,
                    str(dc_daten[tx_k]),
                    str(vl_w)
                )
            else:
                print("OK         ", tx_test)
        else:
            # Dieses Script testen
            in_anzerr = f_fehlertext(
                in_anzerr,
                "TESTFEHLER ",
                tx_test,
                str(dc_daten[tx_k]),
                str(vl_w)
            )
    print()
    print("TEST        DateiInfo.m_clear()")
    ob_datinf.m_clear()
    # Testliste definieren, [[Testbezeichnung, Wert]
    ls_testdaten = [
        ["DateiInfo.tx_name", "Test_2"],
        ["DateiInfo.tx_typ", ".tx$"],
        ["DateiInfo.tx_datum", "23.12.2021 13:28:00"],
        ["DateiInfo.tx_groesse", 32]
    ]
    print()
    print("TEST        Werte direkt eintragen")
    ob_datinf.tx_name = ls_testdaten[0][1]
    ob_datinf.tx_typ = ls_testdaten[1][1]
    ob_datinf.tx_datum = ls_testdaten[2][1]
    ob_datinf.tx_groesse = ls_testdaten[3][1]
    print()
    print("TEST        Werte direkt abfragen")
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
        tx_test = "Attribut = {0}".format(tx_t)
        if bl_modus:
            # Produktiver Test Modus
            if vl_w != vl_r:
                in_anzerr = f_fehlertext(
                    in_anzerr,
                    "FEHLER     ",
                    tx_test,
                    str(vl_w),
                    str(vl_r)
                )
            else:
                print("OK         ", tx_test)
        else:
            # Dieses Script testen
            in_anzerr = f_fehlertext(
                in_anzerr,
                "TESTFEHLER ",
                tx_test,
                str(vl_w),
                str(vl_r)
            )
    print()
    print("ANZAHL     ", in_anzerr)
