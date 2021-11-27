# Entwicklung Strukturen vergleichen

- Quellstruktur aus JSON laden

- Zielstruktur aus JSON laden

- Zusammenfassung vergleichen

  - Unterschiede Anzahl Dateien

    - Quelle als Zahl

    - Ziel als Zahl

    - Differenz Ziel zu Quelle als Zahl

  - Unterschiede Anzahl Verzeichnisse

    - Quelle als Zahl

    - Ziel als Zahl

    - Differenz Ziel zu Quelle als Zahl

  - Unterschiede Anzahl Dateitypen

    - Quelle als Zahl

    - Ziel als Zahl

    - Differenz Ziel zu Quelle als Zahl

- Verzeichnisse vergleichen

    - Unterschiede Anzahl Verzeichnisse

      - Quelle als Zahl

      - Ziel als Zahl

      - Differenz Ziel zu Quelle als Zahl

    - Unterschied Verzeichnislisten

      - Unterschiede Verzeichnisse als Wörterbuch

        ```
                           Ziel  Quelle
        {Verzeichnisname: (True, True)}
        ```

    - Unterschiede Anzahl Dateien

      - Quelle als Zahl

      - Ziel als Zahl

      - Differenz Ziel zu Quelle als Zahl

    - Unterschiede Anzahl Dateitypen

      - Quelle als Zahl

      - Ziel als Zahl

      - Differenz Ziel zu Quelle als Zahl

    - Unterschied Dateien Ziel zu Quellen

      - Unterschiede Dateien als Wörterbuch

        ```
        {Dateiname, Dateityp, Dateidatum, "neuer/älter", Dateigrösse, "grösser/kleiner"}
        ```

- Alles zusammen als JSON speichern in einem lesbaren Format

- Kontrolle der gespeicherten JSON
