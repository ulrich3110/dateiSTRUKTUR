#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *

'''
dastshob.py - dateiSTRUKTUR, Struktur HTML Ausgabe, Objektmodul
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


class HtmlStruktur():
    ''' Aus einem Datei-Stuktur JSON ein HTML Dokument erstellen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "HtmlStrukturNeu"
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
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "JSONPFAD": '',
            "HTMLPFAD": '',
            "TITEL": '',
            "TEXT": '',
            "AUSGABEJSON": {},
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
            "AUSGABEJSON": self.dc_ausgabe,
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
        self.dc_ausgabe = dc_daten["AUSGABEJSON"]
        self.tx_html = dc_daten["HTML"]

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
        self.tx_html = "".join([self.tx_html, '</body></html>'])

    def m_save(self):
        ''' HTML Datei-Struktur speichern '''
        print("# {0}.m_save #".format(self.tx_objname))
        # HTML speichern
        f_savetext(self.tx_htmlpfad, self.tx_html)

    def m_struktur(self):
        ''' HTML Datei-Struktur Zusammenfassung '''
        print("# {0}.m_struktur #".format(self.tx_objname))
        # Zusammenfassung: Pfad, Datum, Anzahl Verzeichnisse,
        # Anzahl Dateien, Anzahl Dateitypen
        self.tx_html = "".join([
            self.tx_html,
            '<h2>Zusammenfassung: ', self.dc_ausgabe["STAMMPFAD"],
            '</h2>',
            '<p>Datum / Uhrzeit: ', self.dc_ausgabe["DATUM"],
            '</p>',
            '<p>Anzahl Verzeichnisse: ',
            str(self.dc_ausgabe["VERZEICHNISANZAHL"]), '</p>',
            '<p>Anzahl Dateien: ',
            str(self.dc_ausgabe["DATEIANZAHL"]), '</p>',
            '<p>Anzahl Dateitypen: ',
            str(self.dc_ausgabe["TYPENANZAHL"]), '</p>'
        ])

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
                tx_verpfad = '<i>Hauptverzeichnis</i>'
            else:
                # Ein Unterverzeichnis
                tx_verpfad = ls_ver[0]
            # Verzeichnispfad und Anzahl Unterverzeichnisse
            tx_anzver = str(len(ls_ver[2]))
            self.tx_html = "".join([
                self.tx_html,
                '<h2>Verzeichnis: ', tx_verpfad,
                '</h2>',
                '<p>Anzahl Verzeichnisse: ', tx_anzver,
                '</p>'
            ])
            # Prüfen ob Subverzeichnisse vorhanden sind
            if ls_ver[2]:
                # Mit Verzeichnisliste Tabelle beginnen
                self.tx_html = "".join([
                    self.tx_html,
                    '<table><tr>',
                    '<th id="left">Verzeichnisname</th>',
                    '</tr>'
                ])
                # Verzeichnisliste durchlaufen
                for tx_verz in ls_ver[2]:
                    # Verzeichnisnamen
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td id="left">', tx_verz, '</td>',
                        '</tr>'
                    ])
                # Tabellen Ende Verzeichnisliste
                self.tx_html = "".join([self.tx_html, "</table>"])
            # Anzahl Dateien, Anzahl Dateitypen
            tx_anzdat = str(len(ls_ver[1]))
            tx_anztyp = str(len(ls_ver[3]))
            self.tx_html = "".join([
                self.tx_html,
                '<p>Anzahl Dateien: ', tx_anzdat,
                '</p>',
                '<p>Anzahl Dateitypen: ', tx_anztyp,
                '</p>'
            ])
            # Prüfen ob Dateien vorhanden sind
            if ls_ver[1]:
                # Mit Dateilisten Tabelle beginnen
                self.tx_html = "".join([
                    self.tx_html,
                    '<table><tr>',
                    '<th id="left">Dateiname</th>',
                    '<th id="left">Dateityp</th>',
                    '<th id="left"><small>Datum/Uhrzeit</small></th>',
                    '<th id="right"><small>Groesse (bytes)</small></th>',
                    '</tr>'
                ])
                # Dateiliste durchlaufen
                for tx_pfad, ls_info in ls_ver[1].items():
                    # Dateiname mit Informationen
                    ls_pfad = os.path.splitext(tx_pfad)
                    tx_name = ls_pfad[0]
                    tx_typ = ls_pfad[1]
                    tx_groesse = str(ls_info[1])
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td id="left">', tx_name, '</td>',
                        '<td id="left">', tx_typ, '</td>',
                        '<td id="left"><small>', ls_info[0],
                        '</small></td>',
                        '<td id="right"><small>', tx_groesse,
                        '</small></td>',
                        '</tr>'
                    ])
                # Tabellen Ende
                self.tx_html = "".join([self.tx_html, "</table>"])
