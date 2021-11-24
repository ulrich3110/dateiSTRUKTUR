#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import datetime
import json
import os
import time

'''
dx_htmlcsv.py - [d]atei[s]strukturen als HTML und CSV speichern
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


def f_loadjson(tx_pfad):
    '''
    Lädt eine JSON Datei und gibt diese zurück als Wörterbuch
    - tx_pfad = Pfad
    - dc_verz = Wörterbuch
    '''
    print("# f_loadjson #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # Json laden
    try:
        with open(tx_pfad) as ob_f:
            dc_verz = json.load(ob_f)
    except Exception as ob_err:
        # Fehlermeldung ausgeben und leeres Wörterbuch erzeugen
        tx_t = "FEHLER -- PFAD: {0} -- ERROR: {1}".format(
            tx_pfad,
            str(ob_err)
        )
        print(tx_t)
        dc_verz = {}
    return(dc_verz)


def f_savejson(tx_pfad, dc_verz):
    '''
    Speichert ein Wörterbuch als JSON Datei unter dem Pfad ab.
    - tx_pfad = Pfad
    - dc_verz = Wörterbuch
    '''
    print("# f_savejson #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # JSON speichern
    try:
        with open(tx_pfad, 'w', encoding='utf-8',
                  errors='ignore') as ob_jsonfile:
            json.dump(dc_verz, ob_jsonfile, indent=2, sort_keys=True)
    except Exception as ob_err:
        # Fehlermeldung ausgeben
        tx_t = "FEHLER -- PFAD: {0} -- ERROR: {1}".format(
            tx_pfad,
            str(ob_err)
        )
        print(tx_t)
    return()


def f_savetext(tx_pfad, tx_text):
    '''
    Speichert einen Text unter dem Pfad ab.
    - tx_pfad = Pfad
    - tx_text = Text
    '''
    print("# f_savetext #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # Text speichern
    try:
        ob_datei = open(
            tx_pfad,
            'w',
            encoding='utf-8',
            errors='ignore'
        )
        ob_datei.write(tx_text)
        ob_datei.close()
    except Exception as ob_err:
        tx_t = "# FEHLER ## PFAD: {0} ## Error: {1} #".format(
            tx_pfad,
            str(ob_err)
        )
        tx_errpfad = "{0}___error.txt".format(tx_pfad)
        ob_errfile = open(tx_errpfad, 'w')
        ob_errfile.write(tx_t)
        ob_errfile.close()


def f_savecsv(tx_pfad, ls_tabelle):
    '''
    Speichert einen Liste als CSV unter dem Pfad ab.
    - tx_pfad = Pfad
    - ls_tabelle = Liste in Tabellenform:
      [
        ["Spaltentitel 1", "Spaltentitel 2"],
        [Wert Spale 1,     Wert Spalte 2],
      ]
    '''
    print("# f_savecsv #")
    # Pfad normalisieren
    tx_pfad = os.path.normcase(os.path.normpath(tx_pfad))
    # CSV speichern
    ob_datei = open(tx_pfad, 'w')
    with ob_datei:
        ob_writer = csv.writer(ob_datei)
        for ls_zeile in ls_tabelle:
            ob_writer.writerow(ls_zeile)


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
            "DATUM": '',
            "VERZEICHNISANZAHL": 0,
            "DATEIANZAHL": 0,
            "TYPANZAHL": 0,
            "VERZEICHNISSE": []
        }
        self.m_set_dc(dc_clear, True)

    def m_get_dc(self, bl_objekte):
        '''
        Dateistruktur in einem Wörterbuch zurückgeben
        bl_objekte = True:  Objekte zurückgeben
                   = False: Als Wörterbücher zurückgeben
        '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "DATEILISTE": self.ls_dateien,
            "VERZEICHNISLISTE": self.ls_verzeich,
            "STAMMPFAD": self.tx_stammpfad,
            "DATUM": self.tx_datum,
            "VERZEICHNISANZAHL": self.in_anzverz,
            "DATEIANZAHL": self.in_anzdat,
            "TYPANZAHL": self.in_anztyp,
        }
        if bl_objekte:
            # Mit Objekten
            dc_daten["VERZEICHNISSE"] = self.ls_verz
        else:
            # Mit Werten in einem Wörterbuch
            dc_daten["VERZEICHNISSE"] = []
            for ob_verz in self.ls_verz:
                dc_daten["VERZEICHNISSE"].append(
                    ob_verz.m_get_dc(False)
                )
        return(dc_daten)

    def m_set_dc(self, dc_daten, bl_objekte):
        '''
        Dateistruktur aus einem Wörterbuch hinzufügen
        bl_objekte = True:  Aus Objekten
                   = False: Aus Wörterbüchern
        '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.ls_dateien = dc_daten["DATEILISTE"]
        self.ls_verzeich = dc_daten["VERZEICHNISLISTE"]
        self.tx_stammpfad = dc_daten["STAMMPFAD"]
        self.tx_datum = dc_daten["DATUM"]
        self.in_anzverz = dc_daten["VERZEICHNISANZAHL"]
        self.in_anzdat = dc_daten["DATEIANZAHL"]
        self.in_anztyp = dc_daten["TYPANZAHL"]
        if bl_objekte:
            # Verzeichnis Objekte
            self.ls_verz = dc_daten["VERZEICHNISSE"]
        else:
            # Stattdessen Werte aus Wörterrbücher
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
        ob_now = datetime.datetime.today()
        self.tx_datum = ob_now.strftime('%d.%m.%Y %H:%M:%S')

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
            if os.path.isfile(tx_i):
                ob_datum = os.path.getmtime(tx_i)
                ob_dat.tx_datum = time.strftime(
                    '%d.%m.%Y %H:%M:%S',
                    time.localtime(ob_datum)
                )
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
        Verzeichnis in einem Wörterbuch zurückgeben
        bl_objekte = True:  Als Objekte zurückgeben
                   = False: Als Wörterbücher zurückgeben
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
            # Mit Werten in einem Wörterbuch
            dc_daten["DATEILISTE"] = []
            for ob_dat in self.ls_dat:
                dc_daten["DATEILISTE"].append(ob_dat.m_get_dc())
        return(dc_daten)

    def m_set_dc(self, dc_daten, bl_objekte):
        '''
        Verzeichnis aus einem Wörterbuch hinzufügen
        bl_objekte = True:  Aus Objekten
                   = False: Aus Wörterbüchern
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
            # Stattdessen Werte aus Wörterbücher
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
            "DATUM": '',
            "GROESSE": 0
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Dateiinfo in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "NAME": self.tx_name,
            "TYP": self.tx_typ,
            "DATUM": self.tx_datum,
            "GROESSE": self.in_groesse
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Dateiinfo aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_name = dc_daten["NAME"]
        self.tx_typ = dc_daten["TYP"]
        self.tx_datum = dc_daten["DATUM"]
        self.in_groesse = dc_daten["GROESSE"]


