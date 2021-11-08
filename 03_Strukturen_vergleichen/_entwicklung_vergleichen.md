# Entwicklung Strukturen vergleichen

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

        ```
        #                   Ziel  Quelle
        {Verzeichnisnamen: (True, True)}
        ```

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

        ```
        {Dateityp: Dateinamen, Dateidatum, "neuer/älter", Dateigrösse, "grösser/kleiner"}
        ```

- Alles zusammen als JSON speichern in einem lesbaren Format

- Kontrolle der gespeicherten JSON
