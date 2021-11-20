# Darstellung Dateistruktur als Text

### Zusammenfassung `Pfad absolut`

Anzahl Verzeichnisse: `x`

Anzahl Dateien: `x`

Anzahl Dateitypen: `x`

### Verzeichnis `Pfad relativ`

Anzahl Verzeichnisse: `x`

| Verzeichnisnamen |
| --- |
| `Verzeichnis` |
| `...` |

Anzahl Dateien: `x`

Anzahl Dateitypen: `x`

| Dateiname | Typ | Änderungsdatum | Dateigrösse |
| --- | --- | --- | --- |
| `Name` | `Typ` | `Datum` | `Grösse` |
| `...` | `...` | `...` | `...` |

# Darstellung Dateistruktur als Tabelle

| Kategorie | Anzahl | Verzeichnisnamen | Dateiname | Dateityp | Datum/Uhrzeit | Grösse (bytes) |
| --- | --- | --- | --- | --- | --- | --- |
| `Titel` | | | | | | |
| `Beschrieb` | | | | | | |
| Übericht Hauptverzeichnis | | `absoluter Pfad` | | | | |
| Datum / Uhrzeit | | | | | `Datum` | |
| Anzahl Verzeichnisse | `x` | | | | | |
| Anzahl Dateien | `x` | | | | | |
| Anzahl Dateitypen | `x` | | | | | |
| Verzeichnis | | `relativer Pfad` | | | | |
| Anzahl Verzeichnisse | `x` | | | | | |
| Verzeichnisliste | `x` | | | | | |
| Verzeichnis #1 | | `Name` | | | | |
| Verzeichnis #.. | | `Name` | | | | |
| Anzahl Dateien | `x` | | | | | |
| Anzahl Dateitypen | `x` | | | | | |
| Datei #1 | | | `Name` | `Typ` | `Datum` | `x` |
| Datei #.. | | | `Name` | `Typ` | `Datum` | `x` |

# Format der JSON Datei-Struktur

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
