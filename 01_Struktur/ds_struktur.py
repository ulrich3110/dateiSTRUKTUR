#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ds_struktur.py - [d]atei[s]struktur
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


if __name__ == '__main__':
    # 1. Schritt
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


Verzeichnis {Pfad relativ} ({Pfad absolut})
-------------------------------------------
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

Verzeichnis     {Pfad relativ}
------------------------------
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
