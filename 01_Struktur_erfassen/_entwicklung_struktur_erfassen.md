# Entwicklung Struktur erfassen

* Struktur erfassen wie bei pyOsTools

* Datum und Grösse der Dateien erfassen

* Dateistruktur ordnen

  * Stammverzeichnis

    * Pfad absolut

    * Anzahl Verzeichnisse

    * Anzahl Dateien

    * Anzahl Dateitypen

  * Unterverzeichnisse

    * Pfad relativ

    * Pfad absolut

    * Anzahl Verzeichnisse

    * Liste mit Verzeichnisnamen

    * Anzahl Dateien

    * Anzahl Dateitypen

    * Dateien als Verzeichnis {Dateityp: Dateinamen, Dateidatum, Dateigrösse}

* Alles zusammen als JSON speichern in einem lesbaren Format

* Kontrolle der gespeicherten JSON

```python
JSON = {
  "DATEIANZAHL": zahl,
  "DATEILISTE": ['Dateipfade', ],
  "DATUM": 'TT.MM.JJJJ hh:mm:ss',
  "STAMMPFAD": 'absoluter Pfad',
  "TYPANZAHL": zahl,
  "VERZEICHNISANZAHL": zahl,
  "VERZEICHNISLISTE": ['Verzeichnispfade', ],
  "VERZEICHNISSE": [
    {
      "DATEIANZAHL": zahl,
      "DATEILISTE": [
        {
          "DATUM": 'tt.mm.jjjj hh:mm:ss',
          "GROESSE": zahl,
          "NAME": 'dateiname',
          "TYP": 'erw'
        },
      ],
      "PFAD": 'relativer pfad zum absolutem Stammpfad',
      "TYPANZAHL": zahl,
      "VERZEICHNISANZAHL": zahl,
      "VERZEICHNISLISTE": ['Verzeichnisname', ]
    },
  ]
}
```
