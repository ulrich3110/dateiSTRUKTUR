#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import time

'''
dx_struktur.py - [d]atei[s]struktur
Copyright (c) Oktober 2021: Andreas Ulrich
<http://erasand.ch>, <andreas@erasand.ch>

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
    ''' Datei-Struktur Inhalt '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "DateiStruktur"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        print("# {0}.__str__ #".format(self.tx_objname))
        dc_info = self.m_get_dc(False)
        tx_info = json.dumps(dc_info, indent=2)
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "DATEILISTE": [],
            "VERZEICHNISLISTE": [],
            "STAMMPFAD": '',
            "DATUM": None,
            "VERZEICHNISANZAHL": 0,
            "DATEIANZAHL": 0,
            "TYPANZAHL": 0,
            "VERZEICHNISSE": []
        }
        self.m_set_dc(dc_clear, True)

    def m_get_dc(self, bl_objekte):
        '''
        Dateistruktur in einem Verzeichnis zurückgeben
        bl_objekte = True:  Objekte zurückgeben
                   = False: Als Verzeichnisse zurückgeben
        '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "DATEILISTE": self.ls_dateien,
            "VERZEICHNISLISTE": self.ls_verzeich,
            "STAMMPFAD": self.tx_stammpfad,
            "DATUM": self.ob_datetime,
            "VERZEICHNISANZAHL": self.in_anzverz,
            "DATEIANZAHL": self.in_anzdat,
            "TYPANZAHL": self.in_anztyp,
        }
        if bl_objekte:
            # Mit Objekten
            dc_daten["VERZEICHNISSE"] = self.ls_verz
        else:
            # Mit Werten in einem Verzeichnis
            dc_daten["VERZEICHNISSE"] = []
            for ob_verz in self.ls_verz:
                dc_daten["VERZEICHNISSE"].append(
                    ob_verz.m_get_dc(False)
                )
        return(dc_daten)

    def m_set_dc(self, dc_daten, bl_objekte):
        '''
        Dateistruktur aus einem Verzeichnis hinzufügen
        bl_objekte = True:  Aus Objekten
                   = False: Aus Verzeichnissen
        '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.ls_dateien = dc_daten["DATEILISTE"]
        self.ls_verzeich = dc_daten["VERZEICHNISLISTE"]
        self.tx_stammpfad = dc_daten["STAMMPFAD"]
        self.ob_datetime = dc_daten["DATUM"]
        self.in_anzverz = dc_daten["VERZEICHNISANZAHL"]
        self.in_anzdat = dc_daten["DATEIANZAHL"]
        self.in_anztyp = dc_daten["TYPANZAHL"]
        if bl_objekte:
            # Verzeichnis Objekte
            self.ls_verz = dc_daten["VERZEICHNISSE"]
        else:
            # Stattdessen Werte aus Verzeichnissen
            self.ls_verz = []
            for dc_verz in dc_daten["VERZEICHNISSE"]:
                ob_verz = Verzeichnis()
                ob_verz.m_set_dc(dc_verz, False)
                self.ls_verz.append(ob_verz)

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
                self.ls_dateien.append(
                    os.path.join(tx_root, tx_name)
                )
            for tx_name in ob_dirs:
                self.ls_verzeich.append(os.path.join(
                    tx_root, tx_name)
                )
        # Datum speichern
        self.ob_datetime = time.localtime()

    def m_ordnen(self):
        ''' Ordnet die Struktur von .m_lesen() '''
        print("# {0}.m_ordnen #".format(self.tx_objname))
        # Ordnungs Dictionairy
        dc_ord = {}
        # Root Verzeichnis erzeugen
        ob_verz = Verzeichnis()
        ob_verz.tx_pfad = self.tx_stammpfad
        self.ls_verz = [ob_verz]
        # Dem Ordnungsdictionairy hinzufügen
        dc_ord[ob_verz.tx_pfad] = ob_verz
        # Andere Verzeichnis erzeugen
        for tx_i in self.ls_verzeich:
            # Verzeichnis erzeugen, Pfad eintragen, in Liste speichern
            ob_verz = Verzeichnis()
            ob_verz.tx_pfad = tx_i
            self.ls_verz.append(ob_verz)
            # Dem Ordnungsdictionairy hinzufügen
            dc_ord[ob_verz.tx_pfad] = ob_verz
        # Verzichnisse einordnen
        for tx_i in self.ls_verzeich:
            if tx_i != self.tx_stammpfad:
                # Nach übergeordnetem Verzeichnis suchen
                tx_diri = os.path.dirname(tx_i)
                ob_verz = dc_ord[tx_diri]
                # Dem Verzeichnis als Unerverzeichnis hinzufügen
                tx_basei = os.path.basename(tx_i)
                ob_verz.ls_verz.append(tx_basei)
        for tx_i in self.ls_dateien:
            # DateiInfo erzeugen
            ob_dat = DateiInfo()
            # Dateipfad, Dateiname.Typ
            tx_diri = os.path.dirname(tx_i)
            tx_basei = os.path.basename(tx_i)
            # Dateiname und Typ
            ls_basei = os.path.splitext(tx_basei)
            ob_dat.tx_name = ls_basei[0]
            ob_dat.tx_typ = ls_basei[1]
            # Datum und Grösse lesen
            ob_dat.ob_datetime = time.localtime(os.path.getmtime(tx_i))
            ob_dat.in_groesse = os.path.getsize(tx_i)
            # Nach Verzeichnis suchen
            ob_verz = dc_ord[tx_diri]
            # Dem Verzeichnis als Datei hinzufügen
            ob_verz.ls_dat.append(ob_dat)

    def m_total(self):
        ''' Zusammenfassung erstellen '''
        print("# {0}.m_total #".format(self.tx_objname))
        # Anzahl Verzeichnisse und Dateien
        self.in_anzverz = len(self.ls_verzeich) + 1
        self.in_anzdat = len(self.ls_dateien)
        # Anzahl Dateitypen
        mn_typtot = set()
        # Pro Verzeichnis
        for ob_verz in self.ls_verz:
            # Anzahl Verzeichnisse und Dateien
            ob_verz.in_anzverz = len(ob_verz.ls_verz)
            ob_verz.in_anzdat = len(ob_verz.ls_dat)
            # Anzahl Dateitypen
            mn_typ = set()
            for ob_dat in ob_verz.ls_dat:
                mn_typtot.add(ob_dat.tx_typ)
                mn_typ.add(ob_dat.tx_typ)
            ob_verz.in_anztyp = len(mn_typ)
        # Total Anzahl Dateitypen
        self.in_anztyp = len(mn_typtot)


