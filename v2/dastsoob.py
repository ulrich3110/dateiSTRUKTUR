#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *

'''
dastsoob.py - dateiSTRUKTUR, Struktur ordnen für Ausgabe, Objektmodul
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


class StrukturAusgabe():
    ''' Aus einer Datei-Struktur eine Ausgabeliste erzeugen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "StrukturAusgabe"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        tx_info = " ".join([
            "# STAMMPFAD:", self.dc_ausgabe["STAMMPFAD"], "|",
            "DATUM:", self.dc_ausgabe["DATUM"], "|",
            "DATEIEN:", str(self.dc_ausgabe["DATEIANZAHL"]), "|",
            "VERZEICHNISSE:",
            str(self.dc_ausgabe["VERZEICHNISANZAHL"]), "#"
        ])
        return(tx_info)
        ''' Informationen als Text zurückgeben '''
        print("# {0}.__str__ #".format(self.tx_objname))
        dc_info = self.m_get_dc()
        tx_info = json.dumps(dc_info, indent=2)
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "DATEISTRUKTUR": {},
            "AUSGABESTRUKTUR": {
                "DATUM": "",
                "STAMMPFAD": "",
                "DATEIANZAHL": 0,
                "VERZEICHNISANZAHL": 0,
                "TYPENANZAHL": 0,
                "VERZEICHNISSE": [],
                "DASTJSON": "STRUKTURAUSGABE"
            },
            "JSONSTPFAD": "",
            "JSONORPFAD": "",
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' StrukturAusgabe in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "DATEISTRUKTUR": self.dc_struktur,
            "AUSGABESTRUKTUR": self.dc_ausgabe,
            "JSONSTPFAD": self.tx_jsonstpfad,
            "JSONORPFAD": self.tx_jsonorpfad,
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' StrukturAusgabe aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.dc_struktur = dc_daten["DATEISTRUKTUR"]
        self.dc_ausgabe = dc_daten["AUSGABESTRUKTUR"]
        self.tx_jsonstpfad = dc_daten["JSONSTPFAD"]
        self.tx_jsonorpfad = dc_daten["JSONORPFAD"]

    def m_uebersicht(self):
        ''' Übersicht mit den Grundlegenden Inormationen '''
        print("# {0}.m_uebersicht #".format(self.tx_objname))
        # Datum & Stammpfad
        self.dc_ausgabe["DATUM"] = self.dc_struktur["DATUM"]
        self.dc_ausgabe["STAMMPFAD"] = self.dc_struktur["STAMMPFAD"]
        # Anuahl Dateien, Verzeichnisse und Typen
        self.dc_ausgabe["DATEIANZAHL"] = len(
            self.dc_struktur["DATEILISTE"]
        )
        self.dc_ausgabe["VERZEICHNISANZAHL"] = len(
            self.dc_struktur["VERZEICHNISLISTE"]
        )
        self.dc_ausgabe["TYPENANZAHL"] = len(
            self.dc_struktur["TYPENLISTE"]
        )

    def m_verzeichn(self):
        ''' Ordnen nach Verzeichnissen '''
        print("# {0}.m_verzeichn #".format(self.tx_objname))
        # Verzeichnisse der Dateistruktur durchlaufen
        for tx_absverz in self.dc_struktur["VERZEICHNISLISTE"]:
            # Relativer Pfad zum Stammverzeichnis
            tx_relverz = os.path.relpath(
                tx_absverz,
                start=self.dc_struktur['STAMMPFAD']
            )
            # Liste eröffnen, [pfad, Datei-Info, Verzeichnisse, Typen]
            ls_verz = [tx_relverz, {}, [], []]
            # Leere Typenliste
            ls_typ = []
            # Dateiliste durchlaufen
            for tx_absdat in self.dc_struktur["DATEILISTE"]:
                # Verzeichnispfad
                tx_absdatverz = os.path.dirname(tx_absdat)
                tx_reldatverz = os.path.relpath(
                    tx_absdatverz,
                    start=self.dc_struktur['STAMMPFAD']
                )
                if tx_reldatverz == tx_relverz:
                    # relatives Dateiverzeichnis ist gleich relativer
                    # Verzeichnispfad
                    # Relativer Dateipfad erzeugen
                    tx_reldat = os.path.relpath(
                        tx_absdat,
                        start=self.dc_struktur['STAMMPFAD']
                    )
                    # Datei-Info holen
                    ls_info = self.dc_struktur["DATEIINFO"][tx_reldat]
                    # Datei-Name.Typ
                    tx_base = os.path.basename(tx_absdat)
                    # Datei-Info in Liste eintragen, Index 1
                    ls_verz[1][tx_base] = ls_info
                    # Typ loslösen
                    ls_base = os.path.splitext(tx_base)
                    # Typenliste ergänzen
                    ls_typ.append(ls_base[1])
            # Typenliste bereinigen, jeder Typ nur 1 mal
            mn_typ = set(ls_typ)
            # Typenliste sortiert in Liste eintragen, Index 3
            ls_verz[3] = sorted(mn_typ)
            # Verzeichnisliste durchlaufen
            for tx_absver in self.dc_struktur["VERZEICHNISLISTE"]:
                # Verzeichnispfad
                tx_absververz = os.path.dirname(tx_absver)
                if tx_absververz:
                    tx_relververz = os.path.relpath(
                        tx_absververz,
                        start=self.dc_struktur['STAMMPFAD']
                    )
                else:
                    tx_relververz = ""
                if tx_relververz == tx_relverz:
                    # relatives Dateiverzeichnis ist gleich relativer
                    # Verzeichnispfad / Verzeichnisname
                    tx_base = os.path.basename(tx_absver)
                    # An Verzeichnisliste in Liste anhängen, Index 2
                    ls_verz[2].append(tx_base)
            # Verzeichnis Liste sortieren un den Verzeichnissen anhängen
            self.dc_ausgabe["VERZEICHNISSE"].append(ls_verz)

    def m_loadjsonst(self):
        ''' Json Dateistruktur laden '''
        print("# {0}.m_loadjsonst #".format(self.tx_objname))
        # Struktur laden
        dc_datei = f_loadjson(self.tx_jsonstpfad)
        # Struktur prüfen
        if dc_datei["DASTJSON"] == "DATEISTRUKTUR":
            # Dateistruktur JSON
            self.dc_struktur = dc_datei
        else:
            # Kein Dateistruktur JSON
            tx_t = " ".join([
                "# Die Datei",
                self.tx_jsonstpfad,
                "ist kein DATEISTRUKTUR Format #"
            ])
            print(tx_t)

    def m_savejsonor(self):
        ''' Geordnete Json Ausgabestruktur speichern '''
        print("# {0}.m_savejson #".format(self.tx_objname))
        # JSON aus Ausgabe Wörterbuch speichern
        f_savejson(self.tx_jsonorpfad, self.dc_ausgabe)
