import tkinter as tk
import pyjokes


print("Enter '1' for Neutral geeky jokes")
print("Enter '2' for Tongue-twister (will use 'all' category)")
print("Enter '3' for All types of joke")
select = input("Select one option: ")


if select == '1':
    category = "neutral"
elif select == '2':
    category = "all"  
else:
    category = "all"


root = tk.Tk()
root.title("Random Tech Joke Generator App")
root.geometry("500x300")
root.config(bg="#4682b4")


joke_label = tk.Label(root, text="", wraplength=450, bg="#4682b4", fg="white", font=("Arial", 14))
joke_label.pack(pady=50)


def new_joke():
    joke = pyjokes.get_joke(language="en", category=category)
    joke_label.config(text=joke)


tk.Button(root, text="Get New Joke", command=new_joke, bg="white", fg="#4682b4", font=("Arial", 12)).pack()


new_joke()


root.mainloop()
