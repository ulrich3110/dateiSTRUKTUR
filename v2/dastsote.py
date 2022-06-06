#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dastsoob import *
from dastalfn import *

'''
dastsote.py - dateiSTRUKTUR, Struktur ordnen für Ausgabe, Testmodul
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


class Test_StrukturAusgabe():
    '''
    KONZEPT
    - JSON Datei-Struktur vom Objekt DateiStruktur() laden, ordnen und
      für die Ausgabe als geordnetes JSON speichern.
    OBJEKT
    StrukturAusgabe()
    METHODEN
    .__init__()               Initialisieren
    .__str__()                Eingebaute String-Funktion
    .m_clear()                Objekt zurücksetzen
    .m_get_dc()               Daten als Wörterbuch zurückgeben
    .m_set_dc(Wörterbuch)     Daten mit einem Wörterbuch hinzufügen
    .m_loadjsonst()             Json Struktur laden
    .m_uebersicht()           Übersicht erstellen
    .m_verzeichn()            Ordnen nach Verzeichnisse
    .m_savejsonor()             Geordnete Json Ausgabe Struktur speichern
    VARIABELN
    .dc_struktur              Wörterbuch mit der Datei-Struktur
    .dc_ausgabe               Wörterbuch mit der Ausgabe-Struktur
    BEMERKUNGEN
    - In Test_StrukturAusgabe.m_get_json() sind Beispiel Strukturen
      der oben erwähnten Wörterbücher definiert.
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        # Anzahl Fehler
        self.in_anzerr = in_anzerr
        # Variablen
        self.tx_jsonstpfad = "./doku/test/dateistruktur.json"
        self.tx_jsonorpfad = "./doku/test/dastso.json"
        # Test Objekt
        self.ob_test = StrukturAusgabe()
        # Tests
        self.m_test_str()
        self.m_test_clear()
        self.m_test_setdc()
        self.m_test_getdc()
        self.m_test_dcstruktur()
        self.m_test_dcausgabe()
        self.m_test_txjsonstpfad()
        self.m_test_txjsonorpfad()
        self.m_test_uebersicht()
        self.m_test_verzeichnisse()
        self.m_test_loadjsonst()
        self.m_test_savejsonor()

    def m_get_json(self):
        '''
        Dateistruktur und Srukturausgabe zurückgeben
        '''
        dc_dateistruktur = {
            "DASTJSON": "DATEISTRUKTUR",
            "DATEILISTE": [
                "./dastaldo/daster/quelle/pfad1/Datei_11.txa",
                "./dastaldo/daster/quelle/pfad1/Datei_12.txb",
                "./dastaldo/daster/quelle/pfad1/Datei_13.txc",
                "./dastaldo/daster/quelle/pfad2/Datei_21.txa",
                "./dastaldo/daster/quelle/pfad2/Datei_22.txb",
                "./dastaldo/daster/quelle/pfad3/Datei_31.txa",
                "./dastaldo/daster/quelle/pfad3/Datei_32.txb",
                "./dastaldo/daster/quelle/pfad3/Datei_33.txc",
                "./dastaldo/daster/quelle/pfad3/Datei_34.txa"
            ],
            "VERZEICHNISLISTE": [
                "./dastaldo/daster/quelle/pfad1",
                "./dastaldo/daster/quelle/pfad2",
                "./dastaldo/daster/quelle/pfad3",
                "./dastaldo/daster/quelle"
            ],
            "DATUM": "01.06.2022 21:37:05",
            "JSONPFAD": "./dastaldo/daster/quell_st.json",
            "STAMMPFAD": "./dastaldo/daster/quelle",
            "TYPENLISTE": [".txa", ".txb", ".txc"],
            "DATEIINFO": {
                "pfad1/Datei_11.txa": ["27.05.2022 15:01:13", 10],
                "pfad1/Datei_12.txb": ["27.05.2022 15:00:36", 13],
                "pfad1/Datei_13.txc": ["27.05.2022 15:00:59", 15],
                "pfad2/Datei_21.txa": ["27.05.2022 15:02:01", 20],
                "pfad2/Datei_22.txb": ["27.05.2022 15:02:11", 21],
                "pfad3/Datei_31.txa": ["27.05.2022 15:07:12", 24],
                "pfad3/Datei_32.txb": ["27.05.2022 15:04:04", 22],
                "pfad3/Datei_33.txc": ["27.05.2022 15:04:16", 23],
                "pfad3/Datei_34.txa": ["27.05.2022 15:07:53", 26]
            }
        }
        dc_ausgabestruktur = {
            "DASTJSON": "STRUKTURAUSGABE",
            "DATUM": "27.05.2022 15:08:08",
            "STAMMPFAD": "./dastaldo/daster/quelle",
            "DATEIANZAHL": 9,
            "VERZEICHNISANZAHL": 4,
            "TYPENANZAHL": 3,
            "VERZEICHNISSE": [
                [
                    ".",
                    {},
                    ["pfad1", "pfad2", "pfad3"],
                    []
                ],
                [
                    "pfad1",
                    {
                        "Datei_11.txa": ["27.05.2022 15:01:13", 10],
                        "Datei_12.txb": ["27.05.2022 15:00:36", 13],
                        "Datei_13.txc": ["27.05.2022 15:00:59", 15]
                    },
                    [],
                    [".txa", ".txb", ".txc"]
                ],
                [
                    "pfad2",
                    {
                        "Datei_21.txa": ["27.05.2022 15:02:01", 20],
                        "Datei_22.txb": ["27.05.2022 15:02:11", 21]
                    },
                    [],
                    [".txa", ".txb"]
                ],
                [
                    "pfad3",
                    {
                        "Datei_31.txa": ["27.05.2022 15:07:12", 24],
                        "Datei_32.txb": ["27.05.2022 15:04:04", 22],
                        "Datei_33.txc": ["27.05.2022 15:04:16", 23],
                        "Datei_34.txa": ["27.05.2022 15:07:53", 26]
                    },
                    [],
                    [".txa", ".txb", ".txc"]
                ]
            ]
        }
        return(dc_dateistruktur, dc_ausgabestruktur)

    def m_get_ds_liste(self, dc_ds):
        ''' Die Datei-Struktur als Werte und Listen zurückgeben '''
        # Einzelne Werte und sortierte Listen
        tx_dastjson = dc_ds["DASTJSON"]
        ls_dateiliste = dc_ds["DATEILISTE"]
        ls_dateiliste.sort()
        ls_verzliste = dc_ds["VERZEICHNISLISTE"]
        ls_verzliste.sort()
        tx_datum = dc_ds["DATUM"]
        tx_jsonorpfad = dc_ds["JSONPFAD"]
        tx_stammpfad = dc_ds["STAMMPFAD"]
        ls_typliste = dc_ds["TYPENLISTE"]
        ls_typliste.sort()
        # Datei-Info auslesen und als Liste mit Texten speichern
        ls_datinfo = []
        for tx_datei, ls_info in dc_ds["DATEIINFO"].items():
            ls_datinfo.append("{0}, {1}, {2}".format(
                tx_datei,
                ls_info[0],
                str(ls_info[1])
            ))
        ls_datinfo.sort()
        # Als Gesamtliste zurückgeben
        ls_ds = [tx_dastjson, ls_dateiliste, ls_verzliste, tx_datum,
                 tx_jsonorpfad, tx_stammpfad, ls_typliste, ls_datinfo]
        return(ls_ds)

    def m_get_as_liste(self, dc_as):
        ''' Die Ausgabe-Struktur als Werte und Listen zurückgeben '''
        tx_dastjson = dc_as["DASTJSON"]
        tx_datum = dc_as["DATUM"]
        tx_stammpfad = dc_as["STAMMPFAD"]
        in_datanz = dc_as["DATEIANZAHL"]
        in_verzanz = dc_as["VERZEICHNISANZAHL"]
        in_typanz = dc_as["TYPENANZAHL"]
        ls_verz = dc_as["VERZEICHNISSE"]
        # Verzeichnisliste auslesen
        ls_verzneu = []
        for ls_v in ls_verz:
            tx_pfad, dc_datinfo, ls_subverz, ls_dateityp = ls_v
            # Datei-Info auslesen und als Liste mit Texten speichern
            ls_datinfo = []
            for tx_datei, ls_info in dc_datinfo.items():
                ls_datinfo.append("{0}, {1}, {2}".format(
                    tx_datei,
                    ls_info[0],
                    str(ls_info[1])
                ))
            ls_datinfo.sort()
            ls_subverz.sort()
            ls_dateityp.sort()
            ls_verzneu.append([tx_pfad, ls_datinfo, ls_subverz,
                               ls_dateityp])
        ls_verzneu.sort()
        # Als Gesamtliste zurückgeben
        ls_as = [tx_dastjson, tx_stammpfad, in_datanz, in_verzanz,
                 in_typanz, ls_verzneu]
        return(ls_as)

    def m_test_str(self):
        ''' Teste String Methode '''
        # Resultat
        tx_r = str(self.ob_test)
        # Test & Vergleich
        if tx_r:
            bl_t = True
            tx_v = tx_r
        else:
            bl_t = False
            tx_v = "Text .."
        tx_test = "Test Methode __str__"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_clear(self):
        ''' Teste Clear Methode '''
        # Vorgabe
        vl_v = None
        # Resultat
        vl_r = self.ob_test.m_clear()
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_clear"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_setdc(self):
        ''' Teste Set DC Methode '''
        # Vorgabe
        vl_v = None
        # Resultat
        dc_struktur, dc_ausgabe = self.m_get_json()
        dc_daten = {
            "DATEISTRUKTUR": dc_struktur,
            "AUSGABESTRUKTUR": dc_ausgabe,
            "JSONSTPFAD": self.tx_jsonstpfad,
            "JSONORPFAD": self.tx_jsonorpfad
        }
        vl_r = self.ob_test.m_set_dc(dc_daten)
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_set_dc"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_getdc(self):
        ''' Teste Get DC Methode '''
        # Vorgabe
        dc_struktur, dc_ausgabe = self.m_get_json()
        # Resultat
        dc_r = self.ob_test.m_get_dc()
        # Test & Vergleich DATEISTRUKTUR
        ls_v = self.m_get_ds_liste(dc_struktur)
        ls_r = self.m_get_ds_liste(dc_r["DATEISTRUKTUR"])
        tx_test = "Test Methode m_get_dc[DATEISTRUKTUR]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)
        # Test & Vergleich AUSGABESTRUKTUR
        ls_v = self.m_get_as_liste(dc_ausgabe)
        ls_r = self.m_get_as_liste(dc_r["AUSGABESTRUKTUR"])
        tx_test = "Test Methode m_get_dc[AUSGABESTRUKTUR]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)
        # Test Einzelwerte
        ls_v = [self.tx_jsonstpfad, self.tx_jsonorpfad]
        ls_r = [dc_r["JSONSTPFAD"], dc_r["JSONORPFAD"]]
        tx_test = "Test Methode m_get_dc[JSONSTPFAD, JSONORPFAD]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_dcstruktur(self):
        ''' Teste Wörterbuch Datei-Struktur '''
        # Vorgabe
        dc_struktur, dc_ausgabe = self.m_get_json()
        # Resultat
        self.ob_test.dc_struktur = dc_struktur
        dc_r = self.ob_test.dc_struktur
        # Test & Vergleich DATEISTRUKTUR
        ls_v = self.m_get_ds_liste(dc_struktur)
        ls_r = self.m_get_ds_liste(dc_r)
        tx_test = "Test Attribut dc_struktur"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_dcausgabe(self):
        ''' Teste Wörterbuch Ausgabe-Struktur '''
        # Vorgabe
        dc_struktur, dc_ausgabe = self.m_get_json()
        # Resultat
        self.ob_test.dc_ausgabe = dc_ausgabe
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich AUSGABESTRUKTUR
        ls_v = self.m_get_as_liste(dc_ausgabe)
        ls_r = self.m_get_as_liste(dc_r)
        tx_test = "Test Attribut dc_ausgabe"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_txjsonstpfad(self):
        ''' Teste Wörterbuch Ausgabe-Struktur '''
        # Vorgabe
        tx_v = self.tx_jsonstpfad
        # Resultat
        self.ob_test.tx_jsonstpfad = tx_v
        tx_r = self.ob_test.tx_jsonstpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_jsonstpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txjsonorpfad(self):
        ''' Teste Wörterbuch Ausgabe-Struktur '''
        # Vorgabe
        tx_v = self.tx_jsonorpfad
        # Resultat
        self.ob_test.tx_jsonorpfad = tx_v
        tx_r = self.ob_test.tx_jsonorpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_jsonorpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_uebersicht(self):
        ''' Teste Methode Uebersicht '''
        # Vorgabe
        dc_struktur, dc_ausgabe = self.m_get_json()
        dc_v = {
            "DASTJSON": "STRUKTURAUSGABE",
            "DATUM": dc_ausgabe["DATUM"],
            "STAMMPFAD": dc_ausgabe["STAMMPFAD"],
            "DATEIANZAHL": dc_ausgabe["DATEIANZAHL"],
            "VERZEICHNISANZAHL": dc_ausgabe["VERZEICHNISANZAHL"],
            "TYPENANZAHL": dc_ausgabe["TYPENANZAHL"],
            "VERZEICHNISSE": [],
        }
        # Resultat
        self.ob_test.m_clear()
        self.ob_test.dc_struktur = dc_struktur
        self.ob_test.m_uebersicht()
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich AUSGABESTRUKTUR
        ls_v = self.m_get_as_liste(dc_v)
        ls_r = self.m_get_as_liste(dc_r)
        tx_test = "Test Methode m_uebersicht[AUSGABESTRUKTUR]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_verzeichnisse(self):
        ''' Teste Methode Verzeichnisse '''
        # Vorgabe
        dc_struktur, dc_ausgabe = self.m_get_json()
        dc_v = {
            "DASTJSON": "STRUKTURAUSGABE",
            "DATUM": dc_ausgabe["DATUM"],
            "STAMMPFAD": dc_ausgabe["STAMMPFAD"],
            "DATEIANZAHL": dc_ausgabe["DATEIANZAHL"],
            "VERZEICHNISANZAHL": dc_ausgabe["VERZEICHNISANZAHL"],
            "TYPENANZAHL": dc_ausgabe["TYPENANZAHL"],
            "VERZEICHNISSE": dc_ausgabe["VERZEICHNISSE"]
        }
        # Resultat
        self.ob_test.m_verzeichn()
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich AUSGABESTRUKTUR
        ls_v = self.m_get_as_liste(dc_v)
        ls_r = self.m_get_as_liste(dc_r)
        tx_test = "Test Methode m_verzeichn[AUSGABESTRUKTUR]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_loadjsonst(self):
        ''' Teste Methode Json Struktur laden '''
        # Vorgabe
        dc_v, dc_ausgabe = self.m_get_json()
        # Resultat
        self.ob_test.m_clear()
        self.ob_test.tx_jsonstpfad = self.tx_jsonstpfad
        self.ob_test.m_loadjsonst()
        dc_r = self.ob_test.dc_struktur
        # Test & Vergleich DATEISTRUKTUR
        ls_v = self.m_get_ds_liste(dc_v)
        ls_r = self.m_get_ds_liste(dc_r)
        tx_test = "Test Methode m_loadjsonst[DATEISTRUKTUR]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_savejsonor(self):
        ''' Teste Geordnete Ausgabestruktur speichern '''
        # Vorgabe
        vl_v = None
        # Resultat
        # Objekt löschen, Variabeln setzen
        self.ob_test.m_clear()
        self.ob_test.tx_jsonstpfad = self.tx_jsonstpfad
        self.ob_test.tx_jsonorpfad = self.tx_jsonorpfad
        # Dateistruktur laden, Übersicht & Verzeichnisse erstellen
        self.ob_test.m_loadjsonst()
        self.ob_test.m_uebersicht()
        self.ob_test.m_verzeichn()
        # Geordnete Ausgabe speichern
        vl_r = self.ob_test.m_savejsonor()
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_savejsonor"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)


if __name__ == '__main__':
    '''
    Test Hauptprogamm
    '''
    # Titel
    print("# DASTSOTE #")
    # Anzahl Fehler
    in_anzerr = 0
    # DateiStruktur Objekt testen
    ob_test = Test_StrukturAusgabe(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Zusammenfassung
    print("# ANZAHL FEHLER: {0}".format(in_anzerr))
