# -*- coding: utf-8 -*-
"""
==========================================================================================
===            THE BERCEA QUANTUM-4 DECRYPTION PROTOCOL (BQDP)                         ===
===            SYSTEM STAGE: RUNTIME RUNNER ACCELERATOR TERMINAL WRAPPER               ===
==========================================================================================
Leitender Architekt: Ionuț Alin Bercea [1.1]
"""

import sys
import os

def execute_console_stream(target_image):
    """Bootet die BQDP-Kern-Engine sicher und leitet die forensische Entschlüsselungsausgabe weiter."""
    try:
        from BQDP_Advanced_Core import BQDPAdvancedProcessor
        processor = BQDPAdvancedProcessor()
    except ImportError:
        print("\n❌ [STARTFEHLER] Kritischer Abhängigkeitskonflikt!")
        print("   Stelle sicher, dass 'BQDP_Advanced_Core.py' im selben Verzeichnis liegt.")
        sys.exit(1)
    except SystemExit as se:
        print(f"\n❌ [BOOT ABGEBROCHEN] Sicherheits-Schild Interzept: {se}")
        sys.exit(1)

    # Ausführung der vollständigen quantitativen Bildanalyse und Datenbankabfrage
    report = processor.translate_image_matrix(target_image)
    
    print("\n" + "="*95)
    print(f"🎬 PIPELINE-STATUS: {report['status']}")
    print(f"📁 DATEI-CONTAINER: {report.get('datei', 'Unbekannt')}")
    print("="*95)
    
    # Iteration durch die extrahierten Token-Ergebnisse mit sauberer Bildschirmformatierung
    for idx, entry in enumerate(report.get("ergebnisse", []), 1):
        print(f"📌 ABSCHNITT {idx:02d} [Graphem: '{entry['token']}']:")
        print(f"   📝 KLARTEXT:  {entry['klartext']}")
        print(f"   🔤 DIALEKT:   {entry['dialekt']}")
        print(f"   🏛️ HERKUNFT:  {entry['herkunft']}")
        print(f"   ⚙️ PIPELINE:  {entry['status']}\n")
        
    print("="*95)
    print(f"🟩 SYSTEM-AUTORSCHAFT SOUVERÄN GESICHERT FÜR: {processor.developer_attribution} [1.1]\n")

if __name__ == "__main__":
    # Prüfen, ob ein benutzerdefiniertes Bildargument über die Terminalparameter übergeben wurde
    if len(sys.argv) > 1:
        file_target = sys.argv
    else:
        # Standardmäßiges lokales Validierungsprofil, falls kein Argument übergeben wird
        file_target = "test_manuscript.png"
        
    execute_console_stream(file_target)
