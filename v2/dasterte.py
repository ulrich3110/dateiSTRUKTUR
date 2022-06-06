#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dasterob import *
from dastalfn import *

'''
dasterte.py - dateiSTRUKTUR, Struktur erfassen, Testmodul
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


class Test_DateiStruktur():
    '''
    KONZEPT
     Datei-Struktur mit der os.walk funktion lesen, ergänzen und als
     Json speichern.
    OBJEKT
    DateiStruktur()
    METHODEN
    .__init__()           Initialisieren
    .__str__()            Eingebaute String-Funktion
    .m_clear()            Objekt zurücksetzen
    .m_set_dc(Wörterbuch) Daten mit einem Wörterbuch hinzufügen
    .m_get_dc()           Daten als Wörterbuch zurückgeben
    .m_lesen()            Dateistruktur lesen
    .m_typlist()          Typenliste generieren
    .m_datinfo()          Datei-Information holen
    .m_savejson()         Dateistruktur als Json speichern
    VARIABELN
    .ls_dat               Datei-Liste
    .ls_verz              Verzeichnis-Liste
    .ls_typ               Typen-Liste
    .dc_datinf            Datei-Info Wörterbuch
    .tx_stamm             Wurzelverzeichnis
    .tx_datum             Datum
    BEMERKUNGEN
     In Test_DateiStruktur.m_get_strukt() ist eine Beispiel Struktur
     der oben erwähnten Variablen definiert.
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        # Anzahl Fehler
        self.in_anzerr = in_anzerr
        # Test Objekt
        self.ob_test = DateiStruktur()
        # Tests
        self.m_test_str()
        self.m_test_clear()
        self.m_test_setdc()
        self.m_test_getdc()
        self.m_test_lsdateien()
        self.m_test_lsverzeich()
        self.m_test_lstypen()
        self.m_test_dcdateiinfo()
        self.m_test_txstammpfad()
        self.m_test_txdatum()
        self.m_test_txjsonpfad()
        self.m_test_txdastjson()
        self.m_test_lesen()
        self.m_test_typlist()
        self.m_test_datinfo()
        self.m_test_savejson()

    def m_get_strukt(self):
        ''' Datei-Struktur zurückgeben '''
        dc_strkt = {
            "DASTJSON": "DATEISTRUKTUR",
            "DATEILISTE": [
                "./doku/test/quelle/pfad1/Datei_11.txa",
                "./doku/test/quelle/pfad1/Datei_12.txb",
                "./doku/test/quelle/pfad1/Datei_13.txc",
                "./doku/test/quelle/pfad2/Datei_21.txa",
                "./doku/test/quelle/pfad2/Datei_22.txb",
                "./doku/test/quelle/pfad3/Datei_31.txa",
                "./doku/test/quelle/pfad3/Datei_32.txb",
                "./doku/test/quelle/pfad3/Datei_33.txc",
                "./doku/test/quelle/pfad3/Datei_34.txa"
            ],
            "VERZEICHNISLISTE": [
                "./doku/test/quelle",
                "./doku/test/quelle/pfad1",
                "./doku/test/quelle/pfad2",
                "./doku/test/quelle/pfad3"
            ],
            "DATUM": "27.05.2022 15:08:08",
            "STAMMPFAD": "./doku/test/quelle",
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
            },
            "JSONPFAD": "./doku/test/dasterte.json"
        }
        return(dc_strkt)

    def m_get_ds_liste(self, dc_strkt):
        ''' Die Datei-Struktur als Werte und Listen zurückgeben '''
        # Einzelne Werte und sortierte Listen
        tx_dastjson = dc_strkt["DASTJSON"]
        ls_dateiliste = dc_strkt["DATEILISTE"]
        ls_dateiliste.sort()
        ls_verzliste = dc_strkt["VERZEICHNISLISTE"]
        ls_verzliste.sort()
        tx_datum = dc_strkt["DATUM"]
        tx_jsonorpfad = dc_strkt["JSONPFAD"]
        tx_stammpfad = dc_strkt["STAMMPFAD"]
        ls_typliste = dc_strkt["TYPENLISTE"]
        ls_typliste.sort()
        ls_datinfo = self.m_get_datinf_liste(dc_strkt["DATEIINFO"])
        # Als Gesamtliste zurückgeben
        ls_strkt = [tx_dastjson, ls_dateiliste, ls_verzliste, tx_datum,
                    tx_jsonorpfad, tx_stammpfad, ls_typliste,
                    ls_datinfo]
        return(ls_strkt)

    def m_get_datinf_liste(self, dc_datinf):
        ''' Das Wörterbuch mit Datei-Informationen als Liste '''
        # Datei-Info auslesen und als Liste mit Texten speichern
        ls_datinf = []
        for tx_datei, ls_info in dc_datinf.items():
            ls_datinf.append("{0}, {1}, {2}".format(
                tx_datei,
                ls_info[0],
                str(ls_info[1])
            ))
        ls_datinf.sort()
        return(ls_datinf)

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
        vl_r = self.ob_test.m_set_dc(self.m_get_strukt())
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_set_dc"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_getdc(self):
        ''' Teste Get DC Methode '''
        # Vorgabe
        dc_v = self.m_get_strukt()
        # Resultat
        dc_r = self.ob_test.m_get_dc()
        # Test & Vergleich DATEISTRUKTUR
        ls_v = self.m_get_ds_liste(dc_v)
        ls_r = self.m_get_ds_liste(dc_r)
        tx_test = "Test Methode m_get_dc"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_lsdateien(self):
        ''' Teste Dateiliste '''
        # Vorgabe
        ls_v = self.m_get_strukt()["DATEILISTE"]
        # Resultat
        self.ob_test.ls_dateien = ls_v
        ls_r = self.ob_test.ls_dateien
        ls_v.sort()
        ls_r.sort()
        # Test & Vergleich
        bl_t = ls_r == ls_v
        tx_test = "Test Attribut ls_dateien"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, ls_v, ls_r,
                                        self.in_anzerr)

    def m_test_lsverzeich(self):
        ''' Teste Verzeichnisliste '''
        # Vorgabe
        ls_v = self.m_get_strukt()["VERZEICHNISLISTE"]
        # Resultat
        self.ob_test.ls_verzeich = ls_v
        ls_r = self.ob_test.ls_verzeich
        ls_v.sort()
        ls_r.sort()
        # Test & Vergleich
        bl_t = ls_r == ls_v
        tx_test = "Test Attribut ls_verzeich"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, ls_v, ls_r,
                                        self.in_anzerr)

    def m_test_lstypen(self):
        ''' Teste Typenliste '''
        # Vorgabe
        ls_v = self.m_get_strukt()["TYPENLISTE"]
        # Resultat
        self.ob_test.ls_typen = ls_v
        ls_r = self.ob_test.ls_typen
        ls_v.sort()
        ls_r.sort()
        # Test & Vergleich
        bl_t = ls_r == ls_v
        tx_test = "Test Attribut ls_typen"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, ls_v, ls_r,
                                        self.in_anzerr)

    def m_test_dcdateiinfo(self):
        ''' Teste Datei-Info '''
        # Test Titel
        tx_test = "Test Attribut dc_dateiinfo"
        # Vorgabe
        dc_v = self.m_get_strukt()["DATEIINFO"]
        # Resultat
        self.ob_test.dc_dateiinfo = dc_v
        dc_r = self.ob_test.dc_dateiinfo
        # Test & Vergleich DATEIINFO
        ls_v = self.m_get_datinf_liste(dc_v)
        ls_r = self.m_get_datinf_liste(dc_r)
        tx_test = "Test Methode m_get_dc"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_txstammpfad(self):
        ''' Teste Stammpfad '''
        # Vorgabe
        tx_v = self.m_get_strukt()["STAMMPFAD"]
        # Resultat
        self.ob_test.tx_stammpfad = tx_v
        tx_r = self.ob_test.tx_stammpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_stammpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txdatum(self):
        ''' Teste Datum '''
        # Vorgabe
        tx_v = self.m_get_strukt()["DATUM"]
        # Resultat
        self.ob_test.tx_datum = tx_v
        tx_r = self.ob_test.tx_datum
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_datum"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txjsonpfad(self):
        ''' Teste Json Pfad '''
        # Vorgabe
        tx_v = self.m_get_strukt()["JSONPFAD"]
        # Resultat
        self.ob_test.tx_jsonpfad = tx_v
        tx_r = self.ob_test.tx_jsonpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_jsonpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txdastjson(self):
        ''' Teste Json Dateistruktur Typ '''
        # Vorgabe
        tx_v = self.m_get_strukt()["DASTJSON"]
        # Resultat
        self.ob_test.tx_dastjson = tx_v
        tx_r = self.ob_test.tx_dastjson
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_dastjson"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_lesen(self):
        ''' Teste Struktur lesen '''
        # Vorgabe
        vl_v = None
        # Resultat
        self.ob_test.m_clear()
        self.ob_test.tx_stammpfad = "./doku/test/quelle"
        self.ob_test.tx_jsonpfad = "./doku/test/dasterte.json"
        vl_r = self.ob_test.m_lesen()
        print("#", self.ob_test.tx_stammpfad, "#")
        print("#", self.ob_test.ls_dateien, "#")
        print("#", self.ob_test.ls_verzeich, "#")
        print("#", self.ob_test.tx_datum, "#")
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_lesen"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_typlist(self):
        ''' Teste Typenliste erstellen '''
        # Vorgabe
        vl_v = None
        # Resultat
        vl_r = self.ob_test.m_typlist()
        print("#", self.ob_test.ls_typen, "#")
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_typlist"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_datinfo(self):
        ''' Teste Datei-Info abrufen '''
        # Vorgabe
        vl_v = None
        # Resultat
        vl_r = self.ob_test.m_datinfo()
        print("#", self.ob_test.dc_dateiinfo, "#")
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_datinfo"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_savejson(self):
        ''' Teste Dateistrukur speichern '''
        # Vorgabe
        vl_v = None
        # Resultat
        vl_r = self.ob_test.m_savejson()
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_savejson"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)


if __name__ == '__main__':
    '''
    Test Hauptprogamm
    '''
    # Titel
    print("# DASTERTE #")
    # Anzahl Fehler
    in_anzerr = 0
    # DateiStruktur Objekt testen
    ob_test = Test_DateiStruktur(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Zusammenfassung
    print("# ANZAHL FEHLER: {0}".format(in_anzerr))
