#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dastscob import *
from dastalfn import *

'''
dastscte.py - dateiSTRUKTUR, Struktur CSV Ausgabe, Testmodul
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


class Test_CsvStruktur():
    '''
    KONZEPT
     JSON Ausgabe-Struktur vom Objekt StrukturAusgabe() laden und
     als CSV Tabelle speichern.
    OBJEKT
    StrukturAusgabe()
    METHODEN
    .__init__()           Initialisieren
    .__str__()            Eingebaute String-Funktion
    .m_clear()            Objekt zurücksetzen
    .m_get_dc()           Daten als Wörterbuch zurückgeben
    .m_set_dc(Wörterbuch) Daten mit einem Wörterbuch hinzufügen
    .m_loadjsonor()       Ausgabestruktur JSON laden
    .m_anfang()           HTML Datei-Struktur Anfang
    .m_ende()             HTML Datei-Struktur Ende
    .m_save()             HTML Datei-Struktur speichern
    .m_struktur()         HTML Datei-Struktur Zusammenfassung
    .m_verzeichnisse()    HTML Datei-Struktur Verzeichnis
    VARIABELN
    .tx_jsonpfad          Pfad der Json Ausgabestruktur
    .tx_csvpfad           Pfad der CSV Datei
    .tx_titel             Dokumententitel
    .tx_text              Dokuemntebeschreibung
    .dc_ausgabe           Wörterbuch mit der Ausgabestruktur
    .ls_csv               Tabelle als Liste im CSV Format
    BEMERKUNGEN
     In Test_CsvStruktur.m_get_json() sind Beispiel Strukturen
     dem oben erwähnten Variabeln definiert.
    DARSTELLUNG TABELLE
     +------+------+------+------+------+------+------+------+------+
     |Zeile |Kateg.|Text  |Anzahl|VerNam|DatNam|DatTyp|DatUhr|Grösse|
     +------+------+------+------+------+------+------+------+------+
     |1     |Titel |[Tite]|      |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |2     |Besch.|[Text]|      |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |3     |Zusam.|      |      |[Pfad]|      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |4     |Datum |      |      |      |      |      |[DaTi]|      |
     +------+------+------+------+------+------+------+------+------+
     |5     |AnzVer|      |[x]   |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |6     |AnzDat|      |[x]   |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |7     |AnzTyp|      |[x]   |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |8     |Leer  |---   |---   |---   |---   |---   |---   |---   |
     +------+------+------+------+------+------+------+------+------+
     |9     |Verze.|      |      |[Pfad]|      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |10    |AnzVer|      |[x]   |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |11    |Ver.#1|      |      |[Name]|      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |##    |Ver.##|      |      |[Name]|      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |##    |AnzDat|      |[x]   |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |##    |AnzTyp|      |[x]   |      |      |      |      |      |
     +------+------+------+------+------+------+------+------+------+
     |##    |Dat.#1|      |      |      |[Name]|[Typ] |[DaTi]|[byte]|
     +------+------+------+------+------+------+------+------+------+
     |##    |Dat.##|      |      |      |[Name]|[Typ] |[DaTi]|[byte]|
     +------+------+------+------+------+------+------+------+------+
     |##    |Leer  |---   |---   |---   |---   |---   |---   |---   |
     +------+------+------+------+------+------+------+------+------+
     Weitere Verzeichnisse

    '''

    def __init__(self, in_anzerr):
        ''' Initieren '''
        # Anzahl Fehler
        self.in_anzerr = in_anzerr
        # Test Objekt
        self.ob_test = CsvStruktur()
        # Tests
        self.m_test_str()
        self.m_test_clear()
        self.m_test_setdc()
        self.m_test_getdc()
        self.m_test_txjsonpfad()
        self.m_test_txcsvpfad()
        self.m_test_txtitel()
        self.m_test_txtext()
        self.m_test_dcausgabe()
        self.m_test_lscsv()
        self.m_test_loadjsonor()
        self.m_test_anfang()
        self.m_test_struktur()
        self.m_test_verzeichnisse()
        self.m_test_save()

    def m_get_json(self):
        '''
        Daten für Ausgabestruktur & Attribute zurückgeben
        '''
        dc_ausgabestruktur = {
            "DASTJSON": "STRUKTURAUSGABE",
            "DATUM": "01.06.2022 21:37:05",
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
        dc_daten = {
            "JSONPFAD": "./doku/test/strukturausgabe.json",
            "CSVPFAD": "./doku/test/dastscte.csv",
            "TITEL": "Test DASTSCOB 1",
            "TEXT": "Struktur von Test 1: Script DASTSCOB",
            "AUSGABEJSON": dc_ausgabestruktur,
            "CSV": [["A", "B"], ["a1", "b1"], ["a2", "b2"]]
        }
        return(dc_daten)

    def m_get_daten_liste(self, dc_daten):
        ''' Die Daten-Struktur als Werte und Listen zurückgeben '''
        tx_jsonpfad = dc_daten["JSONPFAD"]
        tx_htmlpfad = dc_daten["CSVPFAD"]
        tx_titel = dc_daten["TITEL"]
        tx_text = dc_daten["TEXT"]
        tx_dastjson = dc_daten["AUSGABEJSON"]["DASTJSON"]
        tx_datum = dc_daten["AUSGABEJSON"]["DATUM"]
        tx_stammpfad = dc_daten["AUSGABEJSON"]["STAMMPFAD"]
        in_datanz = dc_daten["AUSGABEJSON"]["DATEIANZAHL"]
        in_verzanz = dc_daten["AUSGABEJSON"]["VERZEICHNISANZAHL"]
        in_typanz = dc_daten["AUSGABEJSON"]["TYPENANZAHL"]
        ls_verz = dc_daten["AUSGABEJSON"]["VERZEICHNISSE"]
        tx_csv = dc_daten["CSV"]
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
        ls_daten = [tx_jsonpfad, tx_htmlpfad, tx_titel, tx_text,
                    tx_dastjson, tx_datum, tx_stammpfad, in_datanz,
                    in_verzanz, in_typanz, ls_verz, tx_csv,
                    ls_verzneu]
        return(ls_daten)

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

    def m_get_spalten(self):
        ''' Gibt die Spaltenüberschriften als Liste zurück '''
        ls_s = ['Zeile', 'Kategorie', 'Text', 'Anzahl',
                'Verzeichnisnamen', 'Dateiname', 'Dateityp',
                'Datum/Uhrzeit', 'Groesse (bytes)']
        return(ls_s)

    def m_get_textzeilen(self):
        ''' Gibt die Spaltenüberschriften als Liste zurück '''
        ls_t1 = [1, 'Titel', 'Test DASTSCOB 1', '', '', '', '', '', '']
        ls_t2 = [2, 'Beschrieb', 'Struktur von Test 1: Script DASTSCOB',
                 '', '', '', '', '', '']
        return(ls_t1, ls_t2)

    def m_get_csvliste(self):
        ''' Gibt die CSV-Liste zurück '''
        ls_c = [
            ['Zeile', 'Kategorie', 'Text', 'Anzahl', 'Verzeichnisnamen',
             'Dateiname', 'Dateityp', 'Datum/Uhrzeit',
             'Groesse (bytes)'],
            [1, 'Titel', 'Test DASTSCOB 1', '', '', '', '', '', ''],
            [2, 'Beschrieb', 'Struktur von Test 1: Script DASTSCOB', '',
             '', '', '', '', ''],
            [3, 'Hauptverzeichnis', '', '', './dastaldo/daster/quelle',
             '', '', '', ''],
            [4, 'Datum / Uhrzeit', '', '', '', '', '',
             '01.06.2022 21:37:05', ''],
            [5, 'Anzahl Verzeichnisse', '', 4, '', '', '', '', ''],
            [6, 'Anzahl Dateien', '', 9, '', '', '', '', ''],
            [7, 'Anzahl Dateitypen', '', 3, '', '', '', '', ''],
            [8, 'Leerzeile', '---', '---', '---', '---', '---', '---',
             '---'],
            [9, 'Verzeichnis', '', '', 'Hauptverzeichnis', '', '', '',
             ''],
            [10, 'Anzahl Verzeichnisse', '', '3', '', '', '', '', ''],
            [11, 'Verzeichnis #1', '', '', 'pfad1', '', '', '', ''],
            [12, 'Verzeichnis #2', '', '', 'pfad2', '', '', '', ''],
            [13, 'Verzeichnis #3', '', '', 'pfad3', '', '', '', ''],
            [14, 'Anzahl Dateien', '', '0', '', '', '', '', ''],
            [15, 'Anzahl Dateitypen', '', '0', '', '', '', '', ''],
            [16, 'Leerzeile', '---', '---', '---', '---', '---', '---',
             '---'],
            [17, 'Verzeichnis', '', '', 'pfad1', '', '', '', ''],
            [18, 'Anzahl Verzeichnisse', '', '0', '', '', '', '', ''],
            [19, 'Anzahl Dateien', '', '3', '', '', '', '', ''],
            [20, 'Anzahl Dateitypen', '', '3', '', '', '', '', ''],
            [21, 'Datei #1', '', '', '', 'Datei_11', '.txa',
             '27.05.2022 15:01:13', 10],
            [22, 'Datei #2', '', '', '', 'Datei_12', '.txb',
             '27.05.2022 15:00:36', 13],
            [23, 'Datei #3', '', '', '', 'Datei_13', '.txc',
             '27.05.2022 15:00:59', 15],
            [24, 'Leerzeile', '---', '---', '---', '---', '---', '---',
             '---'],
            [25, 'Verzeichnis', '', '', 'pfad2', '', '', '', ''],
            [26, 'Anzahl Verzeichnisse', '', '0', '', '', '', '', ''],
            [27, 'Anzahl Dateien', '', '2', '', '', '', '', ''],
            [28, 'Anzahl Dateitypen', '', '2', '', '', '', '', ''],
            [29, 'Datei #1', '', '', '', 'Datei_21', '.txa',
             '27.05.2022 15:02:01', 20],
            [30, 'Datei #2', '', '', '', 'Datei_22', '.txb',
             '27.05.2022 15:02:11', 21],
            [31, 'Leerzeile', '---', '---', '---', '---', '---', '---',
             '---'],
            [32, 'Verzeichnis', '', '', 'pfad3', '', '', '', ''],
            [33, 'Anzahl Verzeichnisse', '', '0', '', '', '', '', ''],
            [34, 'Anzahl Dateien', '', '4', '', '', '', '', ''],
            [35, 'Anzahl Dateitypen', '', '3', '', '', '', '', ''],
            [36, 'Datei #1', '', '', '', 'Datei_31', '.txa',
             '27.05.2022 15:07:12', 24],
            [37, 'Datei #2', '', '', '', 'Datei_32', '.txb',
             '27.05.2022 15:04:04', 22],
            [38, 'Datei #3', '', '', '', 'Datei_33', '.txc',
             '27.05.2022 15:04:16', 23],
            [39, 'Datei #4', '', '', '', 'Datei_34', '.txa',
             '27.05.2022 15:07:53', 26]
        ]
        return(ls_c)

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
        dc_daten = self.m_get_json()
        vl_r = self.ob_test.m_set_dc(dc_daten)
        # Test & Vergleich
        bl_t = vl_r == vl_v
        tx_test = "Test Methode m_set_dc"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, vl_v, vl_r,
                                        self.in_anzerr)

    def m_test_getdc(self):
        ''' Teste Get DC Methode '''
        # Vorgabe
        dc_v = self.m_get_json()
        # Resultat
        dc_r = self.ob_test.m_get_dc()
        # Test & Vergleich
        ls_v = self.m_get_daten_liste(dc_v)
        ls_r = self.m_get_daten_liste(dc_r)
        tx_test = "Test Methode m_get_dc"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_txjsonpfad(self):
        ''' Teste Json Pfad '''
        # Vorgabe
        dc_daten = self.m_get_json()
        tx_v = dc_daten["JSONPFAD"]
        # Resultat
        self.ob_test.tx_jsonpfad = tx_v
        tx_r = self.ob_test.tx_jsonpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_jsonpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txcsvpfad(self):
        ''' Teste Csv Pfad '''
        # Vorgabe
        dc_daten = self.m_get_json()
        tx_v = dc_daten["CSVPFAD"]
        # Resultat
        self.ob_test.tx_csvpfad = tx_v
        tx_r = self.ob_test.tx_csvpfad
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_csvpfad"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_txtitel(self):
        ''' Teste Titel '''
        # Vorgabe
        dc_daten = self.m_get_json()
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
        dc_daten = self.m_get_json()
        tx_v = dc_daten["TEXT"]
        # Resultat
        self.ob_test.tx_text = tx_v
        tx_r = self.ob_test.tx_text
        # Test & Vergleich
        bl_t = tx_r == tx_v
        tx_test = "Test Attribut tx_text"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_dcausgabe(self):
        ''' Teste Wörterbuch Ausgabe '''
        # Vorgabe
        dc_daten = self.m_get_json()
        dc_v = dc_daten["AUSGABEJSON"]
        # Resultat
        self.ob_test.dc_ausgabe = dc_v
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich
        ls_v = self.m_get_as_liste(dc_v)
        ls_r = self.m_get_as_liste(dc_r)
        tx_test = "Test Attribut dc_ausgabe"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_lscsv(self):
        ''' Teste CSV Liste '''
        # Vorgabe
        dc_daten = self.m_get_json()
        ls_v = dc_daten["CSV"]
        # Resultat
        self.ob_test.ls_csv = ls_v
        ls_r = self.ob_test.ls_csv
        # Test & Vergleich
        tx_test = "Test Attribut ls_csv"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_loadjsonor(self):
        ''' Teste geordnetes Json laden Methode '''
        # Vorgabe
        dc_daten = self.m_get_json()
        dc_daten["AUSGABEJSON"] = {}
        self.ob_test.m_set_dc(dc_daten)
        # Resultat
        self.ob_test.m_loadjsonor()
        dc_r = self.ob_test.dc_ausgabe
        # Test & Vergleich
        dc_v = self.m_get_json()
        ls_v = self.m_get_as_liste(dc_v["AUSGABEJSON"])
        ls_r = self.m_get_as_liste(dc_r)
        tx_test = "Test Methode m_loadjsonor"
        self.in_anzerr = f_test_liste(tx_test, ls_v, ls_r,
                                      self.in_anzerr)

    def m_test_anfang(self):
        ''' Teste Anfang Methode '''
        # Vorgabe
        tx_v = str(self.m_get_spalten())
        # Resultat
        self.ob_test.m_anfang()
        ls_r = self.ob_test.ls_csv
        tx_r = str(ls_r)
        # Test & Vergleich
        bl_t = tx_v in tx_r
        tx_test = "Test Methode m_anfang"
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_struktur(self):
        ''' Teste Struktur Methode '''
        # Vorgabe
        ls_v = self.m_get_textzeilen()
        tx_v1 = str(ls_v[0])
        tx_v2 = str(ls_v[1])
        # Resultat
        self.ob_test.m_struktur()
        ls_r = self.ob_test.ls_csv
        tx_r = str(ls_r)
        # Test & Vergleich
        bl_t = tx_v1 in tx_r and tx_v2 in tx_r
        tx_test = "Test Methode m_struktur"
        tx_v = "{0} | {1}".format(tx_v1, tx_v2)
        self.in_anzerr = f_test_einzeln(tx_test, bl_t, tx_v, tx_r,
                                        self.in_anzerr)

    def m_test_verzeichnisse(self):
        ''' Teste Verzeichnis Methode '''
        # Vorgabe
        tx_v = str(self.m_get_csvliste())
        # Resultat
        self.ob_test.m_verzeichnisse()
        ls_r = self.ob_test.ls_csv
        tx_r = str(ls_r)
        # Test & Vergleich
        bl_t = tx_v == tx_r
        tx_test = "Test Methode m_verzeichnisse"
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
    print("# DASTSCTE #")
    # Anzahl Fehler
    in_anzerr = 0
    # DateiStruktur Objekt testen
    ob_test = Test_CsvStruktur(in_anzerr)
    in_anzerr = ob_test.in_anzerr
    # Zusammenfassung
    print("# ANZAHL FEHLER: {0}".format(in_anzerr))
