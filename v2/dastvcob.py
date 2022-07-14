#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *

'''
dastvcob.py - dateiSTRUKTUR, Vergleich CSV Ausgabe, Objektmodul
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


class CsvVergleich():
    ''' Aus einem Vergleich JSON ein HTML Dokument erstellen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "HtmlVergleich"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        tx_info = " ".join([
            "# TITEL:", self.tx_titel, "|",
            "TEXT:", self.tx_text, "#"
        ])
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.m_clear #".format(self.tx_objname))
        dc_clear = {
            "JSONPFAD": '',
            "CSVPFAD": '',
            "TITEL": '',
            "TEXT": '',
            "VERGLEICHJSON": {},
            "CSV": []
        }
        self.in_zeile = 0
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Verzeichnis in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "JSONPFAD": self.tx_jsonpfad,
            "CSVPFAD": self.tx_csvpfad,
            "TITEL": self.tx_titel,
            "TEXT": self.tx_text,
            "VERGLEICHJSON": self.dc_vergleich,
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
        self.dc_vergleich = dc_daten["VERGLEICHJSON"]
        self.ls_csv = dc_daten["CSV"]

    def m_loadjsonvg(self):
        ''' Vergleich JSON laden  '''
        print("# {0}.m_loadjsonvg #".format(self.tx_objname))
        # Ausgabestruktur laden
        dc_datei = f_loadjson(self.tx_jsonpfad)
        # Struktur prüfen
        if dc_datei["DASTJSON"] == "VERGLEICHSTRUKTUR":
            # Strukturausgabe JSON übernehmen
            self.dc_vergleich = dc_datei
        else:
            # Kein Strukturausgabe JSON
            tx_t = " ".join([
                "# Die Datei",
                self.tx_jsonpfad,
                "ist kein VERGLEICHSTRUKTUR Format #"
            ])
            print(tx_t)

    def m_anfang(self):
        ''' HTML Datei-Struktur Anfang '''
        print("# {0}.m_anfang #".format(self.tx_objname))
        # Zeilenzähler zurücksetzen
        self.in_zeile = 1
        # Spaltenüberschriften
        self.ls_csv = [[
            'Zeile',
            'Kategorie',
            'Text',
            'Anzahl Quelle',
            'Anzahl Ziel',
            'Pfad Quelle',
            'Pfad Ziel',
            'Datum/Uhrzeit Quelle',
            'Datum/Uhrzeit Ziel',
            'Groesse Quelle (bytes)',
            'Groesse Ziel (bytes)'
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
                "",
                "",
                ""
            ]
        ])
        self.in_zeile += 2

    def m_save(self):
        ''' HTML Datei-Struktur speichern '''
        print("# {0}.m_save #".format(self.tx_objname))
        # CSV speichern
        f_savecsv(self.tx_csvpfad, self.ls_csv)

    def m_zusammenfassung(self):
        ''' HTML Vergleich Zusammenfassung '''
        print("# {0}.m_zusammenfassung #".format(self.tx_objname))
        # Zusammenfassung: Pfad, Datum, Anzahl Verzeichnisse,
        # Anzahl Dateien, Anzahl Dateitypen
        self.ls_csv.extend([
            [
                self.in_zeile,
                "Pfad",
                "",
                "",
                "",
                self.dc_vergleich["STAMMPFAD_QUELLE"],
                self.dc_vergleich["STAMMPFAD_ZIEL"],
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 1,
                "Erfassungsdatum",
                "",
                "",
                "",
                "",
                "",
                self.dc_vergleich["DATUM_STRUKTUR_QUELLE"],
                self.dc_vergleich["DATUM_STRUKTUR_ZIEL"],
                "",
                ""
            ],
            [
                self.in_zeile + 2,
                "Anzahl Dateien",
                "",
                self.dc_vergleich["ANZAHL_DATEIEN_QUELLE"],
                self.dc_vergleich["ANZAHL_DATEIEN_ZIEL"],
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 3,
                "Anzahl Verzeichnisse",
                "",
                self.dc_vergleich["ANZAHL_VERZEICHNISSE_QUELLE"],
                self.dc_vergleich["ANZAHL_VERZEICHNISSE_ZIEL"],
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 4,
                "Anzahl Typen",
                "",
                self.dc_vergleich["ANZAHL_TYPEN_QUELLE"],
                self.dc_vergleich["ANZAHL_TYPEN_ZIEL"],
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            [
                self.in_zeile + 5,
                "---",
                "---",
                "---",
                "---",
                "---",
                "---",
                "---",
                "---",
                "---",
                "---"
            ]
        ])
        self.in_zeile += 6

    def m_namvertyp(self):
        ''' HTML Vergleich nach Namen, Verzeichnisse, Typen '''
        print("# {0}.m_namvertyp #".format(self.tx_objname))
        # Tabelle weiterfahren mit Vergleich nach Pfaden
        ls_namvertyp = [
            [
                "Vergleich nach Dateipfaden",
                ["Gemeinsame Dateipfade", "DATEIEN_GEMEINSAM"],
                ["Dateipfade nur in der Quelle", "DATEIEN_NUR_QUELLE"],
                ["Dateipfade nur im Ziel", "DATEIEN_NUR_ZIEL"]
            ],
            [
                "Vergleich nach Verzeichnispfaden",
                ["Gemeinsame Verzeichnispfade",
                 "VERZEICHNISSE_GEMEINSAM"],
                ["Verzeichnispfade nur in der Quelle",
                 "VERZEICHNISSE_NUR_QUELLE"],
                ["Verzeichnispfade nur im Ziel",
                 "VERZEICHNISSE_NUR_ZIEL"]
            ],
            [
                "Vergleich nach Dateitypen",
                ["Gemeinsame Dateitypen", "TYPEN_GEMEINSAM"],
                ["Dateitypen nur in der Quelle", "TYPEN_NUR_QUELLE"],
                ["Dateitypen nur im Ziel", "TYPEN_NUR_ZIEL"]
            ]
        ]
        # Nach Dateipfaden, Verzeichnispfaden, Dateitypen
        for ls_i in ls_namvertyp:
            # Titel und Liste für Gemeinsam, Quelle, Ziel
            tx_titel = ls_i[0]
            ls_gemquezie = [ls_i[1], ls_i[2], ls_i[3]]
            # Überschrift
            self.ls_csv.extend([
                [
                    self.in_zeile,
                    tx_titel,
                    "---",
                    "---",
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
            # Gemeinsam, Quelle, Ziel
            for tx_beschr, tx_key in ls_gemquezie:
                # Ende als Identifaktor, in welche Spalten die Einträge
                # geschrieben werden sollen.
                tx_ende = tx_key[len(tx_key) - 9:]
                if tx_ende == "GEMEINSAM":
                    # Gemeinsame Elemente anhängen
                    if self.dc_vergleich[tx_key]:
                        # Einträge durchlaufen und anhängen
                        for tx_name in self.dc_vergleich[tx_key]:
                            self.ls_csv.extend([
                                [
                                    self.in_zeile,
                                    tx_beschr,
                                    "",
                                    "",
                                    "",
                                    tx_name,
                                    tx_name,
                                    "",
                                    "",
                                    "",
                                    ""
                                ]
                            ])
                            self.in_zeile += 1
                    else:
                        # Info nichts:
                        self.ls_csv.extend([
                            [
                                self.in_zeile,
                                tx_beschr,
                                "",
                                "",
                                "",
                                "keine vorhanden",
                                "keine vorhanden",
                                "",
                                "",
                                "",
                                ""
                            ]
                        ])
                        self.in_zeile += 1
                elif tx_ende == "UR_QUELLE":
                    # Elemente Quelle anhängen
                    if self.dc_vergleich[tx_key]:
                        # Einträge durchlaufen und anhängen
                        for tx_name in self.dc_vergleich[tx_key]:
                            self.ls_csv.extend([
                                [
                                    self.in_zeile,
                                    tx_beschr,
                                    "",
                                    "",
                                    "",
                                    tx_name,
                                    "",
                                    "",
                                    "",
                                    "",
                                    ""
                                ]
                            ])
                            self.in_zeile += 1
                    else:
                        # Info nichts:
                        self.ls_csv.extend([
                            [
                                self.in_zeile,
                                tx_beschr,
                                "",
                                "",
                                "",
                                "keine vorhanden",
                                "",
                                "",
                                "",
                                "",
                                ""
                            ]
                        ])
                        self.in_zeile += 1
                elif tx_ende == "_NUR_ZIEL":
                    # Elemente Ziel anhängen
                    if self.dc_vergleich[tx_key]:
                        # Einträge durchlaufen und anhängen
                        for tx_name in self.dc_vergleich[tx_key]:
                            self.ls_csv.extend([
                                [
                                    self.in_zeile,
                                    tx_beschr,
                                    "",
                                    "",
                                    "",
                                    "",
                                    tx_name,
                                    "",
                                    "",
                                    "",
                                    ""
                                ]
                            ])
                            self.in_zeile += 1
                    else:
                        # Info nichts:
                        self.ls_csv.extend([
                            [
                                self.in_zeile,
                                tx_beschr,
                                "",
                                "",
                                "",
                                "",
                                "keine vorhanden",
                                "",
                                "",
                                "",
                                ""
                            ]
                        ])
                        self.in_zeile += 1

    def m_dateiinfo(self):
        ''' HTML Vergleich unterschiedliche Datei-Informationen '''
        print("# {0}.m_dateiinfo #".format(self.tx_objname))
        # Überschrift
        self.ls_csv.extend([
            [
                self.in_zeile,
                "".join([
                    "Gleiche Dateipfade mit ",
                    "unterschiedlicher Dateigrösse / Datum"
                ]),
                "---",
                "---",
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
        # Unterschiedliche Datei-Info durchlaufen
        for tx_pfad, ls_info in self.dc_vergleich[
            "UNTERSCHIEDLICHE_INFO"
        ].items():
            # Informationen anhängen
            self.ls_csv.extend([
                [
                    self.in_zeile,
                    "",
                    "",
                    "",
                    "",
                    tx_pfad,
                    tx_pfad,
                    ls_info[0],
                    ls_info[2],
                    ls_info[1],
                    ls_info[3]
                ]
            ])
            self.in_zeile += 1
