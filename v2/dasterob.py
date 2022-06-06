#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *

'''
dasterob.py - dateiSTRUKTUR, Struktur erfassen, Objektmodul
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


class DateiStruktur():
    ''' Datei-Struktur Inhalt (dast v2) '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "DateiStrukturNeu"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        tx_info = " ".join([
            "# <DateiStruktur> | STAMMPFAD:", self.tx_stammpfad, "|",
            "DATUM:", self.tx_datum, "|",
            "DATEIEN:", str(len(self.ls_dateien)), "|",
            "VERZEICHNISSE:", str(len(self.ls_verzeich)), "#"
        ])
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "DATEILISTE": [],
            "VERZEICHNISLISTE": [],
            "DATUM": '',
            "STAMMPFAD": '',
            "TYPENLISTE": [],
            "DATEIINFO": {},
            "JSONPFAD": '',
            "DASTJSON": 'DATEISTRUKTUR'
        }
        self.m_set_dc(dc_clear)

    def m_set_dc(self, dc_daten):
        ''' Dateistruktur aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.ls_dateien = dc_daten["DATEILISTE"]
        self.ls_verzeich = dc_daten["VERZEICHNISLISTE"]
        self.tx_datum = dc_daten["DATUM"]
        self.tx_stammpfad = dc_daten["STAMMPFAD"]
        self.ls_typen = dc_daten["TYPENLISTE"]
        self.dc_dateiinfo = dc_daten["DATEIINFO"]
        self.tx_jsonpfad = dc_daten["JSONPFAD"]
        self.tx_dastjson = dc_daten["DASTJSON"]

    def m_get_dc(self):
        ''' Dateistruktur in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "DATEILISTE": self.ls_dateien,
            "VERZEICHNISLISTE": self.ls_verzeich,
            "DATUM": self.tx_datum,
            "STAMMPFAD": self.tx_stammpfad,
            "TYPENLISTE": self.ls_typen,
            "DATEIINFO": self.dc_dateiinfo,
            "JSONPFAD": self.tx_jsonpfad,
            "DASTJSON": self.tx_dastjson
        }
        return(dc_daten)

    def m_lesen(self):
        ''' Dateistruktur mit os.walk lesen'''
        print("# {0}.m_lesen #".format(self.tx_objname))
        # Listen leeren
        self.ls_dateien = []
        self.ls_verzeich = []
        # Struktur erfassen
        for tx_root, ob_dirs, ob_files in os.walk(
            self.tx_stammpfad,
            topdown=False
        ):
            for tx_name in ob_files:
                self.ls_dateien.append(os.path.join(
                    tx_root,
                    tx_name
                ))
            for tx_name in ob_dirs:
                self.ls_verzeich.append(os.path.join(
                    tx_root,
                    tx_name
                ))
        # Sortieren
        self.ls_dateien.sort()
        self.ls_verzeich.sort()
        # Stammverzeichnis anhängen
        self.ls_verzeich.append(self.tx_stammpfad)
        # Datum speichern
        ob_now = datetime.datetime.today()
        self.tx_datum = ob_now.strftime('%d.%m.%Y %H:%M:%S')

    def m_typlist(self):
        ''' Typenliste aus Dateiliste erzeugen '''
        print("# {0}.m_typlist #".format(self.tx_objname))
        # Liste für Typen definieren
        ls_typtotal = []
        # Dateiliste durchlaufen
        for tx_pfad in self.ls_dateien:
            # Dateiname und Typ
            tx_dir = os.path.dirname(tx_pfad)
            tx_base = os.path.basename(tx_pfad)
            ls_base = os.path.splitext(tx_base)
            # Typenliste ergänzen
            ls_typtotal.append(ls_base[1])
        # Typenliste bereinigen, jeder Typ nur 1 mal
        mn_typ = set(ls_typtotal)
        self.ls_typen = sorted(mn_typ)

    def m_datinfo(self):
        ''' Dateiinformationen der Dateien holen '''
        print("# {0}.m_datinfo #".format(self.tx_objname))
        # Dateiliste durchlaufen
        for tx_pfad in self.ls_dateien:
            # Dateipfad, Dateiname.Typ
            tx_relpfad = os.path.relpath(tx_pfad, self.tx_stammpfad)
            # Datum und Grösse lesen
            if os.path.isfile(tx_pfad):
                ob_datum = os.path.getmtime(tx_pfad)
                tx_datum = time.strftime(
                    '%d.%m.%Y %H:%M:%S',
                    time.localtime(ob_datum)
                )
                in_groesse = os.path.getsize(tx_pfad)
                # Dateiinfo Wörterbuch füllen
                self.dc_dateiinfo[tx_relpfad] = [tx_datum, in_groesse]

    def m_savejson(self):
        ''' Json Dateistruktur speichern '''
        print("# {0}.m_savejson #".format(self.tx_objname))
        # Wörterbuch für JSON holen
        dc_json = self.m_get_dc()
        # JSON speichern
        f_savejson(self.tx_jsonpfad, dc_json)
