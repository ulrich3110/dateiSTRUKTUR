#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time
from dastalfn import *
from dasterob import *
from dastsoob import *
from dastshob import *
from dastscob import *
from dastvgob import *

'''
dastrucm.py - dateiSTRUKTUR, Startprogramm, Kommandozeile
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


class RunTerm():
    ''' Befehle aus einer JSON Datei ausführen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "RunTerm"
        self.tx_titel = "dateiSTRUKTUR"
        print("# {0}.__init__ #".format(self.tx_objname))

    def m_get_befehle(self):
        ''' Befehls Wörterbuch '''
        print("# {0}.m_get_befehle #".format(self.tx_objname))
        tx_p = "./doku/run/"
        self.dc_befehle = {
            "1": {
                "TITEL": "Erfassung Test Quell Verzeichnis",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": "./doku/test/quelle",
                        "JSON": "{0}er_quell_st.json".format(tx_p)
                    }
                ]
            },
            "2": {
                "TITEL": "Erfassung Test Ziel Verzeichnis",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": "./doku/test/ziel",
                        "JSON": "{0}er_ziel_st.json".format(tx_p)
                    }
                ]
            },
            "3": {
                "TITEL": "Struktur ordnen vom aktuellen Verzeichnis",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": ".",
                        "JSON": "{0}so_quell_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "STRUKTUR_ORDNEN",
                        "JSON_ST": "{0}so_quell_st.json".format(tx_p),
                        "JSON_OR": "{0}so_quell_or.json".format(tx_p)
                    }
                ]
            },
            "4": {
                "TITEL": "HTML Dokument vom aktuellen Verzeichnis",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": ".",
                        "JSON": "{0}sh_quell_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "STRUKTUR_ORDNEN",
                        "JSON_ST": "{0}sh_quell_st.json".format(tx_p),
                        "JSON_OR": "{0}sh_quell_or.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "HTML",
                        "JSON_OR": "{0}sh_quell_or.json".format(tx_p),
                        "HTML": "{0}sh_quelle.html".format(tx_p),
                        "TITEL": "Aktuelles Verzeichnis",
                        "TEXT": "HTML Beispiel"
                    }
                ]
            },
            "5": {
                "TITEL": "CSV Dokument vom aktuellen Verzeichnis",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": ".",
                        "JSON": "{0}sc_quell_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "STRUKTUR_ORDNEN",
                        "JSON_ST": "{0}sc_quell_st.json".format(tx_p),
                        "JSON_OR": "{0}sc_quell_or.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "CSV",
                        "JSON_OR": "{0}sc_quell_or.json".format(tx_p),
                        "CSV": "{0}sc_quelle.csv".format(tx_p),
                        "TITEL": "Aktuelles Verzeichnis",
                        "TEXT": "CSV Beispiel"
                    }
                ]
            },
            "6": {
                "TITEL": "'.' mit sich selber vergleichen",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": ".",
                        "JSON": "{0}vg_quell1_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": ".",
                        "JSON": "{0}vg_ziel1_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "VERGLEICHEN",
                        "QUELLE": "{0}vg_quell1_st.json".format(tx_p),
                        "ZIEL": "{0}vg_ziel1_st.json".format(tx_p),
                        "VERGL": "{0}vg_vergleich1.json".format(tx_p)
                    }
                ]
            },
            "7": {
                "TITEL": "'./doku/run' mit './doku/test' vergleichen",
                "BEFEHLE": [
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": "./doku/run",
                        "JSON": "{0}vg_quell2_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "ERFASSEN",
                        "QUELLE": "./doku/test",
                        "JSON": "{0}vg_ziel2_st.json".format(tx_p)
                    },
                    {
                        "BEFEHL": "VERGLEICHEN",
                        "QUELLE": "{0}vg_quell2_st.json".format(tx_p),
                        "ZIEL": "{0}vg_ziel2_st.json".format(tx_p),
                        "VERGL": "{0}vg_vergleich2.json".format(tx_p)
                    }
                ]
            }
        }

    def m_anzeige(self):
        ''' Befehle anzeigen '''
        tx_wahl = "0"
        while tx_wahl:
            # Schleife solange ausführen bis eine leere Eingabe
            print("# {0}.m_anzeige #".format(self.tx_objname))
            # Titel anzeigen
            print()
            print(self.tx_titel)
            print("-" * len(self.tx_titel))
            # Befehls-Wörterbuch durchlaufen
            for tx_key, dc_commands in self.dc_befehle.items():
                print("[{0}]  {1}".format(tx_key, dc_commands["TITEL"]))
            print()
            print("[ENTER]  Beenden")
            print()
            tx_wahl = input("Ihre Wahl: ")
            if tx_wahl:
                # Keine Leere Eingabe = Befehlswahl
                # Leere Eingabe (Enter) = Beenden
                ls_befehle = self.dc_befehle[tx_wahl]["BEFEHLE"]
                print()
                print("#" * 40)
                self.m_run(ls_befehle)
                print("#" * 40)
                print()

    def m_run(self, ls_befehle):
        ''' Befehl ausführen '''
        print("# {0}.m_run #".format(self.tx_objname))
        # Befehlsliste durchlaufen
        for dc_args in ls_befehle:
            # Aktion und Werte Wörterbuch
            # Aktionen wählen
            if dc_args["BEFEHL"] == "ERFASSEN":
                print("# {0}.m_run ERFASSEN #".format(self.tx_objname))
                # Struktur erzeugen
                ob_strkt = DateiStruktur()
                # Variabeln setzen
                ob_strkt.tx_stammpfad = dc_args["QUELLE"]
                ob_strkt.tx_jsonpfad = dc_args["JSON"]
                # Struktur lesen
                ob_strkt.m_lesen()
                # Typenliste generieren
                ob_strkt.m_typlist()
                # Datei-Information holen
                ob_strkt.m_datinfo()
                # JSON speichern
                ob_strkt.m_savejson()
            elif dc_args["BEFEHL"] == "STRUKTUR_ORDNEN":
                print("# {0}.m_run STRUKTUR_ORDNEN #".format(
                    self.tx_objname
                ))
                # Struktur ordnen Objekt erzeugen
                ob_ausgabe = StrukturAusgabe()
                # Variabeln setzen
                ob_ausgabe.tx_jsonstpfad = dc_args["JSON_ST"]
                ob_ausgabe.tx_jsonorpfad = dc_args["JSON_OR"]
                # JSON Dateistruktur laden
                ob_ausgabe.m_loadjsonst()
                # Struktur für Ausgabe ordnen
                ob_ausgabe.m_uebersicht()
                ob_ausgabe.m_verzeichn()
                # Geordnete Ausgabe als JSON speichern
                ob_ausgabe.m_savejsonor()
            elif dc_args["BEFEHL"] == "HTML":
                print("# {0}.m_run HTML #".format(self.tx_objname))
                # HTML-Struktur Objekt erzeugen
                ob_html = HtmlStruktur()
                # Variabeln setzen
                ob_html.tx_jsonpfad = dc_args["JSON_OR"]
                ob_html.tx_htmlpfad = dc_args["HTML"]
                ob_html.tx_titel = dc_args["TITEL"]
                ob_html.tx_text = dc_args["TEXT"]
                # HTML generieren
                ob_html.m_loadjsonor()
                ob_html.m_anfang()
                ob_html.m_struktur()
                ob_html.m_verzeichnisse()
                ob_html.m_ende()
                # HTML speichern
                ob_html.m_save()
            elif dc_args["BEFEHL"] == "CSV":
                print("# {0}.m_run CSV #".format(self.tx_objname))
                # Als CSV Tabelle speichern
                ob_csv = CsvStruktur()
                ob_csv.tx_jsonpfad = dc_args["JSON_OR"]
                ob_csv.tx_csvpfad = dc_args["CSV"]
                ob_csv.tx_titel = dc_args["TITEL"]
                ob_csv.tx_text = dc_args["TEXT"]
                # CSV generieren
                ob_csv.m_loadjsonor()
                ob_csv.m_anfang()
                ob_csv.m_struktur()
                ob_csv.m_verzeichnisse()
                # CSV speichern
                ob_csv.m_save()
            elif dc_args["BEFEHL"] == "VERGLEICHEN":
                print("# {0}.m_run VERGLEICHEN #".format(
                    self.tx_objname
                ))
                # Vergleichsobjekt erzeugen
                ob_vergl = Vergleich()
                # Variabeln setzen
                ob_vergl.tx_quelljson = dc_args["QUELLE"]
                ob_vergl.tx_zieljson = dc_args["ZIEL"]
                ob_vergl.tx_diffjson = dc_args["VERGL"]
                # Strukturenen laden
                ob_vergl.m_loadjsons()
                # Analysieren
                ob_vergl.m_analize()
                # JSON speichern
                ob_vergl.m_savejson()


if __name__ == '__main__':
    # RunJson Objekt und Befehle laden
    ob_run = RunTerm()
    ob_run.m_get_befehle()
    ob_run.m_anzeige()
