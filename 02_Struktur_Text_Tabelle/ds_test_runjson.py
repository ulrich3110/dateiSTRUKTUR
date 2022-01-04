#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ds_htmlcsv import *
from ds_test_funktionen import *

'''
ds_test_runjson.py - [d]atei[s]strukturen <RunJson> Test
Copyright (c) Dezember 2021: Andreas Ulrich
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
    '''
    Beschreibung
    '''
    print("DS_TEST_RUNJSON")
    print("---------------")
    print("Objekt:        RunJson")
    print("Methoden:      __init__(), m_reset_befehle(), m_load(),")
    print("               m_run()")
    print("Attribute:     dc_befehle")
    # Anzahl Fehler
    in_anzerr = 0
    # Modus, True = produktiver Test, False = diese Script prüfen
    bl_modus = True
    '''
    OBJEKT erzeugen
    '''
    tx_test = "RunJson Objekt erzeugen"
    f_testtitel(tx_test)
    ob_run = RunJson()
    '''
    __STR__ testen
    '''
    tx_test = "RunJson.__str__()"
    f_testtitel(tx_test)
    tx_r = ob_run.__str__()
    # Test
    if tx_r:
        bl_test = True
    else:
        bl_test = False
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            "'..'", tx_r)
    '''
    RESET testen
    '''
    tx_test = "RunJson.m_reset_befehle()"
    f_testtitel(tx_test)
    ob_run.m_reset_befehle()
    # Vorgabe
    tx_vorgabe = str(type([]))
    # Resultat
    ls_r = ob_run.dc_befehle["BEFEHLE"]
    tx_r = str(type(ls_r))
    # Test
    bl_test = tx_vorgabe == tx_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_vorgabe, tx_r)
    '''
    LADEN testen
    '''
    tx_test = "RunJson.m_load()"
    f_testtitel(tx_test)
    ob_run.m_load()
    # Vorgabe
    tx_vorgabe = str(type([]))
    # Resultat
    ls_r = ob_run.dc_befehle["BEFEHLE"]
    tx_r = str(type(ls_r))
    # Test
    bl_test = tx_vorgabe == tx_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            tx_vorgabe, tx_r)
    '''
    RUN testen
    '''
    tx_test = "RunJson.m_load()"
    f_testtitel(tx_test)
    # Vorgabe
    vl_w = None
    # Resultat
    vl_r = ob_run.m_run()
    # Test
    bl_test = vl_w == vl_r
    # Vergleich
    in_anzerr = f_vergleich(bl_modus, bl_test, in_anzerr, tx_test,
                            str(vl_w), str(vl_r))
    '''
    ZUSAMMENFASSUNG
    '''
    print()
    print(f_formattext("ANZAHL", str(in_anzerr)))
