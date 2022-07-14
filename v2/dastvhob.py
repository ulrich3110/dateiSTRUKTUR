#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *

'''
dastvhob.py - dateiSTRUKTUR, Vergleich HTML Ausgabe, Objektmodul
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


class HtmlVergleich():
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
            "HTMLPFAD": '',
            "TITEL": '',
            "TEXT": '',
            "VERGLEICHJSON": {},
            "HTML": ''
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Verzeichnis in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "JSONPFAD": self.tx_jsonpfad,
            "HTMLPFAD": self.tx_htmlpfad,
            "TITEL": self.tx_titel,
            "TEXT": self.tx_text,
            "VERGLEICHJSON": self.dc_vergleich,
            "HTML": self.tx_html
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Verzeichnis aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_jsonpfad = dc_daten["JSONPFAD"]
        self.tx_htmlpfad = dc_daten["HTMLPFAD"]
        self.tx_titel = dc_daten["TITEL"]
        self.tx_text = dc_daten["TEXT"]
        self.dc_vergleich = dc_daten["VERGLEICHJSON"]
        self.tx_html = dc_daten["HTML"]

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
        # Head, Body, Titel, Text
        self.tx_html = "".join([
            '<!DOCTYPE html><html>',
            '<head>',
            '<style>table, th, td ',
            '{padding: 3px; ',
            'border: 1px solid black; '
            'border-collapse: collapse;}',
            '#left {text-align: left;}',
            '#right {text-align: right;}',
            '</style></head>',
            '<body>',
            "<h1>", self.tx_titel, "<br>",
            "<small>", self.tx_text, "</small></h1><br>"
        ])

    def m_ende(self):
        ''' HTML Datei-Struktur Ende '''
        print("# {0}.m_ende #".format(self.tx_objname))
        # Body end
        self.tx_html = "".join([
            self.tx_html,
            '</table></body></html>'
        ])

    def m_save(self):
        ''' HTML Datei-Struktur speichern '''
        print("# {0}.m_save #".format(self.tx_objname))
        # HTML speichern
        f_savetext(self.tx_htmlpfad, self.tx_html)

    def m_zusammenfassung(self):
        ''' HTML Vergleich Zusammenfassung '''
        print("# {0}.m_zusammenfassung #".format(self.tx_objname))
        # Mit Tabelle beginnen
        self.tx_html = "".join([
            self.tx_html,
            '<table><tr>',
            '<th style = "text-align: left">Kategorie</th>',
            '<th style = "text-align: right">Quelle</th>',
            '<th style = "text-align: right">Ziel</th>',
            '</tr>'
        ])
        # Pfad
        self.tx_html = "".join([
            self.tx_html,
            '<tr>',
            '<td>Pfad</td>',
            '<td style = "text-align: right">',
            self.dc_vergleich["STAMMPFAD_QUELLE"], '</td>',
            '<td style = "text-align: right">',
            self.dc_vergleich["STAMMPFAD_ZIEL"], '</td>',
            '</tr>'
        ])
        # Erfassungsdatum
        self.tx_html = "".join([
            self.tx_html,
            '<tr>',
            '<td>Erfassungsdatum</td>',
            '<td style = "text-align: right">',
            self.dc_vergleich["DATUM_STRUKTUR_QUELLE"], '</td>',
            '<td style = "text-align: right">',
            self.dc_vergleich["DATUM_STRUKTUR_ZIEL"], '</td>',
            '</tr>'
        ])
        # Anzahl Dateien
        self.tx_html = "".join([
            self.tx_html,
            '<tr>',
            '<td>Anzahl Dateien</td>',
            '<td style = "text-align: right">',
            str(self.dc_vergleich["ANZAHL_DATEIEN_QUELLE"]), '</td>',
            '<td style = "text-align: right">',
            str(self.dc_vergleich["ANZAHL_DATEIEN_ZIEL"]), '</td>',
            '</tr>'
        ])
        # Anzahl Verzeichnisse
        self.tx_html = "".join([
            self.tx_html,
            '<tr>',
            '<td>Anzahl Verzeichnisse</td>',
            '<td style = "text-align: right">',
            str(self.dc_vergleich["ANZAHL_VERZEICHNISSE_QUELLE"]),
            '</td>',
            '<td style = "text-align: right">',
            str(self.dc_vergleich["ANZAHL_VERZEICHNISSE_ZIEL"]),
            '</td>',
            '</tr>'
        ])
        # Anzahl Typen
        self.tx_html = "".join([
            self.tx_html,
            '<tr>',
            '<td>Anzahl Typen</td>',
            '<td style = "text-align: right">',
            str(self.dc_vergleich["ANZAHL_TYPEN_QUELLE"]), '</td>',
            '<td style = "text-align: right">',
            str(self.dc_vergleich["ANZAHL_TYPEN_ZIEL"]), '</td>',
            '</tr>'
        ])

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
            self.tx_html = "".join([
                self.tx_html,
                '<tr>',
                '<td colspan="3"><b>', tx_titel, '</b></td>',
                '</tr>',
                '<tr>',
                '<td><small><b>Kategorie</b></small></td>',
                '<td style = "text-align: right"><small><b>Quelle',
                '</b></small></td>',
                '<td style = "text-align: right"><small><b>Ziel',
                '</b></small></td>',
                '</tr>'
            ])
            # Gemeinsam, Quelle, Ziel
            for tx_beschr, tx_key in ls_gemquezie:
                # Vergleich abrufen
                if self.dc_vergleich[tx_key]:
                    # Einträge durchlaufen und anhägen
                    tx_zelle = ""
                    for tx_name in self.dc_vergleich[tx_key]:
                        tx_zelle = "".join([
                            tx_zelle, tx_name, "<br>"
                        ])
                    # Letzter Zeilenumbruch entfernen
                    tx_zelle = tx_zelle[:len(tx_zelle) - 4]
                else:
                    # Info nichts
                    tx_zelle = "keine vorhanden"
                tx_ende = tx_key[len(tx_key) - 9:]
                if tx_ende == "GEMEINSAM":
                    # Gemeinsame Elemente anhängen
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td>', tx_beschr, '</td>',
                        '<td style = "text-align: center" colspan="2">',
                        tx_zelle, '</td>',
                        '</tr>'
                    ])
                elif tx_ende == "UR_QUELLE":
                    # Elemente Quelle anhängen
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td>', tx_beschr, '</td>',
                        '<td style = "text-align: right">', tx_zelle,
                        '</td>',
                        '<td> </td>',
                        '</tr>'
                    ])
                elif tx_ende == "_NUR_ZIEL":
                    # Elemente Ziel anhängen
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td>', tx_beschr, '</td>',
                        '<td> </td>',
                        '<td style = "text-align: right">', tx_zelle,
                        '</td>',
                        '</tr>'
                    ])

    def m_dateiinfo(self):
        ''' HTML Vergleich unterschiedliche Datei-Informationen '''
        print("# {0}.m_dateiinfo #".format(self.tx_objname))
        # Überschrift
        self.tx_html = "".join([
            self.tx_html,
            '<tr>',
            '<td colspan="3"><b>Gleiche Dateipfade mit ',
            'unterschiedlicher Dateigrösse / Datum</b></td>',
            '</tr>'
        ])
        # Unterschiedliche Datei-Info durchlaufen
        for tx_pfad, ls_info in self.dc_vergleich[
            "UNTERSCHIEDLICHE_INFO"
        ].items():
            # Informationen anhängen
            self.tx_html = "".join([
                self.tx_html,
                '<tr>',
                '<td>', tx_pfad, '</td>',
                '<td style = "text-align: right">', str(ls_info[1]),
                ' bytes<br>',
                ls_info[0], '</td>',
                '<td style = "text-align: right">', str(ls_info[3]),
                ' bytes<br>',
                ls_info[2], '</td>',
                '</tr>'
            ])
