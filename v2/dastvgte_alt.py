#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_3 import *
from test_funktionen import *

'''
test_vergleich.py - [d]atei[s]strukturen <Vergleich> Test
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


def f_get_strukt_neu():
    '''
    Neue Version der Datei-Strukturen für Quele und Ziel zurückgeben
    '''
    dc_quelle = {
        "DATEILISTE": [
            "/quelle/pfad1/Datei_11.tya",
            "/quelle/pfad1/Datei_12.tyb",
            "/quelle/pfad1/Datei_13.tyc",
            "/quelle/pfad2/Datei_21.tya",
            "/quelle/pfad2/Datei_22.tyb",
            "/quelle/pfad3/Datei_31.tya",
            "/quelle/pfad3/Datei_32.tyb",
            "/quelle/pfad3/Datei_33.tyc",
            "/quelle/pfad3/Datei_34.tya"
        ],
        "VERZEICHNISLISTE": ["/quelle", "/quelle/pfad1",
                             "/quelle/pfad2", "/quelle/pfad3"],
        "DATUM": "18.01.2022 21:52:00",
        "STAMMPFAD": "/quelle",
        "TYPENLISTE": [".tya", ".tyb", ".tyc"],
        "DATEIINFO": {
            "pfad1/Datei_11.tya": ["25.12.2021 15:34:00", 16],
            "pfad1/Datei_12.tyb": ["25.12.2021 15:35:00", 32],
            "pfad1/Datei_13.tyc": ["25.12.2021 15:36:00", 64],
            "pfad2/Datei_21.tya": ["25.12.2021 15:37:00", 80],
            "pfad2/Datei_22.tyb": ["25.12.2021 15:38:00", 96],
            "pfad3/Datei_31.tya": ["25.12.2021 15:39:00", 112],
            "pfad3/Datei_32.tyb": ["25.12.2021 15:40:00", 128],
            "pfad3/Datei_33.tyc": ["25.12.2021 15:41:00", 144],
            "pfad3/Datei_34.tya": ["25.12.2021 15:42:00", 160]
        }
    }
    dc_ziel = {
        "DATEILISTE": [
            "/ziel/pfad2/Datei_21.tya",
            "/ziel/pfad2/Datei_22.tyb",
            "/ziel/pfad3/Datei_31.tya",
            "/ziel/pfad3/Datei_32.tyb",
            "/ziel/pfad3/Datei_33.tya",
            "/ziel/pfad3/Datei_35.tyb",
            "/ziel/pfad4/Datei_41.tya",
            "/ziel/pfad4/Datei_42.tyb",
            "/ziel/pfad4/Datei_43.tyc",
            "/ziel/pfad4/Datei_44.tyd",
            "/ziel/Datei_01.tye",
            "/ziel/pfad5/Datei_51.tye",
            "/ziel/pfad5/Datei_52.tye"
        ],
        "VERZEICHNISLISTE": ["/ziel", "/ziel/pfad2", "/ziel/pfad3",
                             "/ziel/pfad4", "/ziel/pfad5"],
        "DATUM": "18.01.2022 22:07:00",
        "STAMMPFAD": "/ziel",
        "TYPENLISTE": [".tya", ".tyb", ".tyc", ".tyd", ".tye"],
        "DATEIINFO": {
            "pfad2/Datei_21.tya": ["25.12.2021 15:37:00", 80],
            "pfad2/Datei_22.tyb": ["25.12.2021 15:38:00", 96],
            "pfad3/Datei_31.tya": ["25.12.2021 15:39:00", 112],
            "pfad3/Datei_32.tyb": ["07.01.2022 20:42:00", 129],
            "pfad3/Datei_33.tya": ["06.01.2022 20:40:00", 1440],
            "pfad3/Datei_35.tyb": ["08.01.2022 20:43:00", 1600],
            "pfad4/Datei_41.tya": ["25.12.2021 15:34:00", 160],
            "pfad4/Datei_42.tyb": ["25.12.2021 15:35:00", 320],
            "pfad4/Datei_43.tyc": ["25.12.2021 15:36:00", 640],
            "pfad4/Datei_44.tyd": ["05.01.2022 20:38:00", 1280],
            "Datei_01.tye": ["09.01.2022 20:44:00", 8],
            "pfad5/Datei_51.tye": ["01.01.2022 20:52:00", 800],
            "pfad5/Datei_52.tye": ["02.01.2022 20:53:00", 960]
        }
    }
    return(dc_quelle, dc_ziel)


def f_vergl_stukt_neu():
    '''
    Soll Ergebnis der Analyse der beiden neuen Strukturen
    zurückgeben
    '''
    dc_diff = {
        "DATUM_STRUKTUR_QUELLE": "18.01.2022 21:52:00",
        "DATUM_STRUKTUR_ZIEL": "18.01.2022 22:07:00",
        "ANZAHL_DATEIEN_QUELLE": 9,
        "ANZAHL_DATEIEN_ZIEL": 13,
        "ANZAHL_VERZEICHNISSE_QUELLE": 4,
        "ANZAHL_VERZEICHNISSE_ZIEL": 5,
        "ANZAHL_TYPEN_QUELLE": 3,
        "ANZAHL_TYPEN_ZIEL": 5,
        "DATEIEN_NUR_QUELLE": [
            "pfad1/Datei_11.tya",
            "pfad1/Datei_12.tyb",
            "pfad1/Datei_13.tyc",
            "pfad3/Datei_33.tyc",
            "pfad3/Datei_34.tya"
        ],
        "DATEIEN_NUR_ZIEL": [
            "Datei_01.tye",
            "pfad3/Datei_33.tya",
            "pfad3/Datei_35.tyb",
            "pfad4/Datei_41.tya",
            "pfad4/Datei_42.tyb",
            "pfad4/Datei_43.tyc",
            "pfad4/Datei_44.tyd",
            "pfad5/Datei_51.tye",
            "pfad5/Datei_52.tye"
        ],
        "DATEIEN_GEMEINSAM": [
            "pfad2/Datei_21.tya",
            "pfad2/Datei_22.tyb",
            "pfad3/Datei_31.tya",
            "pfad3/Datei_32.tyb"
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
            ".tyd",
            ".tye"
        ],
        "TYPEN_GEMEINSAM": [
            ".tya",
            ".tyb",
            ".tyc"
        ],
        "UNTERSCHIEDLICHE_INFO": {
            "pfad3/Datei_32.tyb": [
                "25.12.2021 15:40:00",
                128,
                "07.01.2022 20:42:00",
                129
            ]
        }
    }
    return(dc_diff)


if __name__ == '__main__':
    '''
    Beschreibung
    '''
    # Objekt-Name
    tx_objekt = "DateiStrukturNeu"
    # Methoden-Namen
    tx_m_init = "__init__()"
    tx_m_str = "__str__()"
    tx_m_clear = "m_clear()"
    tx_m_setdc = "m_set_dc(<dict>)"
    tx_m_getdc = "m_get_dc()"
    tx_m_analyze = "m_analyze()"
    # Attribut-Namen
    tx_dc_quelle = "dc_quelle"
    tx_dc_ziel = "dc_ziel"
    tx_dc_diff = "dc_diff"
    # Bildschirmausgabe
    print("TEST_VERGLEICH")
    print("--------------")
    print("Objekt:        {0}".format(tx_objekt))
    print("Methoden:      {0}, {1}, {2},".format(
        tx_m_init,
        tx_m_str,
        tx_m_clear
    ))
    print("               {0}, {1}, {2}".format(
        tx_m_getdc,
        tx_m_setdc,
        tx_m_analyze
    ))
    print("Attribute:     {0}, {1}, {2},".format(
        tx_dc_quelle,
        tx_dc_ziel,
        tx_dc_diff
    ))
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    '''
    OBJEKT erzeugen
    '''
    tx_test = "{0} erzeugen".format(tx_objekt)
    f_testtitel(tx_test)
    ob_vergl = Vergleich()
    '''
    Methode __STR__ testen
    '''
    tx_test = "{0}.__str__()".format(tx_objekt, tx_m_str)
    f_testtitel(tx_test)
    # Vorgabe
    tx_vorgabe = "Text .."
    # Resultat
    tx_resultat = ob_vergl.__str__()
    print(tx_resultat)
    # Test
    if tx_resultat:
        bl_test = True
    else:
        bs_test = False
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_vorgabe, tx_resultat)
    '''
    Methode SET WÖRTERBUCH testen
    '''
    tx_test = "{0}.{1})".format(tx_objekt, tx_m_setdc)
    f_testtitel(tx_test)
    # Vorgabe
    vl_vorgabe = None
    # Resultat
    dc_quelle, dc_ziel = f_get_strukt_neu()
    dc_diff = f_vergl_stukt_neu()
    dc_vergl = {
        "QUELLE": dc_quelle,
        "ZIEL": dc_ziel,
        "VERGLEICH": dc_diff
    }
    vl_resultat = ob_vergl.m_set_dc(dc_vergl)
    # Test
    bl_test = vl_resultat == vl_vorgabe
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            vl_vorgabe, vl_resultat)
    '''
    Methode GET WÖRTERBUCH testen
    '''
    tx_test = "{0}.{1}".format(tx_objekt, tx_m_getdc)
    f_testtitel(tx_test)
    # Vorgabe
    dc_vorgabe = dc_vergl
    # Resultat
    dc_resultat = ob_vergl.m_get_dc()
    # Test
    bl_test = dc_vorgabe == dc_resultat
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            dc_vorgabe, dc_resultat)
    '''
    Methode CLEAR testen
    '''
    tx_test = "{0}.{1}".format(tx_objekt, tx_m_clear)
    f_testtitel(tx_test)
    # Vorgabe
    vl_vorgabe = None
    # Resultat
    vl_resultat = ob_vergl.m_clear()
    # Test
    bl_test = vl_resultat == vl_vorgabe
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            vl_vorgabe, vl_resultat)
    '''
    Attribut QUELLE testen
    '''
    tx_test = "{0}.{1}".format(tx_objekt, tx_dc_quelle)
    f_testtitel(tx_test)
    # Vorgabe
    dc_vorgabe = dc_quelle
    # Resultat
    ob_vergl.dc_quelle = dc_vorgabe
    dc_resultat = ob_vergl.dc_quelle
    # Test
    bl_test = dc_resultat == dc_vorgabe
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            dc_vorgabe, dc_resultat)
    '''
    Atribut ZIEL testen
    '''
    tx_test = "{0}.{1}".format(tx_objekt, tx_dc_ziel)
    f_testtitel(tx_test)
    # Vorgabe
    dc_vorgabe = dc_ziel
    # Resultat
    ob_vergl.dc_ziel = dc_vorgabe
    dc_resultat = ob_vergl.dc_ziel
    # Test
    bl_test = dc_resultat == dc_vorgabe
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            dc_vorgabe, dc_resultat)
    '''
    Attribut UNTERSCHIEDE testen
    '''
    tx_test = "{0}.{1}".format(tx_objekt, tx_dc_diff)
    f_testtitel(tx_test)
    # Vorgabe
    dc_vorgabe = dc_diff
    # Resultat
    ob_vergl.dc_diff = dc_vorgabe
    dc_resultat = ob_vergl.dc_diff
    # Test
    bl_test = dc_resultat == dc_vorgabe
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            dc_vorgabe, dc_resultat)
    '''
    Methode ANALIZE testen
    '''
    tx_test = "{0}.{1}".format(tx_objekt, tx_m_analyze)
    f_testtitel(tx_test)
    # Vorgabe
    dc_vorgabe = dc_diff
    # Resultat
    ob_vergl.dc_quelle = dc_quelle
    ob_vergl.dc_ziel = dc_ziel
    ob_vergl.m_analize()
    dc_resultat = ob_vergl.dc_diff
    # Test
    bl_test = dc_resultat == dc_vorgabe
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            dc_vorgabe, dc_resultat)
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
