#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dastvhob import *
from dastalfn import *

'''
dastvhte.py - dateiSTRUKTUR, Vergleich HTML Ausgabe, Testmodul
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


class Test_HtmlVergleich():
    '''
    KONZEPT
     JSON Unterschiede-Struktur vom Objekt Vergleich() laden und
     als HTML Dokument speichern.
    OBJEKT
    HtmlVergleich()
    METHODEN
    .__init__()           Initialisieren
    .__str__()            Eingebaute String-Funktion
    .m_clear()            Objekt zurücksetzen
    .m_get_dc()           Daten als Wörterbuch zurückgeben
    .m_set_dc(Wörterbuch) Daten mit einem Wörterbuch hinzufügen
    .m_loadjson()         Vergleich-Struktur JSON laden
    .m_anfang()           HTML Vergleich Anfang
    .m_zusammenfassung()  HTML Zusammenfassung
    .m_dateinamen()       HTML Dateinamen Vergleich
    .m_verzeichnisse()    HTMl Verzeichnis Vergleich
    .m_dateitypen()       HTML Dateitypen Vergleich
    .m_dateiinfo()        HTML Vergleich unterschiedlicher Datei-Info
    .m_ende()             HTML Vergleich Ende
    .m_save()             HTML Vergleich speichern
    VARIABELN
    .tx_jsonpfad          Pfad der Json Vergleich-Struktur
    .tx_htmlpfad          Pfad der HTML Datei
    .tx_titel             Dokumententitel
    .tx_text              Dokuemntebeschreibung
    .dc_vergleich         Wörterbuch mit der Vergleich-Struktur
    .tx_html              HTML Text
    BEMERKUNGEN
     In Test_HtmlStruktur.m_get_json() sind Beispiel Strukturen
     dem oben erwähnten Variabeln definiert.
    DARSTELLUNG HTML
     [TITEL]
     [Text]
     -
     +--------------------+---------------------+---------------------+
     |                    | Quelle              | Ziel                |
     +--------------------+---------------------+---------------------+
     |Pfad                |[quellpfad]          |[zielpfad]           |
     +--------------------+---------------------+---------------------+
     |Erfassungsdatum     |[tt.mm.jjjj ss:mm:sk]|[tt.mm.jjjj ss:mm:sk]|
     +--------------------+---------------------+---------------------+
     |Anzahl Dateien      |[x]                  |[x]                  |
     +--------------------+---------------------+---------------------+
     |Anzahl Verzeichniss.|[x]                  |[x]                  |
     +--------------------+---------------------+---------------------+
     |Anzahl Typen        |[x]                  |[x]                  |
     +--------------------+---------------------+---------------------+
     |Vergleich nach Dateinamen                                       |
     +--------------------+-------------------------------------------+
     |Gemeinsame Dateien  |[pfad/name.erw]                            |
     |                    |[...]                                      |
     +--------------------+---------------------+---------------------+
     |Dateien nur Quelle  |[pfad/name.erw]      |                     |
     |                    |[...]                |                     |
     +--------------------+---------------------+---------------------+
     |Dateien nur Ziel    |                     |[pfad/name.erw]      |
     |                    |                     |[...]                |
     +--------------------+---------------------+---------------------+
     |Vergleich nach Verzeichnisnamen                                 |
     +--------------------+---------------------+---------------------+
     |Gemeinsame Verzeich.|[pfad]               |[pfad]               |
     |                    |[...]                |[...]                |
     +--------------------+---------------------+---------------------+
     |Verzeich. nur Quelle|[pfad]               |                     |
     |                    |[...]                |                     |
     +--------------------+---------------------+---------------------+
     |Verzeichn. nur Ziel |                     |[pfad]               |
     |                    |                     |[...]                |
     +--------------------+---------------------+---------------------+
     |Vergleich nach Dateitypen                                       |
     +--------------------+---------------------+---------------------+
     |Gemeinsame Typen    |[.typ]               |[.typ]               |
     |                    |[...]                |[...]                |
     +--------------------+---------------------+---------------------+
     |Typen nur in Quelle |[.typ]               |                     |
     |                    |[...]                |                     |
     +--------------------+---------------------+---------------------+
     |Typen nur im Ziel   |                     |[.typ]               |
     |                    |                     |[...]                |
     +--------------------+---------------------+---------------------+
     |Gleiche Dateipfade mit unterschiedlicher Dateigrösse / Datum    |
     +--------------------+---------------------+---------------------+
     |[pfad/name.typ]     |[x] bytes            |[x] bytes            |
     |                    |[tt.mm.jjjj ss:mm:sk]|[tt.mm.jjjj ss:mm:sk]|
     +--------------------+---------------------+---------------------+
     |[...]               |[...] bytes          |[...] bytes          |
     |                    |[...]                |[...]                |
     +--------------------+---------------------+---------------------+
    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        # Anzahl Fehler
        self.in_anzerr = in_anzerr
        # Test Objekt
        self.ob_test = HtmlVergleich()
        # Tests
        self.m_test_str()
        self.m_test_clear()
        self.m_test_setdc()
        self.m_test_getdc()
        self.m_test_txjsonpfad()
        self.m_test_txhtmlpfad()
        self.m_test_txtitel()
        self.m_test_txtext()
        self.m_test_dcvergleich()
        self.m_test_txhtml()
        self.m_test_loadjsonvg()
        self.m_test_anfang()
        self.m_test_zusammenfassung()
        self.m_test_namvertyp()
        self.m_test_dateiinfo()
        self.m_test_ende()
        self.m_test_save()

    def m_get_diff(self):
        ''' Unterschiede von Quelle und Ziel als Wörterbuch '''
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

    def m_get_diff_liste(self, dc_diff):
        ''' Unterschied Wörterbuch als Werte und Liste '''
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

    def m_get_diffinfo_liste(self, dc_diff):
        ''' Wörterbuch Unterschiede Datei-Info als Liste '''
        ls_diffinf = []
        for tx_datei, ls_info in dc_diff.items():
            ls_diffinf.append("{0}, {1}, {2}".format(
                tx_datei,
                ls_info[0],
                ls_info[1]
            ))
        ls_diffinf.sort()
        return(ls_diffinf)

    def m_get_data(self):
        ''' Daten als Wörterbuch wie ..set_dc(..) zurückgeben '''

        dc_d = {
            "JSONPFAD": "./doku/test/strukturvergleich.json",
            "HTMLPFAD": "./doku/test/dastvhte.html",
            "TITEL": "Test DASTVHOB 1",
            "TEXT": "Struktur von Test 1: Script DASTVHOB",
            "VERGLEICHJSON": self.m_get_diff(),
            "HTML": "<!DOCTYPE html><html></html>"
        }
        return(dc_d)

    def m_get_data_liste(self, dc_daten):
        ''' Wörterbuch Daten als Liste zurückgeben '''
        tx_jsonpfad = dc_daten["JSONPFAD"]
        tx_htmlpfad = dc_daten["HTMLPFAD"]
        tx_titel = dc_daten["TITEL"]
        tx_text = dc_daten["TEXT"]
        tx_html = dc_daten["HTML"]
        ls_vergleichliste = self.m_get_diff_liste(
            dc_daten["VERGLEICHJSON"]
        )
        # Gesamtliste zurückgeben
        ls_daten = [tx_jsonpfad, tx_htmlpfad, tx_titel, tx_text]
        ls_daten.extend(ls_vergleichliste)
        ls_daten.append(tx_html)
        return(ls_daten)

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
        dc_daten = self.m_get_data()
        vl_r = self.ob_test.m_set_dc(dc_daten)
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_set_dc"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_getdc(self):
        ''' Teste Get DC Methode '''
        # Vorgabe
        dc_v = self.m_get_data()
        # Resultat
        self.ob_test.m_set_dc(dc_v)
        dc_r = self.ob_test.m_get_dc()
        # Test & Vergleich
        ls_v = self.m_get_data_liste(dc_v)
        ls_r = self.m_get_data_liste(dc_r)
        tx_test = "Test Methode m_get_dc"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_txjsonpfad(self):
        ''' Teste Json Pfad '''
        # Vorgabe
        dc_daten = self.m_get_data()
        tx_v = dc_daten["JSONPFAD"]
        # Resultat
        self.ob_test.tx_jsonpfad = tx_v
        tx_r = self.ob_test.tx_jsonpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_jsonpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txhtmlpfad(self):
        ''' Teste HMTL Pfad '''
        # Vorgabe
        dc_daten = self.m_get_data()
        tx_v = dc_daten["HTMLPFAD"]
        # Resultat
        self.ob_test.tx_htmlpfad = tx_v
        tx_r = self.ob_test.tx_htmlpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_htmlpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txtitel(self):
        ''' Teste Titel '''
        # Vorgabe
        dc_daten = self.m_get_data()
        tx_v = dc_daten["TITEL"]
        # Resultat
        self.ob_test.tx_titel = tx_v
        tx_r = self.ob_test.tx_titel
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_titel"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txtext(self):
        ''' Teste Text '''
        # Vorgabe
        dc_daten = self.m_get_data()
        tx_v = dc_daten["TEXT"]
        # Resultat
        self.ob_test.tx_text = tx_v
        tx_r = self.ob_test.tx_text
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_text"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_dcvergleich(self):
        ''' Teste Wörterbuch Ausgabe '''
        # Vorgabe
        dc_daten = self.m_get_data()
        dc_v = dc_daten["VERGLEICHJSON"]
        # Resultat
        self.ob_test.dc_ausgabe = dc_v
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich
        ls_v = self.m_get_diff_liste(dc_v)
        ls_r = self.m_get_diff_liste(dc_r)
        tx_test = "Test Attribut dc_ausgabe"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_txhtml(self):
        ''' Teste HTML Text '''
        # Vorgabe
        dc_daten = self.m_get_data()
        tx_v = dc_daten["HTML"]
        # Resultat
        self.ob_test.tx_html = tx_v
        tx_r = self.ob_test.tx_html
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_html"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_loadjsonvg(self):
        ''' Teste Methode Verlgeich Json laden '''
        # Vorgabe
        dc_daten = self.m_get_data()
        dc_daten["VERGLEICHJSON"] = {}
        self.ob_test.m_set_dc(dc_daten)
        # Resultat
        self.ob_test.m_loadjsonvg()
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich
        dc_v = self.m_get_data()["VERGLEICHJSON"]
        ls_v = self.m_get_diff_liste(dc_v)
        ls_r = self.m_get_diff_liste(dc_r)
        tx_test = "Test Methode m_prepare"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_anfang(self):
        ''' Teste Anfang Methode '''
        # Vorgabe
        tx_v = '<!DOCTYPE html><html>'
        # Resultat
        self.ob_test.m_anfang()
        tx_r = self.ob_test.tx_html
        # Test & Vergleich
        bl_t = tx_v in tx_r
        tx_test = "Test Methode m_anfang"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_zusammenfassung(self):
        ''' Teste Vergleich Zusammenfassung Methode '''
        # Vorgabe
        tx_v = '<td>Erfassungsdatum</td>'
        # Resultat
        self.ob_test.m_zusammenfassung()
        tx_r = self.ob_test.tx_html
        # Test & Vergleich
        bl_t = tx_v in tx_r
        tx_test = "Test Methode m_zusammenfassung"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_namvertyp(self):
        ''' Teste Dateinamen Vergleich Methode '''
        # Vorgabe
        tx_v1 = ''.join(['<td colspan="3"><b>',
                        'Vergleich nach Dateipfaden</b></td>'])
        tx_v2 = ''.join(['<td colspan="3"><b>',
                        'Vergleich nach Verzeichnispfaden</b></td>'])
        tx_v3 = ''.join(['<td colspan="3"><b>',
                        'Vergleich nach Dateitypen</b></td>'])
        # Resultat
        self.ob_test.m_namvertyp()
        tx_r = self.ob_test.tx_html
        # Test & Vergleich Dateipfade
        bl_t1 = tx_v1 in tx_r
        tx_test = "Test Methode m_verzeichnisse:Dateipfade"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t1, tx_v1, tx_r,
                                        self.in_anzerr)
        # Test & Vergleich Verzeichnispfade
        bl_t2 = tx_v2 in tx_r
        tx_test = "Test Methode m_verzeichnisse:Verzeichnispfade"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t2, tx_v2, tx_r,
                                        self.in_anzerr)
        # Test & Vergleich Dateitypen
        bl_t3 = tx_v3 in tx_r
        tx_test = "Test Methode m_verzeichnisse:Dateitypen"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t3, tx_v3, tx_r,
                                        self.in_anzerr)

    def m_test_dateiinfo(self):
        ''' Teste Dateitypen Vergleich Methode '''
        # Vorgabe
        tx_v = ''.join(['<td colspan="3">',
                        'Gleiche Dateipfade mit unterschiedlicher ',
                        'Dateigrösse / Datum</td>'])
        # Resultat
        self.ob_test.m_dateiinfo()
        tx_r = self.ob_test.tx_html
        # Test & Vergleich
        bl_t = tx_v in tx_r
        tx_test = "Test Methode m_verzeichnisse"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_ende(self):
        ''' Teste Ende Methode '''
        # Vorgabe
        tx_v = '</body></html>'
        # Resultat
        self.ob_test.m_ende()
        tx_r = self.ob_test.tx_html
        # Test & Vergleich
        bl_t = tx_v in tx_r
        tx_test = "Test Methode m_ende"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_save(self):
        ''' Teste Save Methode '''
        # Vorgabe
        vl_v = None
        # Resultat
        vl_r = self.ob_test.m_save()
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_save"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)


if __name__ == '__main__':
    '''
    Test Hauptprogamm
    '''
    # Titel
    print("# DASTSHTE #")
    # Anzahl Fehler
    in_anzerr = 0
    # DateiStruktur Objekt testen
    ob_test = Test_HtmlVergleich(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Zusammenfassung
    print("# ANZAHL FEHLER: {0}".format(in_anzerr))
