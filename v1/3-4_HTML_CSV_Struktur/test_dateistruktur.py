#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_htmlcsv import *
from test_funktionen import *

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


def f_attribute(ob_test, tx_attribut):
    '''
    Liefert von einem <HtmlStruktur> Objekt den Wert des Attributes
    - ob_test = <HtmlStruktur> Objekt
    - tx_attribut = Text mit dem Namen des Attribtes
    Rückgabe des Attribut-Wertes
    '''
    # Mit Endswith Attribut suchen
    if tx_attribut.endswith("ls_dateien"):
        vl_test = ob_test.ls_dateien
    elif tx_attribut.endswith("ls_verzeich"):
        vl_test = ob_test.ls_verzeich
    elif tx_attribut.endswith("tx_stammpfad"):
        vl_test = ob_test.tx_stammpfad
    elif tx_attribut.endswith("tx_datum"):
        vl_test = ob_test.tx_datum
    elif tx_attribut.endswith("in_anzverz"):
        vl_test = ob_test.in_anzverz
    elif tx_attribut.endswith("in_anzdat"):
        vl_test = ob_test.in_anzdat
    elif tx_attribut.endswith("in_anztyp"):
        vl_test = ob_test.in_anztyp
    elif tx_attribut.endswith("ls_verz"):
        vl_test = ob_test.ls_verz
    # Wert zurückgeben
    return(vl_test)


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    print("DS_TEST_DATEISTRUKUR")
    print("--------------------")
    print("Objekt:        DateiStruktur")
    print("Methoden:      __init__(), __str__(), m_clear(),")
    print("               m_get_dc(<bool>), m_set_dc(<dict>, <bool>),")
    print("               m_lesen(), m_ordnen(), m_total()")
    print("Attribute:     ls_dateien, ls_verzeich, tx_stammpfad,")
    print("               tx_datum, in_anzverz, in_anzdat, in_anztyp,")
    print("               ls_verz")
    print("Bemerkung:     ls_verz = [<Verzeichnis>, ]")
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
    # Objekt für Verzeichnisse als Wörterbücher
    tx_test = "DateiStruktur Objekt {0} erzeugen".format(tx_fuer_dc)
    f_testtitel(tx_test)
    ob_datstrkt_dc = DateiStruktur()
    # Objekt für Verzeichnisse als Objekte
    tx_test = "DateiStruktur Objekt {0} erzeugen".format(tx_fuer_ob)
    f_testtitel(tx_test)
    ob_datstrkt_ob = DateiStruktur()
    '''
    __STR__ testen
    '''
    tx_test = "{0} DateiStruktur.__str__()".format(tx_fuer_beide)
    f_testtitel(tx_test)
    # Verzeichnis mit DateiInfo Wörterbücher und Objekten
    for ob_t, tx_t in [
        [ob_datstrkt_dc, tx_fuer_dc],
        [ob_datstrkt_ob, tx_fuer_ob]
    ]:
        tx_r = ob_t.__str__()
        # Vorgabe
        tx_vorgabe = "DATEILISTE"
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
    dc_testv1_dc = {"PFAD": "/stamm", "VERZEICHNISANZAHL": 3,
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
    # Testliste definieren, [[Schlüssel, Wert], ]
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
    '''
    GET WÖRTERBUCH testen
    '''
    tx_test = "{0} Verzeichnis.m_get_dc()".format(tx_fuer_beide)
    f_testtitel(tx_test)
    # Wörterbücher holen, mit DateiInfo als Wörterbücher und Objekte
    # False = als Wörterbücher, True = als Objekte
    dc_test_dc = ob_datstrkt_dc.m_get_dc(False)
    dc_test_ob = ob_datstrkt_ob.m_get_dc(True)
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
    tx_test = "Schlüssel: 'VERZEICHNISSE'"
    for ls_t in [
        [dc_test_dc["VERZEICHNISSE"], ls_test_dc, tx_fuer_dc],
        [dc_test_ob["VERZEICHNISSE"], ls_test_ob, tx_fuer_ob]
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
    tx_test = "{0} DateiStruktur.m_clear()".format(tx_fuer_ob)
    f_testtitel(tx_test)
    ob_datstrkt_ob.m_clear()
    # Testliste definieren, [[Atribut, Wert], ]
    ls_testdaten = [
        ["DateiStruktur.ls_dateien", []],
        ["DateiStruktur.ls_verzeich", []],
        ["DateiStruktur.tx_stammpfad", ""],
        ["DateiStruktur.tx_datum", ""],
        ["DateiStruktur.in_anzverz", 0],
        ["DateiStruktur.in_anzdat", 0],
        ["DateiStruktur.in_anztyp", 0],
        ["DateiStruktur.ls_verz", []]
    ]
    # Testliste durchlaufen
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: '{0}'".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_datstrkt_ob, tx_t)
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
    # Testliste definieren, [[Attribut, Wert], ]
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
    ob_datstrkt_ob.ls_dateien = ls_testdaten[0][1]
    ob_datstrkt_ob.ls_verzeich = ls_testdaten[1][1]
    ob_datstrkt_ob.tx_stammpfad = ls_testdaten[2][1]
    ob_datstrkt_ob.tx_datum = ls_testdaten[3][1]
    ob_datstrkt_ob.in_anzverz = ls_testdaten[4][1]
    ob_datstrkt_ob.in_anzdat = ls_testdaten[5][1]
    ob_datstrkt_ob.in_anztyp = ls_testdaten[6][1]
    ob_datstrkt_ob.ls_verz = ls_testdaten[7][1]
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
        vl_r = f_attribute(ob_datstrkt_ob, tx_t)
        # Test
        bl_test = vl_w == vl_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(vl_r))
    '''
    LESEN testen
    '''
    tx_stamm = ".."
    tx_test = "{0} DateiStruktur.m_lesen(), stamm={1}".format(
        tx_fuer_beide,
        tx_stamm
    )
    f_testtitel(tx_test)
    # DateiStruktur mit Wörterbücher und Objekte testen
    for ob_t, tx_t in [
        [ob_datstrkt_dc, tx_fuer_dc],
        [ob_datstrkt_ob, tx_fuer_ob]
    ]:
        # Stammpfad setzen
        ob_t.tx_stammpfad = tx_stamm
        # DateiStruktur lesen
        ob_t.m_lesen()
        # Werte testen: Resultat darf nicht leer sein
        for vl_r, tx_w, tx_ta in [
            [ob_t.ls_dateien, "[Liste mit Dateien]",
             "DateiStruktur.ls_dateien"],
            [ob_t.ls_verzeich, "[Liste mit Verzeichnissen]",
             "DateiStruktur.ls_verezeich"],
            [ob_t.tx_datum, "'Datum als Text'",
             "DateiStruktur.tx_datum"]
        ]:
            # Titel
            tx_test = "Attribut: {0}".format(tx_ta)
            # Test
            if vl_r:
                bl_test = True
            else:
                bl_test = False
            # Vergleich
            in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr,
                                    tx_test, tx_w, str(vl_r))
    '''
    ORDNEN testen
    '''
    tx_test = "{0} DateiStruktur.m_ordnen()".format(tx_fuer_beide)
    f_testtitel(tx_test)
    # DateiStruktur mit Wörterbücher und Objekte testen
    for ob_t, tx_t in [
        [ob_datstrkt_dc, tx_fuer_dc],
        [ob_datstrkt_ob, tx_fuer_ob]
    ]:
        # DateiStruktur ordnen
        ob_t.m_ordnen()
        # Test
        if ob_t.ls_verz:
            bl_test = True
        else:
            bl_test = False
        # Vergleich
        tx_test = "{0} Attribut: DateiStruktur.ls_verz".format(tx_t)
        tx_w = "[Liste mit Dateiinformationen]"
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                tx_w, str(ob_t.ls_verz))
    '''
    TOTAL testen
    '''
    tx_test = "{0} DateiStruktur.m_total()".format(tx_fuer_beide)
    f_testtitel(tx_test)
    # DateiStruktur mit Wörterbücher und Objekte testen
    for ob_t, tx_t in [
        [ob_datstrkt_dc, tx_fuer_dc],
        [ob_datstrkt_ob, tx_fuer_ob]
    ]:
        # DateiStruktur ordnen
        ob_t.m_total()
        # Werte testen: Resultat darf nicht 0 sein
        for vl_r, tx_ta in [
            [ob_t.in_anzverz, "DateiStruktur.in_anzverz"],
            [ob_t.in_anzdat, "DateiStruktur.in_anzdat"],
            [ob_t.in_anztyp, "DateiStruktur.in_anztyp"]
        ]:
            # Titel
            tx_test = "Attribut: {0}".format(tx_ta)
            # Test
            bl_test = vl_r > 0
            # Vergleich
            in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr,
                                    tx_test, "> 0", str(vl_r))
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
