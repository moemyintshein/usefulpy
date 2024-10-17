import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator App")
        self.master.geometry("450x450")
        
        self.translator = Translator()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Source language selection
        ttk.Label(self.master, text="Source Language:").grid(row=0, column=0, padx=5, pady=5)
        self.src_lang = ttk.Combobox(self.master, values=list(LANGUAGES.values()), width=30)
        self.src_lang.grid(row=0, column=1, padx=5, pady=5)
        self.src_lang.set("english")
        
        # Target language selection
        ttk.Label(self.master, text="Target Language:").grid(row=1, column=0, padx=5, pady=5)
        self.dest_lang = ttk.Combobox(self.master, values=list(LANGUAGES.values()), width=30)
        self.dest_lang.grid(row=1, column=1, padx=5, pady=5)
        self.dest_lang.set("myanmar (burmese)")
        
        # Source text input
        ttk.Label(self.master, text="Enter text:").grid(row=2, column=0, padx=5, pady=5)
        self.src_text = tk.Text(self.master, height=10, width=40)
        self.src_text.grid(row=2, column=1, padx=5, pady=5)
        
        # Translate button
        self.translate_btn = ttk.Button(self.master, text="Translate", command=self.translate)
        self.translate_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Translated text output
        ttk.Label(self.master, text="Translation:").grid(row=4, column=0, padx=5, pady=5)
        self.dest_text = tk.Text(self.master, height=10, width=40)
        self.dest_text.grid(row=4, column=1, padx=5, pady=5)
    
    def translate(self):
        src = self.src_text.get("1.0", tk.END).strip()
        src_lang = self.src_lang.get()
        dest_lang = self.dest_lang.get()
        
        # Get language codes
        src_lang_code = next(key for key, value in LANGUAGES.items() if value.lower() == src_lang.lower())
        dest_lang_code = next(key for key, value in LANGUAGES.items() if value.lower() == dest_lang.lower())
        
        # Translate
        translation = self.translator.translate(src, src=src_lang_code, dest=dest_lang_code)
        
        # Display translation
        self.dest_text.delete("1.0", tk.END)
        self.dest_text.insert(tk.END, translation.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()