class Verzeichnis():
    ''' Verzeichnis Inhalt '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "Verzeichnis"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        print("# {0}.__str__ #".format(self.tx_objname))
        dc_info = self.m_get_dc(False)
        tx_info = json.dumps(dc_info, indent=2)
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "PFAD": '',
            "VERZEICHNISANZAHL": 0,
            "VERZEICHNISLISTE": [],
            "DATEIANZAHL": 0,
            "TYPANZAHL": 0,
            "DATEILISTE": []
        }
        self.m_set_dc(dc_clear, True)

    def m_get_dc(self, bl_objekte):
        '''
        Verzeichnis in einem Dictionairy zurückgeben
        bl_objekte = True:  Als Objekte zurückgeben
                   = False: Als Verzeichnisse zurückgeben
        '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "PFAD": self.tx_pfad,
            "VERZEICHNISANZAHL": self.in_anzverz,
            "VERZEICHNISLISTE": self.ls_verz,
            "DATEIANZAHL": self.in_anzdat,
            "TYPANZAHL": self.in_anztyp
        }
        if bl_objekte:
            # Mit Objekten
            dc_daten["DATEILISTE"] = self.ls_dat
        else:
            # Mit Werten in einem Verzeichnis
            dc_daten["DATEILISTE"] = []
            for ob_dat in self.ls_dat:
                dc_daten["DATEILISTE"].append(ob_dat.m_get_dc())
        return(dc_daten)

    def m_set_dc(self, dc_daten, bl_objekte):
        '''
        Verzeichnis aus einem Dictionariy hinzufügen
        bl_objekte = True:  Aus Objekten
                   = False: Aus Verzeichnissen
        '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_pfad = dc_daten["PFAD"]
        self.in_anzverz = dc_daten["VERZEICHNISANZAHL"]
        self.ls_verz = dc_daten["VERZEICHNISLISTE"]
        self.in_anzdat = dc_daten["DATEIANZAHL"]
        self.in_anztyp = dc_daten["TYPANZAHL"]
        if bl_objekte:
            # DateiInfo Objekte
            self.ls_dat = dc_daten["DATEILISTE"]
        else:
            # Stattdessen Werte aus Verzeichnissen
            self.ls_dat = []
            for dc_dat in dc_daten["DATEILISTE"]:
                ob_dat = DateiInfo()
                ob_dat.m_set_dc(dc_dat)
                self.ls_dat.append(ob_dat)


class DateiInfo():
    ''' Datei Informationen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "DateiInfo"
        print("# {0}.__init__ #".format(self.tx_objname))
        self.m_clear()

    def __str__(self):
        ''' Informationen als Text zurückgeben '''
        print("# {0}.__str__ #".format(self.tx_objname))
        dc_info = self.m_get_dc()
        tx_info = json.dumps(dc_info, indent=2)
        return(tx_info)

    def m_clear(self):
        ''' Zurücksetzen '''
        print("# {0}.m_clear #".format(self.tx_objname))
        dc_clear = {
            "NAME": '',
            "TYP": '',
            "DATUM": None,
            "GROESSE": 0
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Dateiinfo in einem Verzeichnis zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "NAME": self.tx_name,
            "TYP": self.tx_typ,
            "DATUM": self.ob_datetime,
            "GROESSE": self.in_groesse
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Dateiinfo aus einem Verzeichnis hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_name = dc_daten["NAME"]
        self.tx_typ = dc_daten["TYP"]
        self.ob_datetime = dc_daten["DATUM"]
        self.in_groesse = dc_daten["GROESSE"]


if __name__ == '__main__':
    # 1. Schritt
    # Test DateiInfo
    print("\nDATEIINFO TEST")
    # Leeres DateiInfo Objekt
    ob_datinf = DateiInfo()
    print(ob_datinf)
    # Mit Werten
    dc_test = {
        "NAME": "Testdatei",
        "TYP": "TXT",
        "DATUM": time.localtime(),
        "GROESSE": 1234
    }
    ob_datinf.m_set_dc(dc_test)
    print(ob_datinf)
    # Test Verzeichnis
    print("\nVERZEICHNIS TEST")
    # Leeres Verzeichnis Objekt
    ob_verz = Verzeichnis()
    print(ob_verz)
    # Mit Werten und Objekten
    dc_test = {
        "PFAD": './',
        "VERZEICHNISANZAHL": 1,
        "VERZEICHNISLISTE": ['muster'],
        "DATEIANZAHL": 1,
        "TYPANZAHL": 1,
        "DATEILISTE": [ob_datinf]
    }
    ob_verz.m_set_dc(dc_test, True)
    print(ob_verz)
    # Nur mit JSON Werten
    dc_verz = ob_verz.m_get_dc(False)
    ob_verz2 = Verzeichnis()
    ob_verz2.m_set_dc(dc_verz, False)
    print(ob_verz2)
    # Test DateiStruktur
    print("\nDATEISTRUKTUR TEST")
    # Leeres DateiStruktur Objekt
    ob_ds = DateiStruktur()
    print(ob_ds)
    # Mit Werten und Objekten
    dc_test = {
        "DATEILISTE": [],
        "VERZEICHNISLISTE": [],
        "STAMMPFAD": '',
        "DATUM": None,
        "VERZEICHNISANZAHL": 2,
        "DATEIANZAHL": 2,
        "TYPANZAHL": 1,
        "VERZEICHNISSE": [ob_verz, ob_verz2]
    }
    ob_ds.m_set_dc(dc_test, True)
    print(ob_ds)
    # Nur mit JSON Werten
    dc_ds = ob_ds.m_get_dc(False)
    ob_ds2 = DateiStruktur()
    ob_ds2.m_set_dc(dc_ds, False)
    print(ob_ds2)
    # DateiStruktur lesen testen
    ob_ds3 = DateiStruktur()
    ob_ds3.tx_stammpfad = ".."
    ob_ds3.m_lesen()
    ob_ds3.m_ordnen()
    ob_ds3.m_total()
    print(ob_ds3)

    '''
    STRUKTUR ERFASSEN
    - Struktur erfassen wie bei pyOsTools
    - Datum und Grösse der Dateien erfassen
    - Dateistruktur ordnen
        - Stammverzeichnis
            - Pfad absolut
            - Anzahl Verzeichnisse
            - Anzahl Dateien
            - Anzahl Dateitypen
        - Unterverzeichnisse
            - Pfad relativ
            - Pfad absolut
            - Anzahl Verzeichnisse
            - Liste mit Verzeichnisnamen
            - Anzahl Dateien
            - Anzahl Dateitypen
            - Dateien als Verzeichnis
              {Dateityp: Dateinamen, Dateidatum, Dateigrösse}
    - Alles zusammen als JSON speichern in einem lesbaren Format
    - Kontrolle der gespeicherten JSON
    - JSON = {
        "STAMMPFAD": 'absoluter Pfad',
        "VERZEICHNISANZAHL": zahl,
        "DATEIANZAHL": zahl,
        "TYPANZAHL": zahl,
        "VERZEICHNISSE": [
            {
                "PFAD": 'relativer pfad zum absolutem Stammpfad'
                "DATUM": Python.time()
                "VERZEICHNISANZAHL": zahl,
                "VERZEICHNISLISTE": ['Verzeichnisname', ],
                "DATEIANZAHL": zahl,
                "TYPANZAHL": zahl,
                "DATEILISTE": [
                    {
                        "NAME": 'dateiname',
                        "TYP": 'erw',
                        "DATUM": Python.time()
                        "GROESSE": zahl
                    },
                ]
            }
        ]
    }
    '''
    # 2. Schritt
    '''
    STRUKTUR IN TEXTFORM UND ALS TABELLE SPEICHERN
    - JSON laden
    - HTML generieren für Textdarstellung
    - CSV generieren für Tabellendarstellung
    '''
    # Darstellung
    '''
    DARSTELLUNG DATEISTRUKTUR
Zusammenfassung Struktur {Pfad absolut}
---------------------------------------
Anzahl Verzeichnisse: {x}
Anzahl Dateien: {x}
Anzahl Dateitypen: {x}


Verzeichnis {Pfad relativ}
--------------------------
Anzahl Verzeichnisse: {x}
- {Verzeichnisnamen}
Anzahl Dateien: {x}
Anzahl Dateitypen: {x}
Dateityp {x}
- {Dateiname}, {Änderungsdatum}, {Grösse}
{Weitere Auflistung nach Dateityp und Name sortiert}
    '''
    # 3. Schritt
    '''
    STRUKTUR VERGLEICHEN
    - Quellstruktur aus JSON laden
    - Zielstruktur aus JSON laden
    - Zusammenfassung vergleichen
        - Anzahl Dateien
            - Quelle als Zahl
            - Ziel als Zahl
            - Differenz Ziel zu Quelle als Zahl
        - Anzahl Verzeichnisse
            - Quelle als Zahl
            - Ziel als Zahl
            - Differenz Ziel zu Quelle als Zahl
        - Anzahl Dateitypen
            - Quelle als Zahl
            - Ziel als Zahl
            - Differenz Ziel zu Quelle als Zahl
    - Verzeichnisse vergleichen
        - Anzahl Verzeichnisse
            - Quelle als Zahl
            - Ziel als Zahl
            - Differenz Ziel zu Quelle als Zahl
        - Verzeichnislisten
            - Unterschiede Verzeichnisse als Verzeichnis
                                  Ziel  Quelle
              {Verzeichnisnamen: (True, True)}
        - Anzahl Dateien
            - Quelle als Zahl
            - Ziel als Zahl
            - Differenz Ziel zu Quelle als Zahl
        - Anzahl Dateitypen
            - Quelle als Zahl
            - Ziel als Zahl
            - Differenz Ziel zu Quelle als Zahl
        - Dateien
            - Unterschiede Dateien als Verzeichnis
              {Dateityp: Dateinamen, Dateidatum, "neuer/älter",
                                     Dateigrösse, "grösser/kleiner"}
    - Alles zusammen als JSON speichern in einem lesbaren Format
    - Kontrolle der gespeicherten JSON
    '''
    # 4. Schritt
    '''
    - HTML generieren für Textdarstellung
    - CSV generieren für Tabellendarstellung
    '''
    # Darstellung
    '''
    DARSTELLUNG VERGLEICH
< 32                           >  < 10     >  < 10     >  < 12       >
Zusammenfassung
---------------
Quelle: {absoluter Pfad}
Ziel:   {absoluter Pfad}
                                  Quelle      Ziel        Unterschiede
Struktur                          {absolut}   {absolut}
Verzeichnisse                     {x}         {x}         +{x} / -{x}
Dateien                           {x}         {x}         +{x} / -{x}
Dateitypen                        {x}         {x}         +{x} / -{x}

Verzeichnis {Pfad relativ}
--------------------------
Quelle: {absoluter Pfad}
Ziel:   {absoluter Pfad}
                                  Quelle      Ziel        Unterschiede
Verzeichnisse                     {x}         {x}         +{x} / -{x}
- {Unterschied Verze.}            ja / nein    ja / nein
Anzahl Dateien                    {x}         {x}         +{x} / -{x}
Anzahl Dateitypen                 {x}         {x}         +{x} / -{x}
Dateityp {x}
- {Unterschied Datei}             ja / nein   ja / nein
  {tt.mm.jjjj hh:mm}                          älter / neuer
  {Grösse}                                    kleiner / grösser
{Weitere Auflistung nach Dateityp und Name sortiert}
    '''
    # 5. Schritt GUI Entwicklung
    '''
    Tkinter
    Entwicklungsschritte 1 - 4 als Grundlage
    Funktionen und Objekte übernehemen
    ---
    Strukturerstellung
    Pfadeingabe für Erfassung (Dateidialog Verzeichnis)
    JSON speichern (Dateidialog Speichern)
    ---
    Dokumente erstellen
    JSON öffnen (Dateidialog öffnen)
    HTML speichern (Dateidialog Speichern)
    CSV speichern (Dateidialog Speichern)
    ---
    Strukturen vergleichen
    Quellstruktur JSON öffnen (Dateidialog öffnen)
    Zielstruktur JSON öffnen (Dateidialog öffnen)
    Unterschiede ermitteln
    Unterschiede anzeigen
    Unterschiede als HTML speichern (Dateidialog Speichern)
    Unterschiede als CSV speichern (Dateidialog Speichern)
    '''
    # 6. Schritt Web Entwicklung
    '''
    Django
    Entwicklungsschritte 1 - 4 als Grundlage
    Funktionen und Objekte übernehemen
    ---
    Strukturen lokal als JSON erstellen
    ---
    Seite Struktur anzeigen
    Struktur als JSON hochladen
    Anzeige als HTML Text / Tabelle
    ---
    Seite Strukturen vergleichen
    Quellstruktur als JSON hochladen
    Zielstruktur als JSON hochladen
    Unterschiede als HTML Text / Tabelle
    '''
    # Fertig
