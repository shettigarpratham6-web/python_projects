
import  pyttsx3

engine = pyttsx3.init()
text=input("Enter the text that you want to hear: ")
engine.say(text)
engine.runAndWait()
engine.setProperty('rate', 125)
