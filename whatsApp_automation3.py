import pywhatkit as kt
import time


PHONE = "+919876543210"   # receiver number
GAP = 30                 # seconds gap between messages

messages = [
    "Hello",
    "This is my WhatsApp bot!",
    "It is sending messages automatically 📩",
    "Done!"
]

# === MESSAGE SENDER ===
for msg in messages:
    try:
        kt.sendwhatmsg_instantly(PHONE, msg)
        print(f"Sent: {msg}")
        time.sleep(GAP)
    except:
        print("Error sending message!")
