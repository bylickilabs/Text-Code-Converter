# 🧠 Text ⇄ Code Konverter (GUI)

Dies ist eine vollständig lokal ausführbare Python-Anwendung zum Umwandeln von Text in ASCII, Binär, Hexadezimal und Dezimal – inklusive Rückkonvertierung. Die Anwendung bietet eine moderne grafische Oberfläche, Sprachumschaltung, Dark-/Light-Mode und GitHub-Integration.

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
