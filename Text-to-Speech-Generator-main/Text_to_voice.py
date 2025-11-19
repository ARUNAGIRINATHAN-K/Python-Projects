import tkinter as tk
from tkinter import messagebox
import pyttsx3


class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Generator")
        self.root.geometry("400x300")
        
        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        
        # Create GUI elements
        tk.Label(root, text="Enter Text:").pack(pady=10)
        
        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.pack(pady=10)
        
        # Voice selection
        tk.Label(root, text="Select Voice:").pack(pady=5)
        self.voice_var = tk.StringVar()
        self.voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in self.voices]
        self.voice_menu = tk.OptionMenu(root, self.voice_var, *voice_names)
        self.voice_menu.pack(pady=5)
        if voice_names:
            self.voice_var.set(voice_names[0])
        
        # Buttons
        tk.Button(root, text="Speak", command=self.speak_text).pack(pady=10)
        tk.Button(root, text="Clear", command=self.clear_text).pack(pady=5)
    
    def speak_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return
        
        # Set selected voice
        selected_voice = self.voice_var.get()
        for voice in self.voices:
            if voice.name == selected_voice:
                self.engine.setProperty('voice', voice.id)
                break
        
        # Speak the text
        self.engine.say(text)
        self.engine.runAndWait()
    
    def clear_text(self):
        self.text_input.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()