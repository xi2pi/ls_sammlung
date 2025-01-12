# Erstellen einer Sammlung von Leitsätze des BGH (X. und Xa. Senat) und des BPatG im Zeitraum 2000 bis 2024

Der Quellcode dient der Erstellung einer Sammlung von Leitsätze des BGH (X. und Xa. Senat) und des BPatG im Zeitraum 2000 bis 2024.

Formate: .docx, .txt, .md

Als Quelle werden folgende Datensätze verwendet, aus denen die Daten extrahiert werden:

- Fobbe, S. (2024). Corpus der Entscheidungen des Bundesgerichtshofs (CE-BGH) (2024-09-25) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.12814022 (GitHub: https://github.com/SeanFobbe/ce-bgh)
- Fobbe, S. (2024). Corpus der Entscheidungen des Bundespatentgerichts (CE-BPatG) (2024-07-09) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10849977 (GitHub: https://github.com/SeanFobbe/ce-bpatg)

Die Erstellung erfolgt in drei Schritten:

1. Datenvorbereitung
2. Extraktion der Leitsätze
3. Erstellen der Dokumente

## 1. Datenvorbereitung
Die Dateien prep_data_feather.R und prep_src_data.py dienen der Datenvorbereitung. In einem ersten Schritt werden die Datensätze CE-BGH und CE-BPatG (im .csv Format) mit prep_data_feather.R in das .feather Format gebracht und dabei die Entscheidungen des X. und Xa. Zivilsenats herausgefiltert (Zielordner ist prep_data). In einem zweiten Schritt werden die .feather Dateien nach Leitsatzentscheidungen gefiltert und als .xls Dateien gespeichtert (df_zs10_ls.xlsx, df_zs10a_ls.xlsx und df_bpatg_ls.xlsx).

## 2. Extraktion der Leitsätze
Die Datei extract_ls_to_xls.py extrahiert die Leitsätze aus der Spalte "text" und erstellt dabei eine neue Spalte "leitsatz". Als Ergebnis wird eine Datei ls_all.xlsx im Ordner src_data erstellt.

## 3. Erstellen der Dokumente
Die Datei xls_to_documents.py wandelt die Tabelle ls_all.xlsx in Dokumente um (sammlung_bgh_bpatg.docx, sammlung_bgh_bpatg.txt und sammlung_bgh_bpatg.md)
