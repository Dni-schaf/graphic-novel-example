"""
Prüft alle .svg-Dateien in einem Ordner auf gültiges XML.
Gibt eine Liste aller Dateien mit Fehler aus (inkl. Zeile/Spalte/Fehlertext).

Nutzung:
    python check_svgs.py "C:\\Users\\danie\\Desktop\\Südpol\\svelte_project\\Suedpol_vs_2\\static\\images\\chapter1"
"""

import sys
import os
import xml.etree.ElementTree as ET

def check_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Ordner nicht gefunden: {folder_path}")
        return

    svg_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".svg")]
    svg_files.sort()

    if not svg_files:
        print("Keine .svg-Dateien im Ordner gefunden.")
        return

    print(f"Prüfe {len(svg_files)} SVG-Dateien in: {folder_path}\n")

    valid = []
    invalid = []

    for filename in svg_files:
        full_path = os.path.join(folder_path, filename)
        try:
            ET.parse(full_path)
            valid.append(filename)
        except ET.ParseError as e:
            invalid.append((filename, str(e)))
        except Exception as e:
            invalid.append((filename, f"Unerwarteter Fehler: {e}"))

    print(f"✅ Gültig: {len(valid)}")
    print(f"❌ Fehlerhaft: {len(invalid)}\n")

    if invalid:
        print("--- Fehlerhafte Dateien ---")
        for filename, error in invalid:
            print(f"{filename}: {error}")
    else:
        print("Keine fehlerhaften Dateien gefunden.")

    # Ergebnis zusätzlich in eine Textdatei schreiben, zum Nachschauen
    report_path = os.path.join(folder_path, "_svg_check_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"Geprüft: {len(svg_files)} Dateien\n")
        f.write(f"Gültig: {len(valid)}\n")
        f.write(f"Fehlerhaft: {len(invalid)}\n\n")
        if invalid:
            f.write("--- Fehlerhafte Dateien ---\n")
            for filename, error in invalid:
                f.write(f"{filename}: {error}\n")
    print(f"\nBericht gespeichert unter: {report_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte Ordnerpfad als Argument angeben.")
        print('Beispiel: python check_svgs.py "C:\\Pfad\\zu\\chapter1"')
        sys.exit(1)

    folder = sys.argv[1]
    check_folder(folder)
