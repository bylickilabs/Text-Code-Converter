# 🧠 Text ⇄ Code Converter (GUI)

A fully offline-capable Python application for converting text to ASCII, binary, hex, and decimal – and back. The GUI includes dark/light mode, multilingual support, GitHub integration and an animated info dialog with your logo.

## 🚀 Features

- Text → ASCII, BIN, HEX, DEC
- ASCII, BIN, HEX, DEC → Text
- Multilingual (English / German)
- Dark mode & light mode toggle
- GitHub link (bottom-right button)
- Info dialog with logo and localized description
- Error handling & clipboard integration
- Modern tkinter GUI with themed styles (via JSON)
- 100% local – no cloud, no telemetry

## 📁 Project Structure

```yarn
.Text ⇄ Code Converter
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

1. Install Python 3.9+/-
2. Install dependencies:

```yarn
pip install pillow
```

## ▶️ Run

```yarn
python app.py
```

## 📝 Configuration

- Language: via switch button in GUI
- Theme: light/dark toggle
- Info: displays project description and PNG logo
- Logo path: `assets/logo.png`

## ✅ Requirements

- Python ≥ 3.9
- PNG image for info dialog (optional)

## 🪪 License

MIT License – free for use and modification
[LICENSE](LICENSE)
