# 🧠 Text ⇄ Code Konverter (GUI)

Dies ist eine vollständig lokal ausführbare Python-Anwendung zum Umwandeln von Text in ASCII, Binär, Hexadezimal und Dezimal – inklusive Rückkonvertierung. Die Anwendung bietet eine moderne grafische Oberfläche, Sprachumschaltung, Dark-/Light-Mode und GitHub-Integration.

| <img width="891" height="623" alt="1" src="https://github.com/user-attachments/assets/96c8e451-4080-4e8d-be18-c8ef6326982d" /> | <img width="889" height="622" alt="2" src="https://github.com/user-attachments/assets/91157899-261c-4766-acac-8ca2e634d890" /> |
|---|---|

---

## 🚀 Funktionen

- Text → ASCII, BIN, HEX, DEC
- ASCII, BIN, HEX, DEC → Text
- Mehrsprachige Oberfläche (DE / EN)
- Dark Mode & Light Mode live umschaltbar
- GitHub-Link als Button (unten rechts)
- Info-Button mit Logo und lokalisierter Beschreibung
- Fehlerbehandlung & Benutzerfeedback
- Responsive Oberfläche mit ttk und Farb-Themes (JSON)
- 100 % offline-fähig, keine Cloud, keine Telemetrie

## 📁 Projektstruktur

```yarn
.Text ⇄ Code Konverter
├── app.py
├── logic/
│   └── converter.py
├── themes/
│   ├── dark.json
│   └── light.json
├── locales/
│   ├── de.json
│   └── en.json
├── assets/
│   └── logo.png
```

## 🖥️ Installation

1. Python 3.9+/- installieren
2. Abhängigkeiten installieren:

```yarn
pip install pillow
```

## ▶️ Start

```yarn
python app.py
```

## 📝 Konfiguration

- Sprache: über „Sprache wechseln“-Button
- Theme: hell/dunkel über Button umschaltbar
- Info: Zeigt Projektbeschreibung mit Logo (PNG)
- Logo-Pfad: `assets/logo.png`

## ✅ Voraussetzungen

- Python 3.9 oder neuer
- PNG-Datei für Info-Dialog (optional)

## 🪪 Lizenz

MIT License – frei verwendbar
[LICENSE](LICENSE)
