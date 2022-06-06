#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_erfassen import *
from test_funktionen import *

'''
ds_test_verzeichnis.py - [d]atei[s]strukturen <Verzeichnis> Test
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
    if tx_attribut.endswith("tx_pfad"):
        vl_test = ob_test.tx_pfad
    elif tx_attribut.endswith("in_anzverz"):
        vl_test = ob_test.in_anzverz
    elif tx_attribut.endswith("ls_verz"):
        vl_test = ob_test.ls_verz
    elif tx_attribut.endswith("in_anzdat"):
        vl_test = ob_test.in_anzdat
    elif tx_attribut.endswith("in_anztyp"):
        vl_test = ob_test.in_anztyp
    elif tx_attribut.endswith("ls_dat"):
        vl_test = ob_test.ls_dat
    # Wert zurückgeben
    return(vl_test)


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    print("DS_TEST_VERZEICHNIS")
    print("-------------------")
    print("Objekt:        Verzeichnis")
    print("Methoden:      __init__(), __str__(), m_clear(),")
    print("               m_get_dc(<bool>), m_set_dc(<dict>, <bool>)")
    print("Attribute:     tx_pfad, in_anzverz, ls_verz, in_anzdat,")
    print("               in_anztyp, ls_dat")
    print("Bemerkung:     ls_dat = [<DateiInfo>, ]")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    # Text Variabblen für Objekte, Wörterbücher und beide
    tx_fuer_ob = "<Objekte>"
    tx_fuer_dc = "<Wörterbücher>"
    tx_fuer_beide = "<Obj. & Wörterb.>"
    '''
    OBJEKT erzeugen
    '''
    # Objekt für DateiInfo als Wörterbücher
    tx_test = "Verzeichnis Objekt {0} erzeugen".format(tx_fuer_dc)
    f_testtitel(tx_test)
    ob_verz_dc = Verzeichnis()
    # Objekt für DateiInfo als Objekte
    tx_test = "Verzeichnis Objekt {0} erzeugen".format(tx_fuer_ob)
    f_testtitel(tx_test)
    ob_verz_ob = Verzeichnis()
    '''
    __STR__ testen
    '''
    tx_test = "{0} Verzeichnis.__str__()".format(tx_fuer_beide)
    f_testtitel(tx_test)
    # Verzeichnis mit DateiInfo Wörterbücher und Objekten
    for ob_t, tx_t in [
        [ob_verz_dc, tx_fuer_dc],
        [ob_verz_ob, tx_fuer_ob]
    ]:
        tx_r = ob_t.__str__()
        # Vorgabe
        tx_vorgabe = "VERZEICHNISANZAHL"
        # Test
        bl_test = tx_vorgabe in tx_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                tx_vorgabe, tx_r)
    '''
    SET WÖRTERBUCH testen
    '''
    tx_test = "{0} Verzeichnis.m_set_dc(<dict>, <bool>)".\
        format(tx_fuer_beide)
    f_testtitel(tx_test)
    # Wörterbücher für Test DateiInfo Objekte
    dc_testdat1 = {"NAME": "Datei_1", "TYP": ".tya",
                   "DATUM": "23.12.2021 21:51:00", "GROESSE": 128}
    dc_testdat2 = {"NAME": "Datei_2", "TYP": ".tyb",
                   "DATUM": "23.12.2021 21:52:00", "GROESSE": 256}
    dc_testdat3 = {"NAME": "Datei_3", "TYP": ".tyb",
                   "DATUM": "23.12.2021 21:53:00", "GROESSE": 512}
    # Testliste mit DateiInfo als Wörterbücher
    ls_test_dc = [dc_testdat1, dc_testdat2, dc_testdat3]
    # Test DateiInfo Objekte definieren mit gleichen Informationen
    ob_testdat1 = DateiInfo()
    ob_testdat2 = DateiInfo()
    ob_testdat3 = DateiInfo()
    ob_testdat1.m_set_dc(dc_testdat1)
    ob_testdat2.m_set_dc(dc_testdat2)
    ob_testdat3.m_set_dc(dc_testdat3)
    # Testliste mit DateiInfo als Objekte
    ls_test_ob = [ob_testdat1, ob_testdat2, ob_testdat3]
    # Testliste definieren, [[Schlüssel, Wert], ]
    ls_testdaten = [
        ["PFAD", "/test"],
        ["VERZEICHNISANZAHL", 4],
        ["VERZEICHNISLISTE", ["eins", "zwei", "drei", "vier"]],
        ["DATEIANZAHL", 3],
        ["TYPANZAHL", 2]
    ]
    # 2 Test Wörterbücher: DateiInfo als Wörterbücher und als Objekte
    dc_test_dc = {}
    dc_test_ob = {}
    # Füllen mit Informationen
    for dc_t in [dc_test_dc, dc_test_ob]:
        for ls_t in ls_testdaten:
            dc_t[ls_t[0]] = ls_t[1]
    # Ergänzen mit DateiInfo Listen, als Wörterbücher und Objekte
    dc_test_dc["DATEILISTE"] = ls_test_dc
    dc_test_ob["DATEILISTE"] = ls_test_ob
    # Verzeichnis Objekten die Wörterbücher zuweisen
    # False = als Wörterbücher, True = als Objekte
    ob_verz_dc.m_set_dc(dc_test_dc, False)
    ob_verz_ob.m_set_dc(dc_test_ob, True)
    '''
    GET WÖRTERBUCH testen
    '''
    tx_test = "{0} Verzeichnis.m_get_dc()".format(tx_fuer_beide)
    f_testtitel(tx_test)
    # Wörterbücher holen, mit DateiInfo als Wörterbücher und Objekte
    # False = als Wörterbücher, True = als Objekte
    dc_test_dc = ob_verz_dc.m_get_dc(False)
    dc_test_ob = ob_verz_ob.m_get_dc(True)
    # Beide Daten testen
    for ls_u in [
        [dc_test_dc, tx_fuer_dc],
        [dc_test_ob, tx_fuer_ob]
    ]:
        dc_t, tx_t = ls_u
        # Mit Schlüssel und Soll Resualtat
        for ls_t in ls_testdaten:
            # Schlüssel, Vorgabe, Bezeichnung
            tx_k, vl_w = ls_t
            tx_test = "Schlüssel: '{0}'".format(tx_k)
            # Test
            bl_test = vl_w == dc_t[tx_k]
            # Vergleich
            in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr,
                                    tx_test, str(vl_w),
                                    str(dc_t[tx_k]))
    tx_test = "Schlüssel: 'DATEILISTE'"
    for ls_t in [
        [dc_test_dc["DATEILISTE"], ls_test_dc, tx_fuer_dc],
        [dc_test_ob["DATEILISTE"], ls_test_ob, tx_fuer_ob]
    ]:
        # Resultat, Vorgabe, Bezeichnung
        ls_u, ls_v, tx_t = ls_t
        # Test
        bl_test = ls_v == ls_u
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(ls_v), str(ls_u))
    '''
    CLEAR testen
    '''
    tx_test = "{0} Verzeichnis.m_clear()".format(tx_fuer_ob)
    f_testtitel(tx_test)
    ob_verz_ob.m_clear()
    # Testliste definieren, [[Atribut, Wert], ]
    ls_testdaten = [
        ["Verzeichnis.tx_pfad", ""],
        ["Verzeichnis.in_anzverz", 0],
        ["Verzeichnis.ls_verz", []],
        ["Verzeichnis.in_anzdat", 0],
        ["Verzeichnis.in_anztyp", 0],
        ["Verzeichnis.ls_dat", []]
    ]
    # Testliste durchlaufen
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: '{0}'".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_verz_ob, tx_t)
        # Test
        bl_test = vl_w == vl_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(vl_r))
    '''
    Werte direkt eintragen
    '''
    tx_test = "{0} Werte direkt eintragen".format(tx_fuer_ob)
    f_testtitel(tx_test)
    # Test DateiInfo Objekte
    ob_testdat1 = DateiInfo()
    ob_testdat1.m_set_dc({
        "NAME": "Datei_11",
        "TYP": ".typ",
        "DATUM": "24.12.2021 15:11:00",
        "GROESSE": 1024
    })
    ob_testdat2 = DateiInfo()
    ob_testdat2.m_set_dc({
        "NAME": "Datei_22",
        "TYP": ".typ",
        "DATUM": "24.12.2021 15:22:00",
        "GROESSE": 2048
    })
    ob_testdat3 = DateiInfo()
    # Testliste definieren, [[Attribut, Wert], ]
    ls_testdaten = [
        ["Verzeichnis.tx_pfad", "/test"],
        ["Verzeichnis.in_anzverz", 5],
        ["Verzeichnis.ls_verz", ["1", "2", "3", "4", "5"]],
        ["Verzeichnis.in_anzdat", 2],
        ["Verzeichnis.in_anztyp", 1],
        ["Verzeichnis.ls_dat", [ob_testdat1, ob_testdat2]]
    ]
    ob_verz_ob.tx_pfad = ls_testdaten[0][1]
    ob_verz_ob.in_anzverz = ls_testdaten[1][1]
    ob_verz_ob.ls_verz = ls_testdaten[2][1]
    ob_verz_ob.in_anzdat = ls_testdaten[3][1]
    ob_verz_ob.in_anztyp = ls_testdaten[4][1]
    ob_verz_ob.ls_dat = ls_testdaten[5][1]
    '''
    Werte direkt abfragen
    '''
    tx_test = "{0} Werte direkt abfragen".format(tx_fuer_ob)
    f_testtitel(tx_test)
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: {0}".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_verz_ob, tx_t)
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
