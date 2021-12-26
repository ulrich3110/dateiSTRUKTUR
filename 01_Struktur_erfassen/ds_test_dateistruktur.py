#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_erfassen import *

'''
ds_test_dateistruktur.py - [d]atei[s]strukturen <DateiStruktur> Test
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


if __name__ == '__main__':
    # Titel
    print("DS_TEST_DATEISTRUKUR")
    print("-------------------")
    print("Objekt:     DateiStruktur")
    print("Methoden:   __init__(), __str__(), m_clear(),")
    print("            m_get_dc(<bool>),")
    print("            m_set_dc(<dict>, <bool>),")
    print("            m_lesen(), m_ordnen(), m_total()")
    print("Attribute:  ls_dateien, ls_verzeich, tx_stammpfad, tx_datum")
    print("            in_anzverz, in_anzdat, ls_verz")
    print("Bemerkung:  ls_verz = [<Verzeichnis>, ]")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    print()
    print("TEST        DateiStruktur Objekt erzeugen")
    # Objekt für Verzeichnisse als Wörterbücher
    ob_datstrkt_dc = DateiStruktur()
    # Objekt für Verzeichnisse als Objekte
    ob_datstrkt_ob = DateiStruktur()
    print()
    print("TEST        DateiStruktur.__str__()")
    # Verzeichnis DateiInfo Wörterbücher
    tx_r = ob_datstrkt_dc.__str__()
    # Vergleich
    tx_test = "DateiStruktur.__str__()"
    if bl_modus:
        # Produktiver Test Modus
        if not tx_r:
            in_anzerr = f_fehlertext(
                in_anzerr,
                "FEHLER      (Wörterbücher)",
                tx_test,
                tx_r,
                ""
            )
        else:
            print("OK          (Wörterbücher) DateiStruktur.__str__()")
    else:
        # Dieses Script testen
        in_anzerr = f_fehlertext(
            in_anzerr,
            "TESTFEHLER  (Wörterbücher)",
            tx_test,
            tx_r,
            ""
        )
    # Verzeichnis DateiInfo Objekte
    tx_r = ob_datstrkt_ob.__str__()
    if bl_modus:
        # Produktiver Test Modus
        if not tx_r:
            in_anzerr = f_fehlertext(
                in_anzerr,
                "FEHLER      (Objekte)",
                tx_test,
                tx_r,
                ""
            )
        else:
            print("OK          (Objekte) DateiStruktur.__str__()")
    else:
        # Dieses Script testen
        in_anzerr = f_fehlertext(
            in_anzerr,
            "TESTFEHLER  (Objekte)",
            tx_test,
            tx_r,
            ""
        )
    print()
    print("TEST        DateiStruktur.m_set_dc(..)")
    # Wörterbücher für Test DateiInfo Objekte
    dc_testdat11 = {"NAME": "Datei_11", "TYP": ".tya",
                    "DATUM": "25.12.2021 15:34:00", "GROESSE": 16}
    dc_testdat12 = {"NAME": "Datei_12", "TYP": ".tyb",
                    "DATUM": "25.12.2021 15:35:00", "GROESSE": 32}
    dc_testdat13 = {"NAME": "Datei_13", "TYP": ".tyc",
                    "DATUM": "25.12.2021 15:36:00", "GROESSE": 64}
    dc_testdat21 = {"NAME": "Datei_21", "TYP": ".tya",
                    "DATUM": "25.12.2021 15:37:00", "GROESSE": 80}
    dc_testdat22 = {"NAME": "Datei_22", "TYP": ".tyb",
                    "DATUM": "25.12.2021 15:38:00", "GROESSE": 96}
    dc_testdat31 = {"NAME": "Datei_31", "TYP": ".tya",
                    "DATUM": "25.12.2021 15:39:00", "GROESSE": 112}
    dc_testdat32 = {"NAME": "Datei_32", "TYP": ".tyb",
                    "DATUM": "25.12.2021 15:40:00", "GROESSE": 128}
    dc_testdat33 = {"NAME": "Datei_33", "TYP": ".tyc",
                    "DATUM": "25.12.2021 15:41:00", "GROESSE": 144}
    dc_testdat34 = {"NAME": "Datei_34", "TYP": ".tya",
                    "DATUM": "25.12.2021 15:42:00", "GROESSE": 160}
    # Testlisten mit DateiInfo als Wörterbücher
    ls_dat1_dc = [dc_testdat11, dc_testdat12, dc_testdat13]
    ls_dat2_dc = [dc_testdat21, dc_testdat22]
    ls_dat3_dc = [dc_testdat31, dc_testdat32, dc_testdat33,
                  dc_testdat34]
    # Wörterbücher für Test Verzeichnisse
    dc_testv1_dc = {"PFAD": "/stamm", "VERZEICHNISANZAHL": 4,
                    "VERZEICHNISLISTE": ["pfad1", "pfad2", "pfad3"],
                    "DATEIANZAHL": 0, "TYPANZAHL": 0,
                    "DATEILISTE": []}
    dc_testv2_dc = {"PFAD": "/stamm/pfad1", "VERZEICHNISANZAHL": 0,
                    "VERZEICHNISLISTE": [], "DATEIANZAHL": 3,
                    "TYPANZAHL": 3, "DATEILISTE": ls_dat1_dc}
    dc_testv3_dc = {"PFAD": "/stamm/pfad2", "VERZEICHNISANZAHL": 0,
                    "VERZEICHNISLISTE": [], "DATEIANZAHL": 2,
                    "TYPANZAHL": 2, "DATEILISTE": ls_dat2_dc}
    dc_testv4_dc = {"PFAD": "/stamm/pfad3", "VERZEICHNISANZAHL": 0,
                    "VERZEICHNISLISTE": [], "DATEIANZAHL": 4,
                    "TYPANZAHL": 3, "DATEILISTE": ls_dat3_dc}
    # Verzeichnislisten mit Wörterbücher
    ls_test_dc = [dc_testv1_dc, dc_testv2_dc,
                  dc_testv3_dc, dc_testv4_dc]
    # Test DateiInfo Objekte definieren mit gleichen Informationen
    ob_testdat11 = DateiInfo()
    ob_testdat12 = DateiInfo()
    ob_testdat13 = DateiInfo()
    ob_testdat21 = DateiInfo()
    ob_testdat22 = DateiInfo()
    ob_testdat31 = DateiInfo()
    ob_testdat32 = DateiInfo()
    ob_testdat33 = DateiInfo()
    ob_testdat34 = DateiInfo()
    ob_testdat11.m_set_dc(dc_testdat11)
    ob_testdat12.m_set_dc(dc_testdat12)
    ob_testdat13.m_set_dc(dc_testdat13)
    ob_testdat21.m_set_dc(dc_testdat21)
    ob_testdat22.m_set_dc(dc_testdat22)
    ob_testdat31.m_set_dc(dc_testdat31)
    ob_testdat32.m_set_dc(dc_testdat32)
    ob_testdat33.m_set_dc(dc_testdat33)
    ob_testdat34.m_set_dc(dc_testdat34)
    # Testlisten mit DateiInfo als Objekte
    ls_dat1_ob = [ob_testdat11, ob_testdat12, ob_testdat13]
    ls_dat2_ob = [ob_testdat21, ob_testdat22]
    ls_dat3_ob = [ob_testdat31, ob_testdat32, ob_testdat33,
                  ob_testdat34]
    # Objekte für Test verzeichnisse
    ob_testver1 = Verzeichnis()
    ob_testver2 = Verzeichnis()
    ob_testver3 = Verzeichnis()
    ob_testver4 = Verzeichnis()
    # Wörterbücher für Test Verzeichnisse mit Objekten
    dc_testv1_ob = {}
    dc_testv2_ob = {}
    dc_testv3_ob = {}
    dc_testv4_ob = {}
    # Wörterbüche mit gleichen Werten wie dc_testv._dc
    ls_k = list(dc_testv1_dc.keys())
    for ls_i in [
        [dc_testv1_dc, dc_testv1_ob],
        [dc_testv2_dc, dc_testv2_ob],
        [dc_testv3_dc, dc_testv3_ob],
        [dc_testv4_dc, dc_testv4_ob]
    ]:
        for tx_k in ls_k:
            ls_i[1][tx_k] = ls_i[0][tx_k]
    # Wörterbücher mit Test Objekten
    dc_testv2_ob["DATEILISTE"] = ls_dat1_ob
    dc_testv3_ob["DATEILISTE"] = ls_dat2_ob
    dc_testv4_ob["DATEILISTE"] = ls_dat3_ob
    # Verzeichnisliste mit Objekten
    ls_test_ob = [dc_testv1_ob, dc_testv2_ob,
                  dc_testv3_ob, dc_testv4_ob]
    # Testliste definieren, [[Schlüssel, Wert]
    ls_testdaten = [
        ["DATEILISTE",
            ["/stamm/pfad1/Datei_11.tya", "/stamm/pfad1/Datei_12.tyb",
             "/stamm/pfad1/Datei_13.tyc", "/stamm/pfad2/Datei_21.tya",
             "/stamm/pfad2/Datei_22.tyb", "/stamm/pfad3/Datei_31.tya",
             "/stamm/pfad3/Datei_32.tyb", "/stamm/pfad3/Datei_33.tyc",
             "/stamm/pfad3/Datei_34.tya"]],
        ["VERZEICHNISLISTE",
            ["/stamm", "/stamm/pfad1", "/stamm/pfad2", "/stamm/pfad3"]],
        ["STAMMPFAD", "/stamm"],
        ["DATUM", "25.12.2021 15:21:00"],
        ["VERZEICHNISANZAHL", 4],
        ["DATEIANZAHL", 9],
        ["TYPANZAHL", 3]
    ]
    # 2 Test Wörterbücher: Verzeichnisse als Wörterbücher und Objekte
    dc_test_dc = {}
    dc_test_ob = {}
    # Füllen mit Informationen
    for dc_t in [dc_test_dc, dc_test_ob]:
        for ls_t in ls_testdaten:
            dc_t[ls_t[0]] = ls_t[1]
    # Ergänzen mit DateiInfo Listen, als Wörterbücher und Objekte
    dc_test_dc["VERZEICHNISSE"] = ls_test_dc
    dc_test_ob["VERZEICHNISSE"] = ls_test_ob
    # Verzeichnis Objekten die Wörterbücher zuweisen
    # False = als Wörterbücher, True = als Objekte
    ob_datstrkt_dc.m_set_dc(dc_test_dc, False)
    ob_datstrkt_ob.m_set_dc(dc_test_ob, True)
    print()
    print("TEST        DateiStruktur.m_get_dc()")
    # Wörterbücher holen, mit DateiInfo als Wörterbücher und Objekte
    # False = als Wörterbücher, True = als Objekte
    dc_test_dc = ob_datstrkt_dc.m_get_dc(False)
    dc_test_ob = ob_datstrkt_ob.m_get_dc(True)
    # Beide Daten testen
    for ls_u in [
        [dc_test_dc, "Wörterbücher"],
        [dc_test_ob, "Objekte"]
    ]:
        dc_t, tx_t = ls_u
        # Mit Schlüssel und Soll Resualtat
        for ls_t in ls_testdaten:
            tx_k, vl_w = ls_t
            tx_test = "Schlüssel = '{0}'".format(tx_k)
            # Vergleich
            if bl_modus:
                # Produktiver Testmodus
                if dc_t[tx_k] != vl_w:
                    in_anzerr = f_fehlertext(
                        in_anzerr,
                        "FEHLER      ({0})".format(tx_t),
                        tx_test,
                        str(dc_t[tx_k]),
                        str(vl_w)
                    )
                else:
                    print("OK          ({0}) {1}".format(
                        tx_t, tx_test
                    ))
            else:
                # Dieses Script testen
                in_anzerr = f_fehlertext(
                    in_anzerr,
                    "FEHLER      ({0})".format(tx_t),
                    tx_test,
                    str(dc_t[tx_k]),
                    str(vl_w)
                )
    tx_test = "Schlüssel = 'VERZEICHNISSE'"
    for ls_t in [
        [dc_test_dc["VERZEICHNISSE"], ls_test_dc, "Wörterbücher"],
        [dc_test_ob["VERZEICHNISSE"], ls_test_ob, "Objekte"]
    ]:
        ls_u, ls_v, tx_t = ls_t
        # DateiInfo Listen Vergleich
        if bl_modus:
            # Produktiver Test Modus
            if ls_u != ls_v:
                in_anzerr = f_fehlertext(
                    in_anzerr,
                    "FEHLER      ({0})".format(tx_t),
                    tx_test,
                    str(ls_u),
                    str(ls_v)
                )
            else:
                print("OK          ({0}) {1}".format(
                    tx_t, tx_test
                ))
        else:
            # Dieses Script testen
            in_anzerr = f_fehlertext(
                in_anzerr,
                "TESTFEHLER  ({0})".format(tx_t),
                tx_test,
                str(ls_u),
                str(ls_v)
            )
    print()
    print("TEST        DateiStruktur.m_clear()")
    ob_datstrkt_ob.m_clear()
    # Test DateiInfo Objekte
    ob_testdat01 = DateiInfo()
    ob_testdat11 = DateiInfo()
    ob_testdat12 = DateiInfo()
    ob_testdat13 = DateiInfo()
    ob_testdat21 = DateiInfo()
    ob_testdat22 = DateiInfo()
    ob_testdat23 = DateiInfo()
    ob_testdat24 = DateiInfo()
    ob_testdat01.m_set_dc({"NAME": "Datei_01", "TYP": ".tyD",
                           "DATUM": "26.12.2021 14:21:00",
                           "GROESSE": 800})
    ob_testdat11.m_set_dc({"NAME": "Datei_11", "TYP": ".tyA",
                           "DATUM": "26.12.2021 14:18:00",
                           "GROESSE": 160})
    ob_testdat12.m_set_dc({"NAME": "Datei_12", "TYP": ".tyB",
                           "DATUM": "26.12.2021 14:19:00",
                           "GROESSE": 320})
    ob_testdat13.m_set_dc({"NAME": "Datei_13", "TYP": ".tyB",
                           "DATUM": "26.12.2021 14:20:00",
                           "GROESSE": 640})
    ob_testdat21.m_set_dc({"NAME": "Datei_22", "TYP": ".tyC",
                           "DATUM": "26.12.2021 14:22:00",
                           "GROESSE": 960})
    ob_testdat22.m_set_dc({"NAME": "Datei_31", "TYP": ".tyC",
                           "DATUM": "26.12.2021 14:23:00",
                           "GROESSE": 1120})
    ob_testdat23.m_set_dc({"NAME": "Datei_32", "TYP": ".tyD",
                           "DATUM": "26.12.2021 14:24:00",
                           "GROESSE": 1280})
    ob_testdat24.m_set_dc({"NAME": "Datei_33", "TYP": ".tyE",
                           "DATUM": "26.12.2021 14:25:00",
                           "GROESSE": 1440})
    # Testlisten mit DateiInfo als Objekte
    ls_dat0_ob = [ob_testdat01]
    ls_dat1_ob = [ob_testdat11, ob_testdat12, ob_testdat13]
    ls_dat2_ob = [ob_testdat21, ob_testdat22, ob_testdat23,
                  ob_testdat24]
    # Objekte für Test verzeichnisse
    ob_testver0 = Verzeichnis()
    ob_testver1 = Verzeichnis()
    ob_testver2 = Verzeichnis()
    # Wörterbücher für Test Verzeichnisse mit Objekten
    dc_testv0_ob = {"PFAD": "/stamm", "VERZEICHNISANZAHL": 2,
                    "VERZEICHNISLISTE": ["verz1", "verz2"],
                    "DATEIANZAHL": 1, "TYPANZAHL": 1,
                    "DATEILISTE": ls_dat0_ob}
    dc_testv1_ob = {"PFAD": "/stamm/verz1", "VERZEICHNISANZAHL": 0,
                    "VERZEICHNISLISTE": [], "DATEIANZAHL": 3,
                    "TYPANZAHL": 2, "DATEILISTE": ls_dat1_ob}
    dc_testv2_ob = {"PFAD": "/stamm/verz2", "VERZEICHNISANZAHL": 0,
                    "VERZEICHNISLISTE": [], "DATEIANZAHL": 4,
                    "TYPANZAHL": 3, "DATEILISTE": ls_dat2_ob}
    # Verzeichnisliste mit Objekten
    ls_test_ob = [dc_testv0_ob, dc_testv1_ob, dc_testv2_ob]
    # Testliste definieren, [[Schlüssel, Wert]
    ls_testdaten = [
        ["DateiStruktur.ls_dateien",
            ["/stamm/Datei_01.tyD", "/stamm/verz1/Datei_11.tyA",
             "/stamm/verz1/Datei_12.tyB", "/stamm/verz1/Datei_13.tyB",
             "/stamm/verz2/Datei_21.tyC", "/stamm/verz2/Datei_22.tyC",
             "/stamm/verz2/Datei_23.tyD", "/stamm/verz2/Datei_24.tyE"]],
        ["DateiStruktur.ls_verzeich",
            ["/stamm", "/stamm/verz1", "/stamm/verz2"]],
        ["DateiStruktur.tx_stammpfad", "/stamm"],
        ["DateiStruktur.tx_datum", "25.12.2021 16:27:00"],
        ["DateiStruktur.in_anzverz", 3],
        ["DateiStruktur.in_anzdat", 9],
        ["DateiStruktur.in_anztyp", 5],
        ["DateiStruktur.ls_verz", ls_test_ob]
    ]
    print()
    print("TEST        Werte direkt eintragen")
    ob_datstrkt_ob.ls_dateien = ls_testdaten[0][1]
    ob_datstrkt_ob.ls_verzeich = ls_testdaten[1][1]
    ob_datstrkt_ob.tx_stammpfad = ls_testdaten[2][1]
    ob_datstrkt_ob.tx_datum = ls_testdaten[3][1]
    ob_datstrkt_ob.in_anzverz = ls_testdaten[4][1]
    ob_datstrkt_ob.in_anzdat = ls_testdaten[5][1]
    ob_datstrkt_ob.in_anztyp = ls_testdaten[6][1]
    ob_datstrkt_ob.ls_verz = ls_testdaten[7][1]
    print()
    print("TEST        Werte direkt abfragen")
    for ls_t in ls_testdaten:
        tx_t, vl_w = ls_t
        if tx_t.endswith(".ls_dateien"):
            vl_r = ob_datstrkt_ob.ls_dateien
        elif tx_t.endswith(".ls_verzeich"):
            vl_r = ob_datstrkt_ob.ls_verzeich
        elif tx_t.endswith(".tx_stammpfad"):
            vl_r = ob_datstrkt_ob.tx_stammpfad
        elif tx_t.endswith(".tx_datum"):
            vl_r = ob_datstrkt_ob.tx_datum
        elif tx_t.endswith(".in_anzverz"):
            vl_r = ob_datstrkt_ob.in_anzverz
        elif tx_t.endswith(".in_anzdat"):
            vl_r = ob_datstrkt_ob.in_anzdat
        elif tx_t.endswith(".in_anztyp"):
            vl_r = ob_datstrkt_ob.in_anztyp
        elif tx_t.endswith(".ls_verz"):
            vl_r = ob_datstrkt_ob.ls_verz
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
