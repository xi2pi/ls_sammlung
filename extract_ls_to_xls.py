# -*- coding: utf-8 -*-
"""
@author: Christian Winkler
"""

import pandas as pd
import os
import re



'''
BPatG
'''

# Funktion zum Extrahieren des Leitsatzes (ohne "Normen:"-Zeile)
def extrahiere_leitsatz_bpatg(text):
    # Suchen nach "Normen:", Leerzeile und dem Bereich bis "BUNDESPATENTGERICHT"
    #match = re.search(r"Normen:.*?\s*\n(.*?)\s*BUNDESPATENTGERICHT", text, re.DOTALL)
    match = re.search(r"Normen:.*?(?=\s*BUNDESPATENTGERICHT)", text, re.S)
    if match:
        return match.group(0).strip()  # Extrahierten Text bereinigen und zurückgeben
    return None  # Falls kein Leitsatz gefunden wird

# Pfad zur Excel-Datei
excel_datei = "src_data/df_bpatg_ls.xlsx"

# Excel-Datei einlesen
df_bpatg = pd.read_excel(excel_datei)

# Neue Spalte "leitsatz" erstellen
df_bpatg["leitsatz"] = df_bpatg["text"].apply(extrahiere_leitsatz_bpatg)

# Überprüfen, ob die Spalte "text" vorhanden ist
if "text" not in df_bpatg.columns:
    raise ValueError("Die Spalte 'text' wurde nicht in der Excel-Datei gefunden.")

# Funktion zur Nachbearbeitung und zum Entfernen von Leerzeilen
def bereinige_leitsatz(leitsatz):
    if isinstance(leitsatz, str):
        lines = leitsatz.splitlines()
        # Entferne Leerzeilen
        lines = [line for line in lines if line.strip()]  # Zeilen, die nur Leerzeichen enthalten, werden entfernt
        return "\n".join(lines)
    return leitsatz  # Rückgabe unverändert, falls kein Text vorhanden ist

# Spalte "leitsatz" nachbearbeiten
df_bpatg["leitsatz"] = df_bpatg["leitsatz"].apply(bereinige_leitsatz)




'''
X. und Xa. Zivilsenat
'''
# Funktion zum Extrahieren des Leitsatzes
def extrahiere_leitsatz(text):
    # Regex: Sucht nach den Anfangszeilen und ignoriert alles bis zur ersten Leerzeile
    match = re.search(
        #r"(Nachschlagewerk.*?\n|BGHZ.*?\n|BGHR.*?\n)+\s*\n(.*?)(\n\s*BGH,)",
        "(Nachschlagewerk.*?|BGHZ.*?|BGHR.*?)+\s*\n(.*?)(\n\s*BGH,)", 
        text, 
        re.DOTALL
    )
    if match:
        return match.group(2).strip()  # Nur den relevanten Text nach der Leerzeile zurückgeben
    return None  # Falls kein Leitsatz gefunden wird

# Pfad zur Excel-Datei
excel_datei1 = "src_data/df_zs10_ls.xlsx"

# Pfad zur Excel-Datei
excel_datei2 = "src_data/df_zs10a_ls.xlsx"

# Excel-Datei einlesen
df1 = pd.read_excel(excel_datei1)

# Excel-Datei einlesen
df2 = pd.read_excel(excel_datei2)

# Combination
df_zs = df1.append(df2)

# Neue Spalte "leitsatz" erstellen
df_zs["leitsatz"] = df_zs["text"].apply(extrahiere_leitsatz)

# Überprüfen, ob die Spalte "text" vorhanden ist
if "text" not in df_zs.columns:
    raise ValueError("Die Spalte 'text' wurde nicht in der Excel-Datei gefunden.")

# Funktion zur Nachbearbeitung und zum Entfernen von Leerzeilen
def bereinige_leitsatz(leitsatz):
    if isinstance(leitsatz, str):
        # Entferne Zeilen, die mit "BGHR:", "BGHZ:", oder "Nachschlagewerk:" beginnen
        lines = leitsatz.splitlines()
        lines = [line for line in lines if not re.match(r"^(JNEU|BGHR|BGHZ|Nachschlagewerk)", line)]
        # Entferne Leerzeilen
        lines = [line for line in lines if line.strip()]  # Zeilen, die nur Leerzeichen enthalten, werden entfernt
        return "\n".join(lines)
    return leitsatz  # Rückgabe unverändert, falls kein Text vorhanden ist

# Spalte "leitsatz" nachbearbeiten
df_zs["leitsatz"] = df_zs["leitsatz"].apply(bereinige_leitsatz)


'''
Zusammenfügen und Speichern
'''

#df_zs[["aktenzeichen", "text", "leitsatz"]].to_excel("leitsätze/ls_all.xlsx")

df = df_zs.append(df_bpatg)

df[["aktenzeichen", "text", "leitsatz"]].to_excel("src_data/ls_all.xlsx")

print(f"{len(df)} Entscheidungen")



'''
LOG
'''

# Statistik
extrahiert = df["leitsatz"].notnull().sum()  # Anzahl der extrahierten Leitsätze
nicht_extrahiert = df["leitsatz"].isnull().sum()  # Anzahl der nicht extrahierten Leitsätze

# Ausgabe der Statistik
print("Statistik der Leitsätze:")
print(f"Anzahl der extrahierten Leitsätze: {extrahiert}")
print(f"Anzahl der nicht extrahierten Leitsätze (Leerzeilen): {nicht_extrahiert}")

# Optional: Speichern der Statistik in einer Datei
with open("src_data/log.txt", "w") as file:
    file.write("Statistik der Leitsätze:\n")
    file.write(f"Anzahl der extrahierten Leitsätze: {extrahiert}\n")
    file.write(f"Anzahl der nicht extrahierten Leitsätze (Leerzeilen): {nicht_extrahiert}\n")


'''
TXT Dateien
'''

# # Erstellen der txt-Dateien
# for index, row in df_bpatg.iterrows():
#     text = row["text"]
#     dateiname = os.path.join(zielordner, str(row["aktenzeichen"])+".txt")
#     dateiname = dateiname.replace("/", "_")
        
#     # Text in die Datei schreiben
#     with open(dateiname, "w", encoding="utf-8") as file:
#         file.write(str(text))

# print(f"{len(df_bpatg)} txt-Dateien wurden im Ordner '{zielordner}' erstellt.")

#df[["aktenzeichen", "text", "leitsatz"]].to_excel("leitsätze/bpatg.xlsx") 


# # Erstellen der txt-Dateien
# for index, row in df.iterrows():
#     try:
#         text = row["leitsatz"]
#         dateiname = os.path.join(zielordner, str(row["aktenzeichen"])+".txt")
#         dateiname = dateiname.replace("/", "_")
        
#         # Text in die Datei schreiben
#         with open(dateiname, "w", encoding="utf-8") as file:
#             file.write(str(text))
#     except:
#         print(row["aktenzeichen"])
 
# print(f"{len(df)} txt-Dateien wurden im Ordner '{zielordner}' erstellt.") 

