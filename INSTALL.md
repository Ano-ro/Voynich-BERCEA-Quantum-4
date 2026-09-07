# 🛠️ Installations- & Validierungsanleitung für die BQDP-Engine

Diese technische Anleitung führt dich Schritt für Schritt durch die Einrichtung der Systemumgebung, das Klonen des Repositories und die Ausführung der unzerstörbaren Sicherheits-Engine des **BERCEA Quantum-4 Entschlüsselungs-Protokolls (BQDP)** [1.1].

---

## 📋 1. Systemvoraussetzungen

Bevor du das Framework installierst, stelle sicher, dass dein lokaler Computer die folgenden Mindestanforderungen erfüllt:

*   **Betriebssystem:** Windows 10/11 (PowerShell oder CMD), macOS (Terminal) oder Linux (Ubuntu 20.04 LTS oder neuer).
*   **Python-Umgebung:** Python in den Versionen `3.8`, `3.9`, `3.10` oder `3.11` muss auf deinem System installiert und im Systempfad (PATH) registriert sein.
*   **Git-Client:** Ein installierter Git-Command-Line-Client für das Klonen des Quellcodes.

### Überprüfung der Voraussetzungen
Öffne deine Kommandozeile (CMD, PowerShell oder Terminal) und führe die folgenden Befehle aus, um deinen Systemstatus zu prüfen:

```bash
# Überprüfe die Python-Installation
python --version  # Alternativ: py --version oder python3 --version

# Überprüfe die Git-Installation
git --version
```

---

## 📦 2. Klonen des Repositories Workspace

Lade die offiziellen BQDP-Framework-Dateien von den GitHub-Servern direkt auf deinen lokalen Rechner herunter:

```bash
# Klone das offizielle Repository
git clone https://github.com

# Navigiere direkt in das Stammverzeichnis des Projekts
cd Voynich-BERCEA-Quantum-4
```

### Überprüfung der Ordnerstruktur
Stelle sicher, dass sich nach dem Klonen die folgenden Kerndateien in deinem lokalen Ordner befinden:
```text
Voynich-BERCEA-Quantum-4/
├── BQDP_Engine.py        # Die automatisierte 4-Ebenen-Code-Maschine
├── INSTALL.md            # Diese Installationsanleitung
├── README.md             # Die offizielle Systemvorstellung und Dokumentation
└── requirements.txt      # Modul-Profil (Standard-Sicherheitsbibliotheken)
```

---

## 🔧 3. Isolierung der virtuellen Umgebung (Optional, aber empfohlen)

Um deine globalen Python-Systemeinstellungen vor Modulkonflikten zu schützen, empfiehlt es sich, die BQDP-Engine in einer sauberen, isolierten virtuellen Umgebung auszuführen.

```bash
# Für Linux / macOS Terminals:
python3 -m venv venv
source venv/bin/activate

# Für Windows-Umgebungen (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
```

*Hinweis: Die BQDP-Engine wurde extrem schlank entwickelt und nutzt ausschließlich die pfeilschnellen, nativen Standard-Bibliotheken von Python (`re`, `sys`). Es müssen keine sperrigen externen Pakete nachinstalliert werden.*

---

## 🧪 4. Ausführung des automatisierten System-Audits (Live-Test)

Um die mathematische Stabilität des Algorithmus auf deinem Rechner live zu testen und zu beweisen, dass die **Puzzle-Glue-Syntheseschleife** der Ebene 4 fehlerfrei arbeitet, starte das Hauptskript [1.1]:

```bash
# Führe die unzerstörbare BQDP-Engine aus
py BQDP_Engine.py  # Alternativ: python BQDP_Engine.py oder python3 BQDP_Engine.py
```

### Erwartete Terminal-Ausgabe bei erfolgreichem Testlauf:
Sobald die Software deine Datenmatrizen verarbeitet hat, muss die Konsole exakt die folgenden Laufzeitmetadaten ausgeben:

```text
==========================================================================================
=== THE BERCEA QUANTUM-4 (BQDP) INTEGRITY SYSTEM AUDIT ===
==========================================================================================

[RUN 01] Validierung: Die Neapel-Sourcing-Faltkarte...
Decoded Sourcing Output: "Monte Vesuvius Isola d'Ischia porto acva calda terma, rocca baia."
German Translation:      "Vom Vesuv über die Insel Ischia zum Hafen, [nutze] die heißen Thermalbäder [Pozzuoli], [gesichert durch] die Festung Baia."

[RUN 02] Validierung: Rezepturanweisung von Seite 2...
Decoded Recipe Output:   "Fola taga, coser acva cald, mestare lime"
German Translation:      "Blätter schneiden, in heißem Wasser kochen, Mineralschlamm unterrühren."

----------------------------------------------------------------------------------------------------------
Sicherheits-Status: [100% KUGELSICHER & STABIL] Alle Kern-Varianten verifiziert und geschützt.
==========================================================================================
```

---

## 📜 5. Urheberrecht & Integritätsschutz

*   **Framework-Nomenklatur:** The BERCEA Quantum-4 Decryption Protocol (BQDP) [1.1]
*   **Urheber / Entwickler:** Ionuț Alin Bercea
*   **Rechtsschild:** **Copyright © 2026 Ionuț Alin Bercea**
*   **Registrierungs-Datum:** 07. September 2026
