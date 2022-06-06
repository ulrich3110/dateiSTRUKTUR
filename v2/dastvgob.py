#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *


'''
dastvgob.py - dateiSTRUKTUR, Strukturen vergleichen, Objektmodul
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


class Vergleich():
    ''' 2 Dateistrukturen vergleichen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "Vergleich"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        tx_info = " ".join([
            "# <Vergleich> | STAMM QUELLE:",
            self.dc_quelle["STAMMPFAD"], "|",
            "STAMM ZIEL:", self.dc_ziel["STAMMPFAD"]
        ])
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.m_clear #".format(self.tx_objname))
        dc_clear = {
            "QUELLE": {"STAMMPFAD": "nicht verfügbar"},
            "ZIEL": {"STAMMPFAD": "nicht verfügbar"},
            "VERGLEICH": {"DASTJSON": "VERGLEICHSTRUKTUR"},
            "QUELLJSON": "",
            "ZIELJSON": "",
            "VERGLEICHJSON": ""
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Einstellungen in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "QUELLE": self.dc_quelle,
            "ZIEL": self.dc_ziel,
            "VERGLEICH": self.dc_diff,
            "QUELLJSON": self.tx_quelljson,
            "ZIELJSON": self.tx_zieljson,
            "VERGLEICHJSON": self.tx_diffjson
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Einstellungen aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.dc_quelle = dc_daten["QUELLE"]
        self.dc_ziel = dc_daten["ZIEL"]
        self.dc_diff = dc_daten["VERGLEICH"]
        self.tx_quelljson = dc_daten["QUELLJSON"]
        self.tx_zieljson = dc_daten["ZIELJSON"]
        self.tx_diffjson = dc_daten["VERGLEICHJSON"]

    def m_analize(self):
        ''' Ziel und Quelle analysieren '''
        # Generelle Informationen
        self.dc_diff = {
            "DASTJSON": "VERGLEICHSTRUKTUR",
            "STAMMPFAD_QUELLE": self.dc_quelle["STAMMPFAD"],
            "STAMMPFAD_ZIEL": self.dc_ziel["STAMMPFAD"],
            "DATUM_STRUKTUR_QUELLE":
                self.dc_quelle["DATUM"],
            "DATUM_STRUKTUR_ZIEL":
                self.dc_ziel["DATUM"],
            "ANZAHL_DATEIEN_QUELLE":
                len(self.dc_quelle["DATEILISTE"]),
            "ANZAHL_DATEIEN_ZIEL":
                len(self.dc_ziel["DATEILISTE"]),
            "ANZAHL_VERZEICHNISSE_QUELLE":
                len(self.dc_quelle["VERZEICHNISLISTE"]),
            "ANZAHL_VERZEICHNISSE_ZIEL":
                len(self.dc_ziel["VERZEICHNISLISTE"]),
            "ANZAHL_TYPEN_QUELLE":
                len(self.dc_quelle["TYPENLISTE"]),
            "ANZAHL_TYPEN_ZIEL":
                len(self.dc_ziel["TYPENLISTE"]),
            "DATEIEN_NUR_QUELLE": [],
            "DATEIEN_NUR_ZIEL": [],
            "DATEIEN_GEMEINSAM": [],
            "VERZEICHNISSE_NUR_QUELLE": [],
            "VERZEICHNISSE_NUR_ZIEL": [],
            "VERZEICHNISSE_GEMEINSAM": [],
            "TYPEN_NUR_QUELLE": [],
            "TYPEN_NUR_ZIEL": [],
            "TYPEN_GEMEINSAM": [],
            "UNTERSCHIEDLICHE_INFO": {}
        }
        # Dateien vergleichen mit relativen Pfaden
        ls_rp_quelle = []
        ls_rp_ziel = []
        for tx_ap in self.dc_quelle["DATEILISTE"]:
            ls_rp_quelle.append(os.path.relpath(
                tx_ap,
                self.dc_quelle["STAMMPFAD"]
            ))
        for tx_ap in self.dc_ziel["DATEILISTE"]:
            ls_rp_ziel.append(os.path.relpath(
                tx_ap,
                self.dc_ziel["STAMMPFAD"]
            ))
        ls_beide, ls_nur_quelle, ls_nur_ziel = f_listenvergleich(
            ls_rp_quelle,
            ls_rp_ziel
        )
        self.dc_diff["DATEIEN_GEMEINSAM"] = ls_beide
        self.dc_diff["DATEIEN_NUR_QUELLE"] = ls_nur_quelle
        self.dc_diff["DATEIEN_NUR_ZIEL"] = ls_nur_ziel
        # Verzeichnisse vergleichen mit relativen Pfaden
        ls_rp_quelle = []
        ls_rp_ziel = []
        for tx_ap in self.dc_quelle["VERZEICHNISLISTE"]:
            ls_rp_quelle.append(os.path.relpath(
                tx_ap,
                self.dc_quelle["STAMMPFAD"]
            ))
        for tx_ap in self.dc_ziel["VERZEICHNISLISTE"]:
            ls_rp_ziel.append(os.path.relpath(
                tx_ap,
                self.dc_ziel["STAMMPFAD"]
            ))
        ls_beide, ls_nur_quelle, ls_nur_ziel = f_listenvergleich(
            ls_rp_quelle,
            ls_rp_ziel
        )
        self.dc_diff["VERZEICHNISSE_GEMEINSAM"] = ls_beide
        self.dc_diff["VERZEICHNISSE_NUR_QUELLE"] = ls_nur_quelle
        self.dc_diff["VERZEICHNISSE_NUR_ZIEL"] = ls_nur_ziel
        # Typen vergleichen
        ls_beide, ls_nur_quelle, ls_nur_ziel = f_listenvergleich(
            self.dc_quelle["TYPENLISTE"],
            self.dc_ziel["TYPENLISTE"]
        )
        self.dc_diff["TYPEN_GEMEINSAM"] = ls_beide
        self.dc_diff["TYPEN_NUR_QUELLE"] = ls_nur_quelle
        self.dc_diff["TYPEN_NUR_ZIEL"] = ls_nur_ziel
        # Datei-Info gemeinsamer Dateien vergleichen
        for tx_pfad in self.dc_diff["DATEIEN_GEMEINSAM"]:
            ls_info_quelle = self.dc_quelle["DATEIINFO"][tx_pfad]
            ls_info_ziel = self.dc_ziel["DATEIINFO"][tx_pfad]
            # Unterschiede prüfen, True = identisch, False = untersch.
            bl_datum = ls_info_quelle[0] == ls_info_ziel[0]
            bl_groesse = ls_info_quelle[1] == ls_info_ziel[1]
            if not bl_datum or not bl_groesse:
                # Es gibt Unterschiede, zur Liste hinzufügen
                self.dc_diff["UNTERSCHIEDLICHE_INFO"][tx_pfad] = [
                    ls_info_quelle[0],
                    ls_info_quelle[1],
                    ls_info_ziel[0],
                    ls_info_ziel[1]
                ]

    def m_savejson(self):
        ''' Unterschiede als Json speichern '''
        print("# {0}.m_savejson #".format(self.tx_objname))
        # JSON speichern
        f_savejson(self.tx_diffjson, self.dc_diff)

    def m_loadjsons(self):
        ''' Dateistruktur JSON Quelle und Ziel laden  '''
        print("# {0}.m_loadjsons #".format(self.tx_objname))
        # Dateistrukturen laden
        dc_q = f_loadjson(self.tx_quelljson)
        dc_z = f_loadjson(self.tx_zieljson)
        # Quell Strukturen prüfen
        if dc_q["DASTJSON"] == "DATEISTRUKTUR":
            # Quell Strukturausgabe JSON übernehmen
            self.dc_quelle = dc_q
        else:
            # Kein Strukturausgabe JSON
            tx_t = " ".join([
                "# Die Quell-Datei",
                self.tx_quelljson,
                "ist kein DATEISTRUKTUR Format #"
            ])
            print(tx_t)
        # Ziel Strukturen prüfen
        if dc_z["DASTJSON"] == "DATEISTRUKTUR":
            # Ziel Strukturausgabe JSON übernehmen
            self.dc_ziel = dc_z
        else:
            # Kein Strukturausgabe JSON
            tx_t = " ".join([
                "# Die Quell-Datei",
                self.tx_zieljson,
                "ist kein DATEISTRUKTUR Format #"
            ])
            print(tx_t)
