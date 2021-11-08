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
  "STAMMPFAD": 'absoluter Pfad',
  "VERZEICHNISANZAHL": zahl,
  "DATEIANZAHL": zahl,
  "TYPANZAHL": zahl,
  "VERZEICHNISSE": [
    {
      "PFAD": 'relativer pfad zum absolutem Stammpfad'
      "DATUM": 'tt.mm.jjjj hh:mm:ss'
      "VERZEICHNISANZAHL": zahl,
      "VERZEICHNISLISTE": ['Verzeichnisname', ],
      "DATEIANZAHL": zahl,
      "TYPANZAHL": zahl,
      "DATEILISTE": [
        {
          "NAME": 'dateiname',
          "TYP": 'erw',
          "DATUM": 'tt.mm.jjjj hh:mm:ss'
          "GROESSE": zahl
        },
      ]
    }
  ]
}
```
