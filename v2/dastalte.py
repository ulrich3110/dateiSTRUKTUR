#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dastalfn import *

'''
dastalte.py - dateiSTRUKTUR, Alle Etappen, Testmodul
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


class Test_fnjson():
    '''
    KONZEPT
     Daten eines Wörterbuches (Dictionairy) von in einer Json-Datei
     speichern mit Hilfe des "json" Moduls
     Daten von einer Json-Datei in ein Wörterbuch laden mit Hilfe
     des "json" Moduls
    LOADJSON
    dc_data = f_loadjson(tx_pfad)
     dc_data = Wörterbuch
     tx_pfad = Pfad zur Json-Datei
    SAVEJSON
    f_savejson(tx_pfad, dc_data)
     dc_data = Wörterbuch
     tx_pfad = Pfad zur Json-Datei
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        self.in_anzerr = in_anzerr
        self.m_test_saveload()

    def m_test_saveload(self):
        ''' Teste Json speichern und nachher wieder laden '''
        # Vorgabe
        dc_v = {
            "HEAD": "Funktionstest",
            "BODY": "Dies testet die Syntax"
        }
        f_savejson("doku/test/dastalte.json", dc_v)
        # Resultat
        dc_r = f_loadjson("doku/test/dastalte.json")
        # Test & Vergleich 1
        bl_t = dc_r["BODY"] == dc_v["BODY"]
        tx_test = "Test f_savejson & f_loadjson BODY"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, dc_v["BODY"],
                                        dc_r["BODY"], self.in_anzerr)
        # Test & Vergleich 2
        bl_t = dc_r["HEAD"] == dc_v["HEAD"]
        tx_test = "Test f_savejson & f_loadjson HEAD"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, dc_v["HEAD"],
                                        dc_r["HEAD"], self.in_anzerr)


class Test_fnsave():
    '''
    KONZEPT
    - Textdateien speichern
    - CSV Dateien speichern
    SAVETEXT
    f_savetext(tx_pfad, tx_text)
        tx_pfad = Pfad zur Text-Datei
        tx_text = Text mit Zeilenumbrüchen
    SAVECSV
    f_savecsv(tx_pfad, ls_tabelle)
        ls_tabelle = Liste in Tabellenformat:
                     [["Spalte 1", "Spalte 2", "Spalte 3"],
                      ["x", "y", "z"],
                     ]
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        self.in_anzerr = in_anzerr
        self.m_test_savetext()
        self.m_test_savecsv()

    def m_test_savetext(self):
        ''' Teste Text speichern '''
        # Vorgabe
        tx_v = "\n".join([
            "Funktionstest",
            "-------------",
            "Dies testet die Syntax"
        ])
        # Test
        bl_r = f_savetext("doku/test/dastalte.txt", tx_v)
        # Vergleich
        if not bl_r:
            bl_t = True
            tx_v, tx_r = None, None
        else:
            bl_t = False
            tx_v, tx_r = "Text ..", ""
        tx_test = "Test f_savetext"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)
        tx_t = "".join(["# Bitte die Textdatei  ",
                        "doku/test/dastalte.txt",
                        "  kontrollieren #\n"])
        print(tx_t)

    def m_test_savecsv(self):
        ''' Teste Text speichern '''
        # Vorgabe
        ls_v = [
            ["A", "B", "C"],
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"]
        ]
        # Test
        bl_r = f_savecsv("doku/test/dastalte.csv", ls_v)
        # Vergleich
        if not bl_r:
            bl_t = True
            tx_v, tx_r = None, None
        else:
            bl_t = False
            tx_v, tx_r = "[ Tabelle .. ]", ""
        tx_test = "Test f_savecsv"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)
        tx_t = "".join(["# Bitte die CSV-Datei  ",
                        "doku/test/dastalte.csv",
                        "  kontrollieren #\n"])
        print(tx_t)


class Test_listenvergleich():
    '''
    KONZEPT
    - 2 Listen mit Hilfe der Mengen Funktionen vergleichen
    LISTENVERGLEICH
    ls_beide, ls_nur_a, ls_nur_b = f_listenvergleich(ls_a, ls_b)
        ls_a = 1. Liste
        ls_b = 2. Liste
        ls_beide = Vorhandene Elemente in beiden Liste
        ls_nur_a = Vorhandene Elemente nur in der 1. Liste
        ls_nur_b = Vorhandene Elemente nur in der 2. Liste
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        self.in_anzerr = in_anzerr
        self.m_test_vergleich_A()
        self.m_test_vergleich_B()

    def m_test_vergleich_A(self):
        ''' Teste Listenvergleich mit Texten'''
        # Vorgabe Liste A & B
        ls_va = ["Apfel", "Birne", "Banane", "Kiwi"]
        ls_vb = ["Apfel", "Birne", "Orange", "Zitrone"]
        # Vorgabe Erbgebnis
        ls_vr = [
                    ["Apfel", "Birne"],
                    ["Banane", "Kiwi"],
                    ["Orange", "Zitrone"]
            ]
        # Resultat
        ls_beide, ls_nur_a, ls_nur_b = f_listenvergleich(ls_va, ls_vb)
        ls_r = [ls_beide, ls_nur_a, ls_nur_b]
        # Test & Vergleich
        tx_test = "Test f_listenvergleich mit Texten"
        self.in_anzerr = f_test_liste(tx_test, ls_vr, ls_r,
                                      self.in_anzerr)

    def m_test_vergleich_B(self):
        ''' Teste Listenvergleich mit Zahlen '''
        # Vorgabe Liste A & B
        ls_va = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ls_vb = [2, 4, 6, 8, 10, 12, 14, 16]
        # Vorgabe Erbgebnis
        ls_vr = [
                    [2, 4, 6, 8],
                    [1, 3, 5, 7, 9],
                    [10, 12, 14, 16]
        ]
        # Resultat
        ls_beide, ls_nur_a, ls_nur_b = f_listenvergleich(ls_va, ls_vb)
        ls_r = [ls_beide, ls_nur_a, ls_nur_b]
        # Test & Vergleich
        tx_test = "Test f_listenvergleich mit Zahlen"
        self.in_anzerr = f_test_liste(tx_test, ls_vr, ls_r,
                                      self.in_anzerr)


if __name__ == '__main__':
    '''
    Test Hauptprogamm
    '''
    # Titel
    print("# DASTALTE #")
    # Anzahl Fehler
    in_anzerr = 0
    # Json Funktionen testen
    ob_test = Test_fnjson(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Save Funktionen testen
    ob_test = Test_fnsave(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Listenvergleich testen
    ob_test = Test_listenvergleich(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Zusammenfassung
    print("# ANZAHL FEHLER: {0}".format(in_anzerr))
