import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

def say_now():
    text = text_box.get("1.0", tk.END)   
    if text.strip() != "":
        engine.say(text)
        engine.runAndWait()

root = tk.Tk()
root.title("🎤 Text to Speech App")
root.geometry("400x300")
root.config(bg="#4682b4")

tk.Label(
    root,
    text="......Enter text to Speak......",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#9b59b6"
).pack(pady=15)


text_box = tk.Text(
    root,
    width=40,
    height=5,            
    font=("Arial", 12),
    bg="#121212",
    fg="white",
    insertbackground="white",
    wrap="word"            
)
text_box.pack(pady=10)

tk.Button(
    root,
    text="Speak 🔊",
    font=("Arial", 12, "bold"),
    bg="#00adb5",
    fg="white",
    activebackground="#007a80",
    relief="raised",
    command=say_now
).pack(pady=20)

root.mainloop()
