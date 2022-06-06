#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *

'''
dastscob.py - dateiSTRUKTUR, Struktur CSV Ausgabe, Objektmodul
Copyright (c) Andreas Ulrich, <http://erasand.ch>, <andreas@erasand.ch>

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


class CsvStruktur():
    ''' Aus einem Datei-Stuktur JSON eine CSV Tabelle erstellen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "CsvStruktur"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        tx_info = " ".join([
            "# TITEL:", self.tx_titel, " | ",
            "TEXT:", self.tx_text, "#"
        ])
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "JSONPFAD": '',
            "CSVPFAD": '',
            "TITEL": '',
            "TEXT": '',
            "AUSGABEJSON": {},
            "CSV": []
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Verzeichnis in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "JSONPFAD": self.tx_jsonpfad,
            "CSVPFAD": self.tx_csvpfad,
            "TITEL": self.tx_titel,
            "TEXT": self.tx_text,
            "AUSGABEJSON": self.dc_ausgabe,
            "CSV": self.ls_csv
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Verzeichnis aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_jsonpfad = dc_daten["JSONPFAD"]
        self.tx_csvpfad = dc_daten["CSVPFAD"]
        self.tx_titel = dc_daten["TITEL"]
        self.tx_text = dc_daten["TEXT"]
        self.dc_ausgabe = dc_daten["AUSGABEJSON"]
        self.ls_csv = dc_daten["CSV"]

    def m_loadjsonor(self):
        ''' Ausgabestruktur JSON laden  '''
        print("# {0}.m_loadjsonor #".format(self.tx_objname))
        # Ausgabestruktur laden
        dc_datei = f_loadjson(self.tx_jsonpfad)
        # Struktur prüfen
        if dc_datei["DASTJSON"] == "STRUKTURAUSGABE":
            # Strukturausgabe JSON übernehmen
            self.dc_ausgabe = dc_datei
        else:
            # Kein Strukturausgabe JSON
            tx_t = " ".join([
                "# Die Datei",
                self.tx_jsonpfad,
                "ist kein STRUKTURAUSGABE Format #"
            ])
            print(tx_t)

    def m_save(self):
        ''' CSV Datei-Struktur speichern '''
        print("# {0}.m_save #".format(self.tx_objname))
        # CSV speichern
        f_savecsv(self.tx_csvpfad, self.ls_csv)

    def m_anfang(self):
        ''' CSV Datei-Struktur Anfang '''
        print("# {0}.m_anfang #".format(self.tx_objname))
        # Zeilenzähler zurücksetzen
        self.in_zeile = 1
        # Spaltenüberschriften
        self.ls_csv = [[
            "Zeile",
            "Kategorie",
            "Text",
            "Anzahl",
            "Verzeichnisnamen",
            "Dateiname",
            "Dateityp",
            "Datum/Uhrzeit",
            "Groesse (bytes)"
        ]]
        # Titel und Text
        self.ls_csv.extend([
            [
                self.in_zeile,
                "Titel",
                self.tx_titel,
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 1,
                "Beschrieb",
                self.tx_text,
                "",
                "",
                "",
                "",
                "",
                ""
            ]
        ])
        self.in_zeile += 2

    def m_struktur(self):
        ''' CSV Datei-Struktur Zusammenfassung '''
        print("# {0}.m_struktur #".format(self.tx_objname))
        # Zusammenfassung: Pfad, Datum, Anzahl Verzeichnisse,
        # Anzahl Dateien, Anzahl Dateitypen
        self.ls_csv.extend([
            [
                self.in_zeile,
                "Hauptverzeichnis",
                "",
                "",
                self.dc_ausgabe["STAMMPFAD"],
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 1,
                "Datum / Uhrzeit",
                "",
                "",
                "",
                "",
                "",
                self.dc_ausgabe["DATUM"],
                ""
            ],
            [
                self.in_zeile + 2,
                "Anzahl Verzeichnisse",
                "",
                self.dc_ausgabe["VERZEICHNISANZAHL"],
                "",
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 3,
                "Anzahl Dateien",
                "",
                self.dc_ausgabe["DATEIANZAHL"],
                "",
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 4,
                "Anzahl Dateitypen",
                "",
                self.dc_ausgabe["TYPENANZAHL"],
                "",
                "",
                "",
                "",
                ""
            ],
        ])
        self.in_zeile += 5

    def m_verzeichnisse(self):
        ''' HTML Datei-Struktur Verzeichnis '''
        print("# {0}.m_verzeichnisse #".format(self.tx_objname))
        # Verzeichnisliste sortiert durchlaufen
        ls_verzsort = list(self.dc_ausgabe["VERZEICHNISSE"])
        ls_verzsort.sort()
        for ls_ver in ls_verzsort:
            # Verzeichnis: Pfad, Anzahl Verzeichnisse
            if ls_ver[0] == ".":
                # Stammverzeichnis
                tx_verpfad = 'Hauptverzeichnis'
            else:
                # Ein Unterverzeichnis
                tx_verpfad = ls_ver[0]
            # Leerzeile
            self.ls_csv.extend([
                [
                    self.in_zeile,
                    "Leerzeile",
                    "---",
                    "---",
                    "---",
                    "---",
                    "---",
                    "---",
                    "---"
                ]
            ])
            self.in_zeile += 1
            # Verzeichnispfad und Anzahl Unterverzeichnisse
            tx_anzver = str(len(ls_ver[2]))
            self.ls_csv.extend([
                [
                    self.in_zeile,
                    "Verzeichnis",
                    "",
                    "",
                    tx_verpfad,
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    self.in_zeile + 1,
                    "Anzahl Verzeichnisse",
                    "",
                    tx_anzver,
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            ])
            self.in_zeile += 2
            # Prüfen ob Subverzeichnisse vorhanden sind
            if ls_ver[2]:
                # Mit Verzeichnisliste Tabelle beginnen
                index = 1
                # Verzeichnisliste durchlaufen
                for tx_verz in ls_ver[2]:
                    self.ls_csv.extend([
                        [
                            self.in_zeile,
                            "Verzeichnis #{0}".format(index),
                            "",
                            "",
                            tx_verz,
                            "",
                            "",
                            "",
                            ""
                        ]
                    ])
                    index += 1
                    self.in_zeile += 1
            # Anzahl Dateien, Anzahl Dateitypen
            tx_anzdat = str(len(ls_ver[1]))
            tx_anztyp = str(len(ls_ver[3]))
            self.ls_csv.extend([
                [
                    self.in_zeile,
                    "Anzahl Dateien",
                    "",
                    tx_anzdat,
                    "",
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    self.in_zeile + 1,
                    "Anzahl Dateitypen",
                    "",
                    tx_anztyp,
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            ])
            self.in_zeile += 2
            # Prüfen ob Dateien vorhanden sind
            if ls_ver[1]:
                # Mit Dateilisten Tabelle beginnen
                index = 1
                # Dateiliste durchlaufen
                for tx_pfad, ls_info in ls_ver[1].items():
                    # Dateiname mit Informationen
                    ls_pfad = os.path.splitext(tx_pfad)
                    tx_name = ls_pfad[0]
                    tx_typ = ls_pfad[1]
                    self.ls_csv.extend([
                        [
                            self.in_zeile,
                            "Datei #{0}".format(index),
                            "",
                            "",
                            "",
                            tx_name,
                            tx_typ,
                            ls_info[0],
                            ls_info[1]
                        ]
                    ])
                    index += 1
                    self.in_zeile += 1
