#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_htmlcsv import *
from ds_test_funktionen import *

'''
ds_test_strukturausgabe.py - [d]atei[s]strukturen <StrukturAusgabe> Test
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
    if tx_attribut.endswith("dc_struktur"):
        vl_test = ob_test.dc_struktur
    elif tx_attribut.endswith("ls_ausgabe"):
        vl_test = ob_test.ls_ausgabe
    # Wert zurückgeben
    return(vl_test)


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    print("DS_TEST_StrukturAusgabe")
    print("-----------------------")
    print("Objekt:        StrukturAusgabe")
    print("Methoden:      __init__(), __str__(), m_clear(),")
    print("               m_get_dc(), m_set_dc(<dict>),")
    print("               m_ausgabeliste(), m_struktur(),")
    print("               m_verzeichnis(), m_ausgabeliste(<list>)")
    print("Attribute:     dc_struktur, ls_ausgabe")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    '''
    OBJEKT erzeugen
    '''
    tx_test = "StrukturAusgabe Objekt erzeugen"
    f_testtitel(tx_test)
    ob_ausgabe = StrukturAusgabe()
    '''
    __STR__ testen
    '''
    tx_test = "StrukturAusgabe.__str__()"
    f_testtitel(tx_test)
    tx_r = ob_ausgabe.__str__()
    # Vorgabe
    tx_vorgabe = "DATEISTRUKTUR"
    # Test
    bl_test = tx_vorgabe in tx_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_vorgabe, tx_r)
    '''
    SET WÖRTERBUCH testen
    '''
    tx_test = "StrukturAusgabe.m_set_dc(<dict>)"
    f_testtitel(tx_test)
    # Ausgabelisten definieren: [Stammpfad absolut, Datum / Zeit,
    #   Anzahl Verzeichnisse, Anzahl Dateien, Anzahl Dateitypen,
    #   [  [Verzeichnispfad relativ, Anzahl Verzeichnisse,
    #        [Verzeichnisnamen, ], Anzahl Dateien, Anzahl Dateitypen,
    #        [ [Name, Typ, Datum, Groesse],  ],
    #      ],  ]
    # Testdateien als Listen definieren:
    # [Name, Typ, Datum, Groesse]
    ls_dat_11 = ["Datei_11", ".tya", "25.12.2021 15:34:00", 16]
    ls_dat_12 = ["Datei_12", ".tyb", "25.12.2021 15:35:00", 32]
    ls_dat_13 = ["Datei_13", ".tyc", "25.12.2021 15:36:00", 64]
    ls_dat_21 = ["Datei_21", ".tya", "25.12.2021 15:37:00", 80]
    ls_dat_22 = ["Datei_22", ".tyb", "25.12.2021 15:38:00", 96]
    ls_dat_31 = ["Datei_31", ".tya", "25.12.2021 15:39:00", 112]
    ls_dat_32 = ["Datei_32", ".tyb", "25.12.2021 15:40:00", 128]
    ls_dat_33 = ["Datei_33", ".tyc", "25.12.2021 15:41:00", 144]
    ls_dat_34 = ["Datei_34", ".tya", "25.12.2021 15:42:00", 160]
    # Testverzeichnisse als Listen definieren:
    # [Pfad relativ, Anzahl Verz., [Verzeichnisse, ], Anzahl Dateien,
    #  Anzahl Dateitypen, [Dateilisten,  ]]
    ls_verz_0 = ["/stamm", 3, ["pfad1", "pfad2", "pfad3"], 0, 0, []]
    ls_verz_1 = ["/stamm/pfad1", 0, [], 3, 3, [ls_dat_11, ls_dat_12,
                 ls_dat_13]]
    ls_verz_2 = ["/stamm/pfad2", 0, [], 2, 2, [ls_dat_21, ls_dat_22]]
    ls_verz_3 = ["/stamm/pfad3", 0, [], 4, 3, [ls_dat_31, ls_dat_32,
                 ls_dat_33, ls_dat_34]]
    # Ausgabeliste zusammenstellen
    ls_test_ausgabe = ["/stamm", "25.12.2021 15:21:00", 4, 9, 3,
                       [ls_verz_0, ls_verz_1, ls_verz_2, ls_verz_3]]
    # Datistruktur JSON definieren (wie in ds_test_dateistruktur.py)
    # Datei-Informationen
    dc_dat_11, dc_dat_12, dc_dat_13 = {}, {}, {}
    dc_dat_21, dc_dat_22 = {}, {}
    dc_dat_31, dc_dat_32, dc_dat_33, dc_dat_34 = {}, {}, {}, {}
    for dc_i, ls_i in [[dc_dat_11, ls_dat_11], [dc_dat_12, ls_dat_12],
                       [dc_dat_13, ls_dat_13],
                       [dc_dat_21, ls_dat_21], [dc_dat_22, ls_dat_22],
                       [dc_dat_31, ls_dat_31], [dc_dat_32, ls_dat_32],
                       [dc_dat_33, ls_dat_33], [dc_dat_34, ls_dat_34]]:
        dc_i["NAME"] = ls_i[0]
        dc_i["TYP"] = ls_i[1]
        dc_i["DATUM"] = ls_i[2]
        dc_i["GROESSE"] = ls_i[3]
    # Dateilisten
    ls_dateien_1 = [dc_dat_11, dc_dat_12, dc_dat_13]
    ls_dateien_2 = [dc_dat_21, dc_dat_22]
    ls_dateien_3 = [dc_dat_31, dc_dat_32, dc_dat_33, dc_dat_34]
    # Verzeichnis Wörterbücher
    dc_verz_0, dc_verz_1, dc_verz_2, dc_verz_3 = {}, {}, {}, {}
    for dc_i, ls_i in [[dc_verz_0, ls_verz_0], [dc_verz_1, ls_verz_1],
                       [dc_verz_2, ls_verz_2], [dc_verz_3, ls_verz_3]]:
        dc_i["PFAD"] = ls_i[0]
        dc_i["VERZEICHNISANZAHL"] = ls_i[1]
        dc_i["VERZEICHNISLISTE"] = ls_i[2]
        dc_i["DATEIANZAHL"] = ls_i[3]
        dc_i["TYPANZAHL"] = ls_i[4]
    # Dateilisten den Verzeichnissen zuweisen
    for dc_i, ls_i in [[dc_verz_0, []],
                       [dc_verz_1, ls_dateien_1],
                       [dc_verz_2, ls_dateien_2],
                       [dc_verz_3, ls_dateien_3]]:
        dc_i["DATEILISTE"] = ls_i
    # Dateistruktur zusammenstellen
    dc_test_ausgabe = {"STAMMPFAD": ls_test_ausgabe[0],
                       "DATUM": ls_test_ausgabe[1],
                       "VERZEICHNISANZAHL": ls_test_ausgabe[2],
                       "DATEIANZAHL": ls_test_ausgabe[3],
                       "TYPANZAHL": ls_test_ausgabe[4],
                       "VERZEICHNISSE": [dc_verz_0, dc_verz_1,
                                         dc_verz_2, dc_verz_3]}
    # Testliste definieren, [[Schlüssel, Wert], ]
    ls_testdaten = [
        ["DATEISTRUKTUR", dc_test_ausgabe],
        ["AUSGABELISTE", ls_test_ausgabe]
    ]
    # Test Wörterbuch
    dc_daten = {}
    for ls_t in ls_testdaten:
        dc_daten[ls_t[0]] = ls_t[1]
    # Wörterbuch setzen
    ob_ausgabe.m_set_dc(dc_daten)
    '''
    GET WÖRTERBUCH testen
    '''
    tx_test = "StrukturAusgabe.m_get_dc()"
    f_testtitel(tx_test)
    dc_daten = ob_ausgabe.m_get_dc()
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
    tx_test = "StrukturAusgabe.m_clear()"
    f_testtitel(tx_test)
    ob_ausgabe.m_clear()
    # Testliste definieren, [[Atribut, Wert], ]
    ls_testdaten = [
        ["StrukturAusgabe.dc_struktur", {}],
        ["StrukturAusgabe.ls_ausgabe", []]
    ]
    # Testliste durchlaufen
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: '{0}'".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_ausgabe, tx_t)
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
    # Ausgabeliste neu definieren
    # Dateilisten
    ls_dat_01 = ["Datei_01", ".tyD", "26.12.2021 14:21:00", 800]
    ls_dat_11 = ["Datei_11", ".tyA", "26.12.2021 14:18:00", 160]
    ls_dat_12 = ["Datei_12", ".tyB", "26.12.2021 14:19:00", 320]
    ls_dat_13 = ["Datei_13", ".tyB", "26.12.2021 14:20:00", 640]
    ls_dat_21 = ["Datei_21", ".tyC", "26.12.2021 14:22:00", 960]
    ls_dat_22 = ["Datei_22", ".tyC", "26.12.2021 14:23:00", 1120]
    ls_dat_23 = ["Datei_23", ".tyD", "26.12.2021 14:24:00", 1280]
    ls_dat_24 = ["Datei_24", ".tyE", "26.12.2021 14:25:00", 1440]
    # Verzeichnislisten
    ls_verz_0 = ["/stamm", 2, ["verz1", "verz2"], 1, 1, [ls_dat_01]]
    ls_verz_1 = ["/stamm/verz1", 0, [], 3, 2, [ls_dat_11, ls_dat_12,
                 ls_dat_13]]
    ls_verz_2 = ["/stamm/verz2", 0, [], 4, 3, [ls_dat_21, ls_dat_22,
                 ls_dat_23, ls_dat_24]]
    # Ausgabeliste zusammenstellen
    ls_test_ausg2 = ["/stamm2", "03.01.2022 13:10:00", 3, 8, 5,
                     [ls_verz_0, ls_verz_1, ls_verz_2]]
    # Datistruktur JSON definieren
    # Datei-Informationen
    dc_dat_01 = {}
    dc_dat_11, dc_dat_12, dc_dat_13 = {}, {}, {}
    dc_dat_21, dc_dat_22, dc_dat_23, dc_dat_24 = {}, {}, {}, {}
    for dc_i, ls_i in [[dc_dat_01, ls_dat_01], [dc_dat_11, ls_dat_11],
                       [dc_dat_12, ls_dat_12], [dc_dat_13, ls_dat_13],
                       [dc_dat_21, ls_dat_21], [dc_dat_22, ls_dat_22],
                       [dc_dat_23, ls_dat_23], [dc_dat_24, ls_dat_24]]:
        dc_i["NAME"] = ls_i[0]
        dc_i["TYP"] = ls_i[1]
        dc_i["DATUM"] = ls_i[2]
        dc_i["GROESSE"] = ls_i[3]
    # Dateilisten
    ls_dateien_0 = [dc_dat_01]
    ls_dateien_1 = [dc_dat_11, dc_dat_12, dc_dat_13]
    ls_dateien_2 = [dc_dat_21, dc_dat_22, dc_dat_23, dc_dat_24]
    # Verzeichnis Wörterbücher
    dc_verz_0, dc_verz_1, dc_verz_2 = {}, {}, {}
    for dc_i, ls_i in [[dc_verz_0, ls_verz_0], [dc_verz_1, ls_verz_1],
                       [dc_verz_2, ls_verz_2]]:
        dc_i["PFAD"] = ls_i[0]
        dc_i["VERZEICHNISANZAHL"] = ls_i[1]
        dc_i["VERZEICHNISLISTE"] = ls_i[2]
        dc_i["DATEIANZAHL"] = ls_i[3]
        dc_i["TYPANZAHL"] = ls_i[4]
    # Dateilisten den Verzeichnissen zuweisen
    for dc_i, ls_i in [[dc_verz_0, ls_dateien_0],
                       [dc_verz_1, ls_dateien_1],
                       [dc_verz_2, ls_dateien_2]]:
        dc_i["DATEILISTE"] = ls_i
    # Dateistruktur zusammenstellen
    dc_test_ausg2 = {"STAMMPFAD": ls_test_ausgabe[0],
                     "DATUM": ls_test_ausgabe[1],
                     "VERZEICHNISANZAHL": ls_test_ausgabe[2],
                     "DATEIANZAHL": ls_test_ausgabe[3],
                     "TYPANZAHL": ls_test_ausgabe[4],
                     "VERZEICHNISSE": [dc_verz_0, dc_verz_1,
                                       dc_verz_2]}
    # Testliste definieren, [[Attribut, Wert], ]
    ls_testdaten = [
        ["StrukturAusgabe.dc_struktur", dc_test_ausg2],
        ["StrukturAusgabe.ls_ausgabe", ls_test_ausg2]
    ]
    ob_ausgabe.dc_struktur = ls_testdaten[0][1]
    ob_ausgabe.ls_ausgabe = ls_testdaten[1][1]
    '''
    Werte direkt abfragen
    '''
    tx_test = "Werte direkt abfragen"
    f_testtitel(tx_test)
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: '{0}'".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_ausgabe, tx_t)
        # Test
        bl_test = vl_w == vl_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(vl_r))
    '''
    AUSGABELISTE testen
    '''
    tx_test = "StrukturAusgabe.m_ausgabeliste()"
    f_testtitel(tx_test)
    ob_ausgabe.dc_struktur = dc_test_ausg2
    ob_ausgabe.m_ausgabeliste()
    # Vorgabe
    ls_w = ls_test_ausg2
    # Resultat
    ls_r = ob_ausgabe.ls_ausgabe
    # Test
    bl_test = vl_w == vl_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(ls_w), str(ls_r))
    '''
    STRUKTUR testen
    '''
    tx_test = "StrukturAusgabe.m_struktur()"
    f_testtitel(tx_test)
    ob_ausgabe.m_struktur()
    # Vorgabe
    ls_w = ls_test_ausg2
    # Resultat
    ls_r = ob_ausgabe.ls_ausgabe
    # Test
    bl_test = vl_w == vl_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(ls_w), str(ls_r))
    '''
    VERZEICHNIS testen
    '''
    tx_test = "StrukturAusgabe.m_verzeichnis()"
    f_testtitel(tx_test)
    ob_ausgabe.m_verzeichnis()
    # Vorgabe
    ls_w = ls_test_ausg2
    # Resultat
    ls_r = ob_ausgabe.ls_ausgabe
    # Test
    bl_test = vl_w == vl_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(ls_w), str(ls_r))
    '''
    DATEILISTE testen
    '''
    tx_test = "StrukturAusgabe.m_dateiliste()"
    f_testtitel(tx_test)
    # Vorgabe
    ls_w = [ls_dat_21, ls_dat_22, ls_dat_23, ls_dat_24]
    # Resultat
    ls_r = ob_ausgabe.m_dateiliste(ls_dateien_2)
    # Grössen von Text zu Integer konvertieren
    for ls_i in ls_r:
        ls_i[3] = int(ls_i[3])
    # Test
    bl_test = ls_w == ls_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(ls_w), str(ls_r))
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
