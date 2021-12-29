#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
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
    - dc_verz = Wörterbuch
    - tx_pfad = Pfad
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
                    "ERFASSEN",
                    {
                        "ZIEL": ".",
                        "JSON": "./struktur.json"
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
        self.dc_befehle = f_loadjson("./ds_erfassen.json")
        if not self.dc_befehle:
            # Fehler beim Laden, Einstellungen erzeugen
            self.m_reset_befehle()
            # Einstellungen sichern
            f_savejson("./ds_erfassen.json", self.dc_befehle)

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
            if tx_befehl == "ERFASSEN":
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


if __name__ == '__main__':
    # RunJson Objekt und Befehle laden
    ob_rj = RunJson()
    ob_rj.m_load()
    # Testmodus prüfen
    if not ob_rj.dc_befehle["TESTMODUS"]:
        ob_rj.m_run()
    else:
        # Test DateiInfo
        print("\nDATEIINFO TEST")
        # Leeres DateiInfo Objekt
        ob_datinf = DateiInfo()
        print(ob_datinf)
        # Mit Werten
        ob_now = datetime.datetime.today()
        dc_test = {
            "NAME": "Testdatei",
            "TYP": "TXT",
            "DATUM": ob_now.strftime('%d.%m.%Y %H:%M:%S'),
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
            "PFAD": '.',
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
        ob_now = datetime.datetime.today()
        dc_test = {
            "DATEILISTE": [],
            "VERZEICHNISLISTE": [],
            "STAMMPFAD": '.',
            "DATUM": ob_now.strftime('%d.%m.%Y %H:%M:%S'),
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
