import tkinter as tk
from tkinter import ttk, messagebox
import json, os
import webbrowser
from PIL import Image, ImageTk
from logic.converter import *

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.lang = "en"
        self.theme = "dark"
        self.load_theme()
        self.load_lang()
        self.build_ui()

    def load_theme(self):
        with open(f"themes/{self.theme}.json", encoding="utf-8") as f:
            self.colors = json.load(f)

    def load_lang(self):
        with open(f"locales/{self.lang}.json", encoding="utf-8") as f:
            self.texts = json.load(f)

    def build_ui(self):
        self.root.title(self.texts["title"])
        self.root.geometry("880x580")
        self.root.configure(bg=self.colors["bg"])

        input_label = tk.Label(self.root, text=self.texts["input_label"], bg=self.colors["bg"], fg=self.colors["fg"])
        input_label.pack(anchor="w", padx=20, pady=(15, 0))

        self.input_text = tk.Text(self.root, height=5, wrap="word", bg=self.colors["entry"], fg=self.colors["fg"])
        self.input_text.pack(fill="x", padx=20, pady=5)
        
        github_frame = tk.Frame(self.root, bg=self.colors["bg"])
        github_frame.pack(side="bottom", anchor="se", fill="x", pady=8, padx=15)

        ttk.Button(github_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/bylickilabs"))\
        .pack(side="right", anchor="e")        


        btn_frame = tk.Frame(self.root, bg=self.colors["bg"])
        btn_frame.pack(pady=10)

        buttons = [
            ("to_ascii", self.convert_ascii), ("to_bin", self.convert_bin),
            ("to_hex", self.convert_hex), ("to_dec", self.convert_dec),
            ("ascii_to_text", self.convert_ascii_text),
            ("bin_to_text", self.convert_bin_text),
            ("hex_to_text", self.convert_hex_text),
            ("dec_to_text", self.convert_dec_text)
        ]

        for i, (key, cmd) in enumerate(buttons):
            ttk.Button(btn_frame, text=self.texts[key], command=cmd).grid(row=i//4, column=i%4, padx=10, pady=5)


        output_label = tk.Label(self.root, text=self.texts["output_label"], bg=self.colors["bg"], fg=self.colors["fg"])
        output_label.pack(anchor="w", padx=20, pady=(10, 0))

        self.output_text = tk.Text(self.root, height=7, wrap="word", bg=self.colors["entry"], fg=self.colors["fg"])
        self.output_text.pack(fill="x", padx=20, pady=(0, 10))


        action_frame = tk.Frame(self.root, bg=self.colors["bg"])
        action_frame.pack(pady=5)

        ttk.Button(action_frame, text=self.texts["copy"], command=self.copy_output).pack(side="left", padx=10)
        ttk.Button(action_frame, text=self.texts["clear"], command=self.clear_all).pack(side="left", padx=10)
        ttk.Button(action_frame, text=self.texts["lang_switch"], command=self.switch_language).pack(side="left", padx=10)
        self.theme_btn = ttk.Button(
            action_frame,
            text=self.texts["light_mode"] if self.theme == "dark" else self.texts["dark_mode"],
            command=self.toggle_theme
        )
        self.theme_btn.pack(side="left", padx=10)

        ttk.Button(action_frame, text=self.texts["info"], command=self.show_info).pack(side="left", padx=10)

    def get_input(self):
        return self.input_text.get("1.0", tk.END).strip()

    def set_output(self, text):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)

    def copy_output(self):
        output = self.output_text.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(output)
        messagebox.showinfo("Info", f"{self.texts['copy']}: OK")

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def switch_language(self):
        self.lang = "de" if self.lang == "en" else "en"
        self.rebuild_ui()

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.rebuild_ui()

    def rebuild_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.load_theme()
        self.load_lang()
        self.build_ui()

    def show_info(self):
        win = tk.Toplevel(self.root)
        win.title(self.texts["info"])
        win.geometry("640x500")
        win.configure(bg=self.colors["bg"])

        try:
            image = Image.open("assets/logo.png")
            image = image.resize((620, 120), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)
            img_label = tk.Label(win, image=img, bg=self.colors["bg"])
            img_label.image = img
            img_label.pack(pady=(15, 5))
        except Exception as e:
            print(f"Bild konnte nicht geladen werden: {e}")

        text = tk.Text(win, wrap="word", bg=self.colors["entry"], fg=self.colors["fg"],
                       relief="flat", font=("Segoe UI", 10))
        text.pack(fill="both", expand=True, padx=10, pady=5)
        text.insert("1.0", self.texts["info_text"])
        text.config(state="disabled")

        ttk.Button(win, text="OK", command=win.destroy).pack(pady=10)


    def convert_ascii(self): self._safe_convert(lambda: ' '.join(text_to_ascii(self.get_input())))
    def convert_bin(self): self._safe_convert(lambda: ' '.join(text_to_bin(self.get_input())))
    def convert_hex(self): self._safe_convert(lambda: ' '.join(text_to_hex(self.get_input())))
    def convert_dec(self): self._safe_convert(lambda: ' '.join(text_to_dec(self.get_input())))
    def convert_ascii_text(self): self._safe_convert(lambda: ascii_to_text(self.get_input()))
    def convert_bin_text(self): self._safe_convert(lambda: bin_to_text(self.get_input()))
    def convert_hex_text(self): self._safe_convert(lambda: hex_to_text(self.get_input()))
    def convert_dec_text(self): self._safe_convert(lambda: dec_to_text(self.get_input()))

    def _safe_convert(self, func):
        try:
            self.set_output(func())
        except Exception as e:
            self.set_output(f"[Error] {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()