class HtmlStruktur():
    ''' Aus einem Datei-Stuktur JSON ein HTML Dokument erstellen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "HtmlStruktur"
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
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "JSONPFAD": '',
            "HTMLPFAD": '',
            "TITEL": '',
            "TEXT": '',
            "AUSGABELISTE": [],
            "HTML": ''
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Verzeichnis in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "JSONPFAD": self.tx_jsonpfad,
            "HTMLPFAD": self.tx_htmlpfad,
            "TITEL": self.tx_titel,
            "TEXT": self.tx_text,
            "AUSGABELISTE": self.ls_ausgabe,
            "HTML": self.tx_html
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Verzeichnis aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_jsonpfad = dc_daten["JSONPFAD"]
        self.tx_htmlpfad = dc_daten["HTMLPFAD"]
        self.tx_titel = dc_daten["TITEL"]
        self.tx_text = dc_daten["TEXT"]
        self.ls_ausgabe = dc_daten["AUSGABELISTE"]
        self.tx_html = dc_daten["HTML"]

    def m_create(self):
        ''' Anhand eines Datei-Struktur JSON ein HTML erstellen '''
        print("# {0}.m_create #".format(self.tx_objname))
        # Json laden
        dc_json = f_loadjson(self.tx_jsonpfad)
        # Ausgabestruktur erstellen
        ob_ausgabe = StrukturAusgabe()
        ob_ausgabe.dc_struktur = dc_json
        ob_ausgabe.m_ausgabeliste()
        # Ausgabeliste übernehmen
        self.ls_ausgabe = ob_ausgabe.ls_ausgabe
        # Anfang
        self.m_anfang()
        # Zusammenfassung
        self.m_struktur()
        # Verzeichnisse
        self.m_verzeichnisse()
        # Ende
        self.m_ende()
        # HTML schreiben
        self.m_save()

    def m_anfang(self):
        ''' HTML Datei-Struktur Anfang '''
        print("# {0}.m_anfang #".format(self.tx_objname))
        # Head, Body, Titel, Text
        self.tx_html = "".join([
            '<!DOCTYPE html><html>',
            '<head>',
            '<style>table, th, td ',
            '{padding: 3px; ',
            'border: 1px solid black; '
            'border-collapse: collapse;}',
            '#left {text-align: left;}',
            '#right {text-align: right;}',
            '</style></head>',
            '<body>',
            "<h1>", self.tx_titel, "<br>",
            "<small>", self.tx_text, "</small></h1><br>"
        ])

    def m_ende(self):
        ''' HTML Datei-Struktur Ende '''
        print("# {0}.m_ende #".format(self.tx_objname))
        # Body end
        self.tx_html = "".join([self.tx_html, '</body></html>'])

    def m_save(self):
        ''' HTML Datei-Struktur speichern '''
        print("# {0}.m_save #".format(self.tx_objname))
        # HTML speichern
        f_savetext(self.tx_htmlpfad, self.tx_html)

    def m_struktur(self):
        ''' HTML Datei-Struktur Zusammenfassung '''
        print("# {0}.m_struktur #".format(self.tx_objname))
        # Zusammenfassung: Pfad, Datum, Anzahl Verzeichnisse,
        # Anzahl Dateien, Anzahl Dateitypen
        self.tx_html = "".join([
            self.tx_html,
            '<h2>Zusammenfassung: ', self.ls_ausgabe[0],
            '</h2>',
            '<p>Datum / Uhrzeit: ', self.ls_ausgabe[1],
            '</p>',
            '<p>Anzahl Verzeichnisse: ', self.ls_ausgabe[2],
            '</p>',
            '<p>Anzahl Dateien: ', self.ls_ausgabe[3],
            '</p>',
            '<p>Anzahl Dateitypen: ', self.ls_ausgabe[4],
            '</p>'
        ])

    def m_verzeichnisse(self):
        ''' HTML Datei-Struktur Verzeichnis '''
        print("# {0}.m_verzeichnisse #".format(self.tx_objname))
        # Verzeichnisliste durchlaufen
        for ls_ver in self.ls_ausgabe[5]:
            # Verzeichnis: Pfad, Anzahl Verzeichnisse
            if ls_ver[0] == ".":
                # Stammverzeichnis
                tx_verpfad = '<i>Hauptverzeichnis</i>'
            else:
                # Ein Unterverzeichnis
                tx_verpfad = ls_ver[0]
            self.tx_html = "".join([
                self.tx_html,
                '<h2>Verzeichnis: ', tx_verpfad,
                '</h2>',
                '<p>Anzahl Verzeichnisse: ', str(ls_ver[1]),
                '</p>'
            ])
            # Prüfen ob Subverzeichnisse vorhanden sind
            if ls_ver[2]:
                # Mit Verzeichnisliste Tabelle beginnen
                self.tx_html = "".join([
                    self.tx_html,
                    '<table><tr>',
                    '<th id="left">Verzeichnisname</th>',
                    '</tr>'
                ])
                # Verzeichnisliste durchlaufen
                for tx_verz in ls_ver[2]:
                    # Verzeichnisnamen
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td id="left">', tx_verz, '</td>',
                        '</tr>'
                    ])
                # Tabellen Ende Verzeichnisliste
                self.tx_html = "".join([self.tx_html, "</table>"])
            # Anzahl Dateien, Anzahl Dateitypen
            self.tx_html = "".join([
                self.tx_html,
                '<p>Anzahl Dateien: ', ls_ver[3],
                '</p>',
                '<p>Anzahl Dateitypen: ', ls_ver[4],
                '</p>'
            ])
            # Prüfen ob Dateien vorhanden sind
            if ls_ver[5]:
                # Mit Dateilisten Tabelle beginnen
                self.tx_html = "".join([
                    self.tx_html,
                    '<table><tr>',
                    '<th id="left">Dateiname</th>',
                    '<th id="left">Dateityp</th>',
                    '<th id="left"><small>Datum/Uhrzeit</small></th>',
                    '<th id="right"><small>Groesse (bytes)</small></th>',
                    '</tr>'
                ])
                # Dateiliste durchlaufen
                for ls_dat in ls_ver[5]:
                    # Dateiname mit Informationen
                    self.tx_html = "".join([
                        self.tx_html,
                        '<tr>',
                        '<td id="left">', ls_dat[0], '</td>',
                        '<td id="left">', ls_dat[1], '</td>',
                        '<td id="left"><small>', ls_dat[2],
                        '</small></td>',
                        '<td id="right"><small>', ls_dat[3],
                        '</small></td>',
                        '</tr>'
                    ])
                # Tabellen Ende
                self.tx_html = "".join([self.tx_html, "</table>"])


class CsvStruktur():
    ''' Aus einem Datei-Stuktur JSON eine CSV Tabelle erstellen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "CsvStruktur"
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
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "JSONPFAD": '',
            "CSVPFAD": '',
            "TITEL": '',
            "TEXT": '',
            "AUSGABELISTE": [],
            "CSV": []
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' Verzeichnis in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "JSONPFAD": self.tx_jsonpfad,
            "CSVPFAD": self.tx_csvpfad,
            "TITEL": self.tx_titel,
            "TEXT": self.tx_text,
            "AUSGABELISTE": self.ls_ausgabe,
            "CSV": self.ls_csv
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' Verzeichnis aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.tx_jsonpfad = dc_daten["JSONPFAD"]
        self.tx_csvpfad = dc_daten["CSVPFAD"]
        self.tx_titel = dc_daten["TITEL"]
        self.tx_text = dc_daten["TEXT"]
        self.ls_ausgabe = dc_daten["AUSGABELISTE"]
        self.ls_csv = dc_daten["CSV"]

    def m_create(self):
        ''' Anhand eines Datei-Struktur JSON ein CSV erstellen '''
        print("# {0}.m_create #".format(self.tx_objname))
        # Json laden
        dc_json = f_loadjson(self.tx_jsonpfad)
        # Ausgabestruktur erstellen
        ob_ausgabe = StrukturAusgabe()
        ob_ausgabe.dc_struktur = dc_json
        ob_ausgabe.m_ausgabeliste()
        # Ausgabeliste übernehmen
        self.ls_ausgabe = ob_ausgabe.ls_ausgabe
        # Anfang
        self.m_titel()
        # Zusammenfassung
        self.m_struktur()
        # Verzeichnisse
        self.m_verzeichnisse()
        # CSV schreiben
        self.m_save()

    def m_titel(self):
        ''' CSV Datei-Struktur Titel '''
        print("# {0}.m_anfang #".format(self.tx_objname))
        # Spaltenüberschriften
        self.ls_csv = [[
            "Kategorie",
            "Anzahl",
            "Verzeichnisnamen",
            "Dateiname",
            "Dateityp",
            "Datum/Uhrzeit",
            "Groesse (bytes)"
        ]]
        # Titel und Text
        self.ls_csv.extend([
            [self.tx_titel, "", "", "", "", "", ""],
            [self.tx_text, "", "", "", "", "", ""]
        ])

    def m_save(self):
        ''' CSV Datei-Struktur speichern '''
        print("# {0}.m_save #".format(self.tx_objname))
        # CSV speichern
        f_savecsv(self.tx_csvpfad, self.ls_csv)

    def m_struktur(self):
        ''' CSV Datei-Struktur Zusammenfassung '''
        print("# {0}.m_struktur #".format(self.tx_objname))
        # Zusammenfassung: Pfad, Datum, Anzahl Verzeichnisse,
        # Anzahl Dateien, Anzahl Dateitypen
        self.ls_csv.extend([
            [
                "Zusammenfassung",
                "",
                self.ls_ausgabe[0],
                "",
                "",
                "",
                ""
            ],
            [
                "Datum / Uhrzeit",
                "",
                "",
                "",
                "",
                self.ls_ausgabe[1],
                ""
            ],
            [
                "Anzahl Verzeichnisse",
                self.ls_ausgabe[2],
                "",
                "",
                "",
                "",
                ""
            ],
            [
                "Anzahl Dateien",
                self.ls_ausgabe[3],
                "",
                "",
                "",
                "",
                ""
            ],
            [
                "Anzahl Dateitypen",
                self.ls_ausgabe[4],
                "",
                "",
                "",
                "",
                ""
            ],

        ])

    def m_verzeichnisse(self):
        ''' CSV Datei-Struktur Verzeichnis '''
        print("# {0}.m_verzeichnisse #".format(self.tx_objname))
        # Verzeichnisliste durchlaufen
        for ls_ver in self.ls_ausgabe[5]:
            # Verzeichnis: Pfad, Anzahl Verzeichnisse
            if ls_ver[0] == ".":
                # Stammverzeichnis
                tx_verpfad = "Hauptverzeichnis"
            else:
                # Ein Unterverzeichnis
                tx_verpfad = ls_ver[0]
            self.ls_csv.extend([
                [
                    "Verzeichnis",
                    "",
                    tx_verpfad,
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    "Anzahl Verzeichnisse",
                    ls_ver[1],
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            ])
            # Prüfen ob Subverzeichnisse vorhanden sind
            if ls_ver[2]:
                index = 1
                # Verzeichnisliste durchlaufen
                for tx_verz in ls_ver[2]:
                    self.ls_csv.extend([
                        [
                            "Verzeichnis #{0}".format(index),
                            "",
                            tx_verz,
                            "",
                            "",
                            "",
                            ""
                        ]
                    ])
                    index += 1
            # Anzahl Dateien, Anzahl Dateitypen
            self.ls_csv.extend([
                [
                    "Anzahl Dateien",
                    ls_ver[3],
                    "",
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    "Anzahl Dateitypen",
                    ls_ver[4],
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            ])
            # Prüfen ob Dateien vorhanden sind
            if ls_ver[5]:
                index = 1
                # Dateiliste durchlaufen
                for ls_dat in ls_ver[5]:
                    # Dateiname mit Informationen
                    self.ls_csv.extend([
                        [
                            "Datei #{0}".format(index),
                            "",
                            "",
                            ls_dat[0],
                            ls_dat[1],
                            ls_dat[2],
                            ls_dat[3]
                        ]
                    ])
                    index += 1


class StrukturAusgabe():
    ''' Aus einer Datei-Struktur eine Ausgabeliste erzeugen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "StrukturAusgabe"
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
        print("# {0}.clear #".format(self.tx_objname))
        dc_clear = {
            "DATEISTRUKTUR": {},
            "AUSGABELISTE": []
        }
        self.m_set_dc(dc_clear)

    def m_get_dc(self):
        ''' StrukturAusgabe in einem Wörterbuch zurückgeben '''
        print("# {0}.m_get_dc #".format(self.tx_objname))
        dc_daten = {
            "DATEISTRUKTUR": self.dc_struktur,
            "AUSGABELISTE": self.ls_ausgabe
        }
        return(dc_daten)

    def m_set_dc(self, dc_daten):
        ''' StrukturAusgabe aus einem Wörterbuch hinzufügen '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        self.dc_struktur = dc_daten["DATEISTRUKTUR"]
        self.ls_ausgabe = dc_daten["AUSGABELISTE"]

    def m_ausgabeliste(self):
        '''
        Ausgabeliste anhand der Datei-Struktur ersellen
        Ausgabeliste = [
            Stammpfad absolut,
            Datum / Zeit,
            Anzahl Verzeichnisse,
            Anzahl Dateien,
            Anzahl Dateitypen,
            [
                [
                    Verzeichnispfad relativ,
                    Anzahl Verzeichnisse,
                    [Verzeichnisnamen, ],
                    Anzahl Dateien,
                    Anzahl Dateitypen,
                    [[Name, Typ, Datum, Groesse], ..],
                ],
                ..
            ]
        ]
        '''
        print("# {0}.m_set_dc #".format(self.tx_objname))
        # Ausgabeliste initieren
        self.ls_ausgabe = []
        # Zusammenfassung der Struktur
        self.m_struktur()
        # Verzeichnisse
        self.m_verzeichnis()

    def m_struktur(self):
        ''' Struktur Zusammenfassung als Liste erstellen '''
        print("# {0}.m_struktur #".format(self.tx_objname))
        # Zusammenfassung: Pfad, Datum, Anzahl Verzeichnisse,
        # Anzahl Dateien, Anzahl Dateitypen
        ls_i = [
            self.dc_struktur['STAMMPFAD'],
            self.dc_struktur['DATUM'],
            str(self.dc_struktur['VERZEICHNISANZAHL']),
            str(self.dc_struktur['DATEIANZAHL']),
            str(self.dc_struktur['TYPANZAHL'])
        ]
        for i in ls_i:
            self.ls_ausgabe.append(i)

    def m_verzeichnis(self):
        ''' Verzeichnis als Liste erstellen '''
        print("# {0}.m_verzeichnis #".format(self.tx_objname))
        # Verzeichnisse als Liste
        ls_verz = self.dc_struktur["VERZEICHNISSE"]
        # Sortierte liste definieren
        ls_verzsort = []
        # Verzeichnisse durchlaufen
        for dc_verz in ls_verz:
            # Verzeichnisse auslesen und Liste bilden
            # ['pfad', x (anzahl verzeichnksse), [verzeichnisse, ],
            #  x (anzahl dateien), x (anzahl typen),
            #  [["typ", [dateien, ]]
            # Verzeichnisliste sortieren
            ls_subverz = dc_verz["VERZEICHNISLISTE"]
            ls_subverz.sort()
            # Dateiliste erzeugen und sortieren
            ls_dat = self.m_dateiliste(dc_verz["DATEILISTE"])
            # Verzeichnispfad relativ zum Stammpfad setzen
            tx_relpath = os.path.relpath(
                dc_verz['PFAD'],
                start=self.dc_struktur['STAMMPFAD']
            )
            # Zur Verzeichnisliste hinzufügen
            ls_verzsort.append([
                tx_relpath,
                dc_verz['VERZEICHNISANZAHL'],
                ls_subverz,
                str(dc_verz['DATEIANZAHL']),
                str(dc_verz['TYPANZAHL']),
                ls_dat
            ])
        # Liste sortieren (Nach 1. Wert: Pfad)
        ls_verzsort.sort()
        # An Ausgabeliste anhängen
        self.ls_ausgabe.append(ls_verzsort)

    def m_dateiliste(self, ls_dateien):
        ''' Dateien nach Namen sortiert als Liste erstellen '''
        print("# {0}.m_dateiliste #".format(self.tx_objname))
        # Rückgabe Dateiliste initieren
        ls_rueckgabe = []
        # List mit Datei-Wörterbücher durchlaufen
        for dc_dat in ls_dateien:
            # Werte aus Wörterbuch auslesen
            tx_name = dc_dat["NAME"]
            tx_typ = dc_dat["TYP"]
            tx_datum = dc_dat["DATUM"]
            tx_groesse = str(dc_dat["GROESSE"])
            # Zur Liste hinzufügen
            ls_rueckgabe.append([
                tx_name,
                tx_typ,
                tx_datum,
                tx_groesse
            ])
        # Rückgabe sortieren (nach 1. Wert: Name) und zurückgeben
        ls_rueckgabe.sort()
        return(ls_rueckgabe)


class RunJson():
    ''' Befehle aus einer JSON Datei ausführen '''

    def __init__(self):
        ''' Initieren '''
        self.tx_objname = "RunJson"
        print("# {0}.__init__ #".format(self.tx_objname))

    def m_reset_befehle(self):
        print("# {0}.m_reset_befehle #".format(self.tx_objname))
        ''' Wörterbuch mit Befehlen zurücksetzen '''
        self.dc_befehle = {
            "TESTMODUS": False,
            "BEFEHLE": [
                (
                    "STRUKTUR ERFASSEN",
                    {
                        "ZIEL": ".",
                        "JSON": "./struktur.json"
                    }
                ),
                (
                    "ZU HTML",
                    {
                        "JSON": "./struktur.json",
                        "HTML": "./struktur.html",
                        "TITEL": "Struktur",
                        "TEXT": "Beispiel"
                    }
                ),
                (
                    "ZU CSV",
                    {
                        "JSON": "./struktur.json",
                        "CSV": "./struktur.csv",
                        "TITEL": "Struktur",
                        "TEXT": "Beispiel"
                    }
                )
            ]
        }

    def m_load(self):
        '''
        JSON Befehle laden
        '''
        print("# {0}.m_load #".format(self.tx_objname))
        # Json laden
        self.dc_befehle = f_loadjson("./ds_htmlcsv.json")
        if not self.dc_befehle:
            # Fehler beim Laden, Einstellungen erzeugen
            self.m_reset_befehle()
            # Einstellungen sichern
            f_savejson("./ds_htmlcsv.json", self.dc_befehle)

    def m_run(self):
        ''' JSON Aktionen ausführen '''
        print("# {0}.m_run #".format(self.tx_objname))
        # Befehlsliste holen
        ls_befehle = self.dc_befehle["BEFEHLE"]
        # Befehlsliste durchlaufen
        for tp_aktion in ls_befehle:
            # Aktion und Werte Wörterbuch
            tx_befehl = tp_aktion[0]
            dc_argumente = tp_aktion[1]
            # Aktionen wählen
            if tx_befehl == "STRUKTUR ERFASSEN":
                # Struktur erzeugen
                ob_ds = DateiStruktur()
                # Ziel Verzeichnis setzen
                ob_ds.tx_stammpfad = dc_argumente["ZIEL"]
                # Datei-Struktur lesen, ordnen und zusammenfassen
                ob_ds.m_lesen()
                ob_ds.m_ordnen()
                ob_ds.m_total()
                # Wörterbuch für JSON erzeugen
                dc_json = ob_ds.m_get_dc(False)
                # JSON speichern
                f_savejson(dc_argumente["JSON"], dc_json)
            elif tx_befehl == "ZU HTML":
                # Als HTML speichern
                ob_html = HtmlStruktur()
                ob_html.tx_jsonpfad = dc_argumente["JSON"]
                ob_html.tx_htmlpfad = dc_argumente["HTML"]
                ob_html.tx_titel = dc_argumente["TITEL"]
                ob_html.tx_text = dc_argumente["TEXT"]
                ob_html.m_create()
            elif tx_befehl == "ZU CSV":
                # Als CSV Tabelle speichern
                ob_csv = CsvStruktur()
                ob_csv.tx_jsonpfad = dc_argumente["JSON"]
                ob_csv.tx_csvpfad = dc_argumente["CSV"]
                ob_csv.tx_titel = dc_argumente["TITEL"]
                ob_csv.tx_text = dc_argumente["TEXT"]
                ob_csv.m_create()


if __name__ == '__main__':
    # RunJson Objekt und Befehle laden
    ob_rj = RunJson()
    ob_rj.m_load()
    # Testmodus prüfen
    if not ob_rj.dc_befehle["TESTMODUS"]:
        ob_rj.m_run()
    else:
        # Datei-Struktur erstellen
        print("\nDATEISTRUKTUR ERSTELLEN")
        # Struktur erzeugen
        ob_ds = DateiStruktur()
        # Ziel Verzeichnis setzen (Ohne / am Ende)
        ob_ds.tx_stammpfad = "/home/andreas/Dropbox/ICH/2_Projekte"
        # Datei-Struktur lesen, ordnen und zusammenfassen
        ob_ds.m_lesen()
        ob_ds.m_ordnen()
        ob_ds.m_total()
        # Wörterbuch für JSON erzeugen
        dc_json = ob_ds.m_get_dc(False)
        # JSON speichern
        f_savejson("./dc_htmlcsv_test.json", dc_json)
        # Datei-Struktur laden
        print("\nDATEISTRUKTUR LADEN")
        # Json laden und ausgeben
        dc_json = f_loadjson("./dc_htmlcsv_test.json")
        print(dc_json)
        # Ausgabestruktur erstellen
        print("\nAUSGABESTRUKTUR")
        ob_ausgabe = StrukturAusgabe()
        ob_ausgabe.dc_struktur = dc_json
        ob_ausgabe.m_ausgabeliste()
        print(ob_ausgabe.ls_ausgabe)
        # Als HTML speichern
        print("\nHTML")
        ob_html = HtmlStruktur()
        ob_html.tx_jsonpfad = "./dc_htmlcsv_test.json"
        ob_html.tx_htmlpfad = "./test.html"
        ob_html.tx_titel = "HTML-Struktur"
        ob_html.tx_text = "Funktionstest"
        ob_html.m_create()
        # Als CSV speichern
        print("\nCSV")
        ob_csv = CsvStruktur()
        ob_csv.tx_jsonpfad = "./dc_htmlcsv_test.json"
        ob_csv.tx_csvpfad = "./test.csv"
        ob_csv.tx_titel = "CSV-Struktur"
        ob_csv.tx_text = "Funktionstest"
        ob_csv.m_create()
