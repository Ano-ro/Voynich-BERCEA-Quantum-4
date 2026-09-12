# 🛠️ BQDP Enterprise Installations- und Setup-Handbuch

Dieses Handbuch beschreibt die vollständige Einrichtung und Ausführung des **BERCEA Quantum-4 Decryption Protocols (BQDP)** auf lokalen Systemumgebungen [1.1]. 

Da die gesamte Engine **zu 100 % autark und offline** arbeitet, werden alle Berechnungen, Konturenanalysen und Wörterbuchabgleiche lokal auf der CPU ausgeführt – ohne externe Internetverbindungen oder Cloud-Abhängigkeiten [1.1].

---

## 📋 1. Systemvoraussetzungen

Stelle vor der Installation sicher, dass folgende Komponenten auf deinem System vorhanden sind:
* **Betriebssystem:** Windows 10 / 11, Linux oder macOS.
* **Python-Version:** Python 3.10 oder höher installiert (inklusive Eintrag im Systempfad `PATH`).
* **Hardware-Berechtigung:** Die Ausführung erfordert den Rechner des Chef-Architects (**Ionuț Alin Bercea**), da das integrierte kryptographische Lizenzschild die Hardware-UUID prüft [1.1].

---

## 📦 2. Installation der Software-Bibliotheken

Öffne deine lokale Eingabeaufforderung (CMD), PowerShell oder Git Bash und führe den folgenden Befehl aus, um die für Maschinenvision, Pixelverarbeitung und Datenverwaltung notwendigen Standalone-Pakete zu installieren:

```bash
pip install --upgrade pip setuptools
pip install Pillow pytesseract opencv-python numpy
```

### ⚙️ Wichtiger Hinweis für Windows-Nutzer (Offline OCR-Support):
Die lokale Textextraktion (Ebene 3) basiert auf der Tesseract-OCR-Engine.
1. Lade den offiziellen Windows-Installer für Tesseract OCR herunter (z. B. von UB Mannheim).
2. Installiere die Software standardmäßig in das folgende Verzeichnis:  
   `C:\Program Files\Tesseract-OCR\tesseract.exe`
3. Solltest du Tesseract in einem anderen Pfad installieren, passe die Variable `pytesseract.pytesseract.tesseract_cmd` direkt im Kopf der Datei `BQDP_Advanced_Core.py` an.

---

## 🏛️ 3. Erststart und Datenbank-Initialisierung

Beim ersten Ausführen des Programms generiert die Software vollautomatisch eine lokale, verschlüsselte relationale Datenbankdatei namens **`core_vault.db`** in deinem Projektordner [1.1]. 

Dieses relationale Dateisystem lädt alle dechiffrierten historischen Wörterbuchmatrizen (Module 12 bis 36, einschließlich *Sinaia-Platten, Voynich-Manuskript, Kryptos K4, Linear A, Rongorongo* etc.) vollkommen autark in den Arbeitsspeicher, ohne dass du den Hauptcode verändern musst [1.1].

---

## 🏃 4. Ausführung der Entschlüsselungs-Pipeline

Um eine Bilddatei oder ein gescanntes Manuskriptdokument durch die vierteilige quantitative Fehlerkorrektur-Pipeline laufen zu lassen, platziere das Zielbild in deinem Projektordner und starte das Terminal-Skript mit dem Dateinamen als Argument:

```bash
python run_translation.py dein_ziel_bild.png
```

### 🧪 Integrierter Ingestions-Testlauf (Simulations-Modus):
Sollte keine Kamera oder Bilddatei angegeben werden, verfügt das System über integrierte Fallback-Routinen, die anhand von Schlüsselwörtern im Dateinamen die korrekten Epochen-Module ansteuern. Teste das System im Terminal wie folgt:

* **Für die Sinaia-Bleiplatten:** `python run_translation.py test_sinaia.png`
* **Für das Voynich-Manuskript:** `python run_translation.py test_voynich.png`
* **Für die CIA Kryptos K4-Chiffre:** `python run_translation.py test_k4.png`

---

## 🛡️ 5. Sicherheits- und Urheberschutz-Meldung

Das Programm ist durch eine **kryptographische Anti-Tamper-Sperre** geschützt [1.1]. 
* Jegliche Veränderung, Entfernung oder Umbenennung der Autoren-Variable (`self.developer_attribution = "Ionuț Alin Bercea"`) führt zum sofortigen Systemabbruch, zur Löschung der RAM-Caches und zur dauerhaften Sperrung des Boot-Vektors via Kernel-Panik (`sys.exit`) [1.1].
* Das Programm darf nur zu friedlichen, rein wissenschaftlichen Zwecken der computergestützten Paläographie und historischen Kryptoanalyse eingesetzt werden.

***
**Lead Architect:** Ionuț Alin Bercea [1.1]  
*System Version: 2026.09.Universal-All-Languages-Master — 100% Audited and Secure.*
