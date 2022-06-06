#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dastvgob import *
from dastalfn import *

'''
dastvgte.py - dateiSTRUKTUR, Strukturen vergleichen, Testmodul
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


class Test_Vergleich():
    '''
    KONZEPT
     2 Json Datei-Strukturen vom Objekt DateiStruktur() lesen,
     vergleichen und die Unterschiede als Json speichern.
    OBJEKT
    Vergleich()
    METHODEN
    .__init__()           Initialisieren
    .__str__()            Eingebaute String-Funktion
    .m_clear()            Objekt zurücksetzen
    .m_set_dc(Wörterbuch) Daten mit einem Wörterbuch hinzufügen
    .m_get_dc()           Daten als Wörterbuch zurückgeben
    .m_analize()          Ziel und Quelle analysieren
    .m_loadjsons          Json Dateistrukturen von Quelle und Ziel laden
    .m_savejson()             Unterschiede als Json speichern

    VARIABELN
    .dc_quelle            Wörterbuch der Quell Dateistruktur
    .dc_ziel              Wörterbuch der Ziel Dateistruktur
    .dc_diff              Wörterbuch mit den Unterschieden
    .tx_quelljson         Pfad zur Quell Json Dateistruktur
    .tx_zieljson          Pfad zur Ziel Json Dateistruktur
    .tx_diffjson          Pfad zum Unterschiede Json
    BEMERKUNGEN
     In Test_DateiStruktur.m_get_quelle(), .m_get_ziel() und
     .m_get_diff sind Beispiele der oben erwähnten Wörterbücher
     definiert.
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        # Anzahl Fehler
        self.in_anzerr = in_anzerr
        # Test Objekt
        self.ob_test = Vergleich()
        # Json Pfade
        self.tx_quelljson = "./doku/test/dastvgte_quelle.json"
        self.tx_zieljson = "./doku/test/dastvgte_ziel.json"
        self.tx_diffjson = "./doku/test/dastvgte_diff.json"
        # Tests
        self.m_test_str()
        self.m_test_clear()
        self.m_test_setdc()
        self.m_test_getdc()
        self.m_test_dcquelle()
        self.m_test_dcziel()
        self.m_test_dcdiff()
        self.m_test_loadjsons()
        self.m_test_analize()
        self.m_test_savejson()

    def m_get_quelle(self):
        ''' Datei-Struktur der Quelle zurückgeben '''
        dc_q = {
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
                "./doku/test/quelle/pfad1",
                "./doku/test/quelle/pfad2",
                "./doku/test/quelle/pfad3",
                "./doku/test/quelle"
            ],
            "DATUM": "05.06.2022 15:03:04",
            "JSONPFAD": "./doku/test/dastvgte_quelle.json",
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
            }
        }
        return(dc_q)

    def m_get_ziel(self):
        ''' Datei-Struktur des Ziels zurückgeben '''
        dc_z = {
            "DASTJSON": "DATEISTRUKTUR",
            "DATEILISTE": [
                "./doku/test/ziel/Datei_01.txe",
                "./doku/test/ziel/pfad2/Datei_21.txa",
                "./doku/test/ziel/pfad2/Datei_22.txb",
                "./doku/test/ziel/pfad3/Datei_31.txa",
                "./doku/test/ziel/pfad3/Datei_32.txb",
                "./doku/test/ziel/pfad3/Datei_33.txa",
                "./doku/test/ziel/pfad3/Datei_35.txb",
                "./doku/test/ziel/pfad4/Datei_41.txa",
                "./doku/test/ziel/pfad4/Datei_42.txb",
                "./doku/test/ziel/pfad4/Datei_43.txc",
                "./doku/test/ziel/pfad4/Datei_44.txd",
                "./doku/test/ziel/pfad5/Datei_51.txe",
                "./doku/test/ziel/pfad5/Datei_52.txe"
            ],
            "VERZEICHNISLISTE": [
                "./doku/test/ziel/pfad2",
                "./doku/test/ziel/pfad3",
                "./doku/test/ziel/pfad4",
                "./doku/test/ziel/pfad5",
                "./doku/test/ziel"
            ],
            "DATUM": "05.06.2022 15:02:02",
            "JSONPFAD": "./doku/test/dastvgte_ziel.json",
            "STAMMPFAD": "./doku/test/ziel",
            "TYPENLISTE": [".txa", ".txb", ".txc", ".txd", ".txe"],
            "DATEIINFO": {
                "Datei_01.txe": ["05.06.2022 13:59:45", 15],
                "pfad2/Datei_21.txa": ["27.05.2022 15:02:01", 20],
                "pfad2/Datei_22.txb": ["27.05.2022 15:02:11", 21],
                "pfad3/Datei_31.txa": ["27.05.2022 15:07:12", 24],
                "pfad3/Datei_32.txb": ["05.06.2022 13:54:43", 26],
                "pfad3/Datei_33.txa": ["27.05.2022 15:04:16", 23],
                "pfad3/Datei_35.txb": ["05.06.2022 13:59:04", 24],
                "pfad4/Datei_41.txa": ["05.06.2022 13:58:14", 22],
                "pfad4/Datei_42.txb": ["05.06.2022 13:58:24", 21],
                "pfad4/Datei_43.txc": ["05.06.2022 13:58:35", 22],
                "pfad4/Datei_44.txd": ["05.06.2022 13:58:48", 22],
                "pfad5/Datei_51.txe": ["05.06.2022 14:00:27", 23],
                "pfad5/Datei_52.txe": ["05.06.2022 14:00:38", 22]
            }
        }
        return(dc_z)

    def m_get_diff(self):
        ''' Unterschiede von Quelle und Ziel zurückgeben '''
        dc_d = {
            "DASTJSON": "VERGLEICHSTRUKTUR",
            "STAMMPFAD_QUELLE": "./doku/test/quelle",
            "STAMMPFAD_ZIEL": "./doku/test/ziel",
            "DATUM_STRUKTUR_QUELLE": "05.06.2022 15:03:04",
            "DATUM_STRUKTUR_ZIEL": "05.06.2022 15:02:02",
            "ANZAHL_DATEIEN_QUELLE": 9,
            "ANZAHL_DATEIEN_ZIEL": 13,
            "ANZAHL_VERZEICHNISSE_QUELLE": 4,
            "ANZAHL_VERZEICHNISSE_ZIEL": 5,
            "ANZAHL_TYPEN_QUELLE": 3,
            "ANZAHL_TYPEN_ZIEL": 5,
            "DATEIEN_NUR_QUELLE": [
                "pfad1/Datei_11.txa",
                "pfad1/Datei_12.txb",
                "pfad1/Datei_13.txc",
                "pfad3/Datei_33.txc",
                "pfad3/Datei_34.txa"
            ],
            "DATEIEN_NUR_ZIEL": [
                "Datei_01.txe",
                "pfad3/Datei_33.txa",
                "pfad3/Datei_35.txb",
                "pfad4/Datei_41.txa",
                "pfad4/Datei_42.txb",
                "pfad4/Datei_43.txc",
                "pfad4/Datei_44.txd",
                "pfad5/Datei_51.txe",
                "pfad5/Datei_52.txe"
            ],
            "DATEIEN_GEMEINSAM": [
                "pfad2/Datei_21.txa",
                "pfad2/Datei_22.txb",
                "pfad3/Datei_31.txa",
                "pfad3/Datei_32.txb"
            ],
            "VERZEICHNISSE_NUR_QUELLE": [
                "pfad1",
            ],
            "VERZEICHNISSE_NUR_ZIEL": [
                "pfad4",
                "pfad5"
            ],
            "VERZEICHNISSE_GEMEINSAM": [
                ".",
                "pfad2",
                "pfad3"
            ],
            "TYPEN_NUR_QUELLE": [],
            "TYPEN_NUR_ZIEL": [
                ".txd",
                ".txe"
            ],
            "TYPEN_GEMEINSAM": [
                ".txa",
                ".txb",
                ".txc"
            ],
            "UNTERSCHIEDLICHE_INFO": {
                "pfad3/Datei_32.txb": [
                    "27.05.2022 15:04:04", 22,
                    "05.06.2022 13:54:43", 26
                ]
            }
        }
        return(dc_d)

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

    def m_get_diff_liste(self, dc_diff):
        ''' Das Unterschied Wörterbuch als Werte und Liste '''
        tx_dastjson = dc_diff["DASTJSON"]
        tx_stammquel = dc_diff["STAMMPFAD_QUELLE"]
        tx_stammziel = dc_diff["STAMMPFAD_ZIEL"]
        tx_datumstrktquel = dc_diff["DATUM_STRUKTUR_QUELLE"]
        tx_datumstrktziel = dc_diff["DATUM_STRUKTUR_ZIEL"]
        in_anzdatquel = dc_diff["ANZAHL_DATEIEN_QUELLE"]
        in_anzdatziel = dc_diff["ANZAHL_DATEIEN_ZIEL"]
        in_anzverquel = dc_diff["ANZAHL_VERZEICHNISSE_QUELLE"]
        in_anzverziel = dc_diff["ANZAHL_VERZEICHNISSE_ZIEL"]
        in_anztypquel = dc_diff["ANZAHL_TYPEN_QUELLE"]
        in_anztypziel = dc_diff["ANZAHL_TYPEN_ZIEL"]
        ls_datnurquel = dc_diff["DATEIEN_NUR_QUELLE"]
        ls_datnurziel = dc_diff["DATEIEN_NUR_ZIEL"]
        ls_datgemeins = dc_diff["DATEIEN_GEMEINSAM"]
        ls_vernurquel = dc_diff["VERZEICHNISSE_NUR_QUELLE"]
        ls_vernurziel = dc_diff["VERZEICHNISSE_NUR_ZIEL"]
        ls_vergemeins = dc_diff["VERZEICHNISSE_GEMEINSAM"]
        ls_typnurquel = dc_diff["TYPEN_NUR_QUELLE"]
        ls_typnurziel = dc_diff["TYPEN_NUR_ZIEL"]
        ls_typgemeins = dc_diff["TYPEN_GEMEINSAM"]
        ls_diffinfo = self.m_get_diffinfo_liste(
            dc_diff["UNTERSCHIEDLICHE_INFO"]
        )
        # Als Gesamtliste zurückgeben
        ls_diff = [tx_dastjson, tx_stammquel, tx_stammziel,
                   tx_datumstrktquel, tx_datumstrktziel, in_anzdatquel,
                   in_anzdatziel, in_anzverquel, in_anzverziel,
                   in_anztypquel, in_anztypziel, ls_datnurquel,
                   ls_datnurziel, ls_datgemeins, ls_vernurquel,
                   ls_vernurziel, ls_vergemeins, ls_typnurquel,
                   ls_typnurziel, ls_typgemeins, ls_diffinfo]
        return(ls_diff)

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

    def m_get_diffinfo_liste(self, dc_diff):
        ''' Das Wörterbuch Unterschiede Datei-Info als Liste '''
        ls_diffinf = []
        for tx_datei, ls_info in dc_diff.items():
            ls_diffinf.append("{0}, {1}, {2}".format(
                tx_datei,
                ls_info[0],
                ls_info[1]
            ))
        ls_diffinf.sort()
        return(ls_diffinf)

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
        dc_daten = {
            "QUELLE": self.m_get_quelle(),
            "ZIEL": self.m_get_ziel(),
            "VERGLEICH": self.m_get_diff(),
            "QUELLJSON": self.tx_quelljson,
            "ZIELJSON": self.tx_zieljson,
            "VERGLEICHJSON": self.tx_diffjson
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
        dc_v = {
            "QUELLE": self.m_get_quelle(),
            "ZIEL": self.m_get_ziel(),
            "VERGLEICH": self.m_get_diff(),
            "QUELLJSON": self.tx_quelljson,
            "ZIELJSON": self.tx_zieljson,
            "VERGLEICHJSON": self.tx_diffjson
        }
        # Resultat
        dc_r = self.ob_test.m_get_dc()
        # Test & Vergleich DATEISTRUKTUR QUELLE
        ls_v = self.m_get_ds_liste(dc_v["QUELLE"])
        ls_r = self.m_get_ds_liste(dc_r["QUELLE"])
        tx_test = "Test Methode m_get_dc[QUELLE]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)
        # Test & Vergleich DATEISTRUKTUR ZIEL
        ls_v = self.m_get_ds_liste(dc_v["ZIEL"])
        ls_r = self.m_get_ds_liste(dc_r["ZIEL"])
        tx_test = "Test Methode m_get_dc[ZIEL]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)
        # Test & Vergleich DATEISTRUKTUR VERGLEICH
        ls_v = self.m_get_diff_liste(dc_v["VERGLEICH"])
        ls_r = self.m_get_diff_liste(dc_r["VERGLEICH"])
        tx_test = "Test Methode m_get_dc[VERGLEICH]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)
        # Test & Vergleich Daten
        ls_v = [dc_v["QUELLJSON"], dc_v["ZIELJSON"],
                dc_v["VERGLEICHJSON"]]
        ls_r = [dc_r["QUELLJSON"], dc_r["ZIELJSON"],
                dc_r["VERGLEICHJSON"]]
        tx_test = "Test Methode m_get_dc[..JSON]"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_dcquelle(self):
        ''' Teste Wörterbuch Quelle '''
        # Vorgabe
        dc_v = self.m_get_quelle()
        # Resultat
        self.ob_test.dc_quelle = dc_v
        dc_r = self.ob_test.dc_quelle
        # Test & Vergleich
        ls_v = self.m_get_ds_liste(dc_v)
        ls_r = self.m_get_ds_liste(dc_r)
        tx_test = "Test Attribut dc_quelle"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_dcziel(self):
        ''' Teste Wörterbuch Ziel '''
        # Vorgabe
        dc_v = self.m_get_ziel()
        # Resultat
        self.ob_test.dc_ziel = dc_v
        dc_r = self.ob_test.dc_ziel
        # Test & Vergleich
        ls_v = self.m_get_ds_liste(dc_v)
        ls_r = self.m_get_ds_liste(dc_r)
        tx_test = "Test Attribut dc_ziel"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_dcdiff(self):
        ''' Teste Wörterbuch Unterschiede '''
        # Vorgabe
        dc_v = self.m_get_diff()
        # Resultat
        self.ob_test.dc_diff = dc_v
        dc_r = self.ob_test.dc_diff
        # Test & Vergleich
        ls_v = self.m_get_diff_liste(dc_v)
        ls_r = self.m_get_diff_liste(dc_r)
        tx_test = "Test Attribut dc_diff"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_txquelljson(self):
        ''' Teste Quell Json '''
        # Vorgabe
        t_v = self.tx_quelljson
        # Resultat
        self.ob_test.tx_quelljson = tx_v
        tx_r = self.ob_test.tx_quelljson
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_quelljson"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txzieljson(self):
        ''' Teste Ziel Json '''
        # Vorgabe
        t_v = self.tx_zieljson
        # Resultat
        self.ob_test.tx_zieljson = tx_v
        tx_r = self.ob_test.tx_zieljson
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_zieljson"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txdiffjson(self):
        ''' Teste Diff Json '''
        # Vorgabe
        t_v = self.tx_diffjson
        # Resultat
        self.ob_test.tx_diffjson = tx_v
        tx_r = self.ob_test.tx_diffjson
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_diffjson"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_loadjsons(self):
        ''' Teste Struktur lesen '''
        # Vorgabe
        vl_v = None
        # Resultat
        self.ob_test.m_clear()
        self.ob_test.tx_quelljson = self.tx_quelljson
        self.ob_test.tx_zieljson = self.tx_zieljson
        self.ob_test.tx_diffjson = self.tx_diffjson
        vl_r = self.ob_test.m_loadjsons()
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_lesen"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_analize(self):
        ''' Teste Unterschiede analysieren '''
        # Vorgabe
        dc_v = self.m_get_diff()
        # Resultat
        self.ob_test.m_analize()
        dc_r = self.ob_test.dc_diff
        # Test & Vergleich DATEISTRUKTUR VERGLEICH
        ls_v = self.m_get_diff_liste(dc_v)
        ls_r = self.m_get_diff_liste(dc_r)
        tx_test = "Test Methode m_test_analize"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
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
    ob_test = Test_Vergleich(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Zusammenfassung
    print("# ANZAHL FEHLER: {0}".format(in_anzerr))
