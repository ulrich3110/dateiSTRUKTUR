#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_htmlcsv import *
from test_funktionen import *

'''
ds_test_csvstruktur.py - [d]atei[s]strukturen <CsvStruktur> Test
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
    if tx_attribut.endswith("tx_jsonpfad"):
        vl_test = ob_test.tx_jsonpfad
    elif tx_attribut.endswith("tx_csvpfad"):
        vl_test = ob_test.tx_csvpfad
    elif tx_attribut.endswith("tx_titel"):
        vl_test = ob_test.tx_titel
    elif tx_attribut.endswith("tx_text"):
        vl_test = ob_test.tx_text
    elif tx_attribut.endswith("ls_ausgabe"):
        vl_test = ob_test.ls_ausgabe
    elif tx_attribut.endswith("ls_csv"):
        vl_test = ob_test.ls_csv
    # Wert zurückgeben
    return(vl_test)


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    print("DS_TEST_CSVSTRUKTUR")
    print("-------------------")
    print("Objekt:        CsvStruktur")
    print("Methoden:      __init__(), __str__(), m_clear(),")
    print("               m_get_dc(), m_set_dc(<dict>), m_create(),")
    print("               m_titel(), m_save(), m_struktur(),")
    print("               m_verzeichnisse()")
    print("Attribute:     tx_jsonpfad, tx_csvpfad, tx_titel, tx_text,")
    print("               ls_ausgabe, ls_csv")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    '''
    OBJEKT erzeugen
    '''
    tx_test = "CsvStruktur Objekt erzeugen"
    f_testtitel(tx_test)
    ob_csv = CsvStruktur()
    '''
    __STR__ testen
    '''
    tx_test = "CsvStruktur.__str__()"
    f_testtitel(tx_test)
    tx_r = ob_csv.__str__()
    # Vorgabe
    tx_vorgabe = "JSONPFAD"
    # Test
    bl_test = tx_vorgabe in tx_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_vorgabe, tx_r)
    '''
    SET WÖRTERBUCH testen
    '''
    tx_test = "CsvStruktur.m_set_dc(<dict>)"
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
    # Testverzeichnisse als Lisen definieren:
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
    # Testliste definieren, [[Schlüssel, Wert], ]
    ls_testdaten = [
        ["JSONPFAD", "./struktur.json"],
        ["CSVPFAD", "./struktur.csv"],
        ["TITEL", "Struktur"],
        ["TEXT", "Beispiel"],
        ["AUSGABELISTE", ls_test_ausgabe],
        ["CSV", [["Spalte1", "Spalte2"],
                 ["Z1, S1", "Z1, S2"],
                 ["Z2, S1", "Z2, S2"]]]
    ]
    # Test Wörterbuch
    dc_daten = {}
    for ls_t in ls_testdaten:
        dc_daten[ls_t[0]] = ls_t[1]
    # Wörterbuch setzen
    ob_csv.m_set_dc(dc_daten)
    '''
    GET WÖRTERBUCH testen
    '''
    tx_test = "CsvStruktur.m_get_dc()"
    f_testtitel(tx_test)
    dc_daten = ob_csv.m_get_dc()
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
    tx_test = "CsvStruktur.m_clear()"
    f_testtitel(tx_test)
    ob_csv.m_clear()
    # Testliste definieren, [[Atribut, Wert], ]
    ls_testdaten = [
        ["CsvStruktur.tx_jsonpfad", ""],
        ["CsvStruktur.tx_csvpfad", ""],
        ["CsvStruktur.tx_titel", ""],
        ["CsvStruktur.tx_text", ""],
        ["CsvStruktur.ls_ausgabe", []],
        ["CsvStruktur.ls_csv", []]
    ]
    # Testliste durchlaufen
    for ls_t in ls_testdaten:
        # Attribut, Vorgabe, Bezeichnung
        tx_t, vl_w = ls_t
        tx_test = "Attribut: '{0}'".format(tx_t)
        # Attribut abfragen
        vl_r = f_attribute(ob_csv, tx_t)
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
    ls_dat_21 = ["Datei_22", ".tyC", "26.12.2021 14:22:00", 960]
    ls_dat_22 = ["Datei_31", ".tyC", "26.12.2021 14:23:00", 1120]
    ls_dat_23 = ["Datei_32", ".tyD", "26.12.2021 14:24:00", 1280]
    ls_dat_24 = ["Datei_33", ".tyE", "26.12.2021 14:25:00", 1440]
    # Verzecihnislisten
    ls_verz_0 = ["/stamm", 3, ["verz1", "verz2"], 1, 1, [ls_dat_01]]
    ls_verz_1 = ["/stamm/verz1", 0, [], 3, 2, [ls_dat_11, ls_dat_12,
                 ls_dat_13]]
    ls_verz_2 = ["/stamm/verz2", 0, [], 2, 2, [ls_dat_21, ls_dat_22,
                 ls_dat_23, ls_dat_24]]
    # Testliste definieren, [[Attribut, Wert], ]
    ls_testdaten = [
        ["CsvStruktur.tx_jsonpfad", "./strkt2.json"],
        ["CsvStruktur.tx_csvpfad", "./strkt2.csv"],
        ["CsvStruktur.tx_titel", "2. Struktur"],
        ["CsvStruktur.tx_text", "2. Beispiel"],
        ["CsvStruktur.ls_ausgabe", [ls_verz_0, ls_verz_1, ls_verz_2]],
        ["CsvStruktur.ls_csv", [["Titel1", "Titel2"],
                                ["Ze1, Sp1", "Ze1, Sp2"],
                                ["Ze2, Sp1", "Ze2, Sp2"]]]
    ]
    ob_csv.tx_jsonpfad = ls_testdaten[0][1]
    ob_csv.tx_csvpfad = ls_testdaten[1][1]
    ob_csv.tx_titel = ls_testdaten[2][1]
    ob_csv.tx_text = ls_testdaten[3][1]
    ob_csv.ls_ausgabe = ls_testdaten[4][1]
    ob_csv.ls_csv = ls_testdaten[5][1]
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
        vl_r = f_attribute(ob_csv, tx_t)
        # Test
        bl_test = vl_w == vl_r
        # Vergleich
        in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                                str(vl_w), str(vl_r))
    '''
    TITEL testen
    '''
    tx_test = "CsvStruktur.m_titel()"
    f_testtitel(tx_test)
    ob_csv.m_titel()
    # Vorgabe
    ls_w = ["Kategorie", "Anzahl", "Verzeichnisnamen", "Dateiname",
            "Dateityp", "Datum/Uhrzeit", "Groesse (bytes)"]
    # Test
    bl_test = ls_w in ob_csv.ls_csv
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(ls_w), str(ob_csv.ls_csv))
    '''
    SAVE testen
    '''
    tx_test = "CsvStruktur.m_save()"
    f_testtitel(tx_test)
    # Vorgabe
    vl_w = None
    # Resultat
    vl_r = ob_csv.m_save()
    # Test
    bl_test = vl_w == vl_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(vl_w), str(vl_r))
    '''
    CREATE testen
    '''
    tx_test = "CsvStruktur.m_create()"
    f_testtitel(tx_test)
    # Objekt Reset
    ob_csv.m_clear()
    # Werte eintragen
    ob_csv.tx_jsonpfad = "./struktur.json"
    ob_csv.tx_csvpfad = "./struktur.csv"
    ob_csv.tx_titel = "Beispiel"
    ob_csv.tx_text = "Struktur"
    # Vorgabe
    vl_w = None
    # Resultat
    vl_r = ob_csv.m_create()
    # Test
    bl_test = vl_w == vl_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(vl_w), str(vl_r))
    '''
    STRUKTUR testen
    '''
    tx_test = "CsvStruktur.m_struktur()"
    f_testtitel(tx_test)
    ob_csv.m_struktur()
    # Vorgabe
    tx_w = "Zusammenfassung"
    # Test
    bl_test = False
    for ls_zeile in ob_csv.ls_csv:
        if tx_w in ls_zeile:
            bl_test = True
            break
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_w, str(ob_csv.ls_csv))
    '''
    VERZEICHNISSE testen
    '''
    tx_test = "CsvStruktur.m_verzeichnisse()"
    f_testtitel(tx_test)
    ob_csv.m_verzeichnisse()
    # Vorgabe
    tx_w = "Verzeichnis"
    # Test
    bl_test = False
    for ls_zeile in ob_csv.ls_csv:
        if tx_w in ls_zeile:
            bl_test = True
            break
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_w, str(ob_csv.ls_csv))
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
