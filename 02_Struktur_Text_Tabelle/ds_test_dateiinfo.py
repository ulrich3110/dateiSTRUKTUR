#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_htmlcsv import *
from ds_test_funktionen import *

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


def f_attribute(ob_test, tx_attribut):
    '''
    Liefert von einem <HtmlStruktur> Objekt den Wert des Attributes
    - ob_test = <HtmlStruktur> Objekt
    - tx_attribut = Text mit dem Namen des Attribtes
    Rückgabe des Attribut-Wertes
    '''
    # Mit Endswith Attribut suchen
    if tx_attribut.endswith("tx_name"):
        vl_test = ob_test.tx_name
    elif tx_attribut.endswith("tx_typ"):
        vl_test = ob_test.tx_typ
    elif tx_attribut.endswith("tx_datum"):
        vl_test = ob_test.tx_datum
    elif tx_attribut.endswith("in_groesse"):
        vl_test = ob_test.in_groesse
    # Wert zurückgeben
    return(vl_test)


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    print("DS_TEST_DATEIINFO")
    print("-----------------")
    print("Objekt:        DateiInfo")
    print("Methoden:      __init__(), __str__(), m_clear(),")
    print("               m_get_dc(), m_set_dc(<dict>)")
    print("Attribute:     tx_name, tx_typ, tx_datum, in_groesse")
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
    # Vorgabe
    tx_vorgabe = "NAME"
    # Test
    bl_test = tx_vorgabe in tx_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_vorgabe, tx_r)
    '''
    SET WÖRTERBUCH testen
    '''
    tx_test = "DateiInfo.m_set_dc(<dict>)"
    f_testtitel(tx_test)
    # Testliste definieren, [[Schlüssel, Wert], ]
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
        # Schlüssel, Vorgabe, Bezeichnung
        tx_k, vl_w = ls_t
        tx_test = "Schlüssel: '{0}'".format(tx_k)
        # Test
        bl_test = vl_w == dc_daten[tx_k]
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(dc_daten[tx_k]))
    '''
    CLEAR testen
    '''
    tx_test = "DateiInfo.m_clear()"
    f_testtitel(tx_test)
    ob_datinf.m_clear()
    # Testliste definieren, [[Atribut, Wert], ]
    ls_testdaten = [
        ["DateiInfo.tx_name", ""],
        ["DateiInfo.tx_typ", ""],
        ["DateiInfo.tx_datum", ""],
        ["DateiInfo.in_groesse", 0]
    ]
    # Testliste durchlaufen
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: {0}".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_datinf, tx_t)
        # Test
        bl_test = vl_w == vl_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(vl_r))
    '''
    Werte direkt eintragen
    '''
    tx_test = "Werte direkt eintragen"
    f_testtitel(tx_test)
    # Testliste definieren, [[Attribut, Wert], ]
    ls_testdaten = [
        ["DateiInfo.tx_name", "Test_2"],
        ["DateiInfo.tx_typ", ".tx$"],
        ["DateiInfo.tx_datum", "23.12.2021 13:28:00"],
        ["DateiInfo.in_groesse", 32]
    ]
    ob_datinf.tx_name = ls_testdaten[0][1]
    ob_datinf.tx_typ = ls_testdaten[1][1]
    ob_datinf.tx_datum = ls_testdaten[2][1]
    ob_datinf.in_groesse = ls_testdaten[3][1]
    '''
    Werte direkt abfragen
    '''
    tx_test = "Werte direkt abfragen"
    f_testtitel(tx_test)
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: {0}".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_datinf, tx_t)
        # Test
        bl_test = vl_w == vl_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(vl_r))
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
