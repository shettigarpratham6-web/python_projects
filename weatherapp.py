from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x500")
name_label=Label(win,text="Weather App",font=("Consolas",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_name= [
        "Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural",
        "Bengaluru Urban", "Bidar", "Chamarajanagar",
        "Chikkaballapur", "Chikkamagaluru", "Chitradurga",
        "Dakshina Kannada", "Davanagere", "Dharwad",
        "Gadag", "Hassan", "Haveri", "Kalaburagi",
        "Kodagu", "Kolar", "Koppal", "Mandya",
        "Mysuru", "Raichur", "Ramanagara",
        "Shivamogga", "Tumakuru", "Udupi",
        "Uttara Kannada", "Vijayapura", "Yadgir"
    ]
com=ttk.Combobox(win,text="Weather App",values=list_name,font=("Consolas",30,"bold"))
com.place(x=25,y=120,height=50,width=450)
done_button=Button(win,text="Done",font=("Consolas",30,"bold"))
done_button.place(x=200,y=190,height=50,width=100)

w_label=Label(win,text="Weather Climate",font=("Consolas",20,"bold"))
w_label.place(x=25,y=260,height=50,width=250)

win.mainloop()
