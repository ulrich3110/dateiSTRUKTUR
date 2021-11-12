# Darstellung Dateistruktur

### Zusammenfassung `Pfad absolut`

Anzahl Verzeichnisse: `x`

Anzahl Dateien: `x`

Anzahl Dateitypen: `x`

### Verzeichnis `Pfad relativ`

Anzahl Verzeichnisse: `x`

| _Verzeichnisnamen_ |
| --- |
| `Verzeichnis` |
| `...` |

Anzahl Dateien: `x`

Anzahl Dateitypen: `x`

| Dateityp `x` | | |
| --- | --- | --- |
| _Dateiname_ | _Änderungsdatum_ | _Dateigrösse_ |
| `Name` | `Datum` | `Grösse` |
| `...` | `...` | `...` |

`Weitere Auflistung nach Dateityp und Name sortiert`

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
