 
import tkinter as tk
from tkinter import scrolledtext
import datetime
import webbrowser
import os
import subprocess
import pyttsx3
import threading
import random


# VOICE ENGINE


def speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# UI COLORS


BG = "#0f172a"
CARD = "#1e293b"
TEXT = "#f1f5f9"
BUTTON = "#6366f1"
CHAT_BG = "#111827"
ENTRY_BG = "#1e293b"
USER_COLOR = "#3b82f6"
ASSISTANT_COLOR = "#10b981"

# CHAT FUNCTIONS


def add_chat(sender, message, voice=True):
    chat_area.configure(state="normal")
    time = datetime.datetime.now().strftime("%H:%M")
    
    if sender == "You":
        chat_area.insert(tk.END, f"[{time}] You : {message}\n", "user")
    else:
        chat_area.insert(tk.END, f"[{time}] Assistant: {message}\n", "assistant")

    chat_area.configure(state="disabled")
    chat_area.see(tk.END)

    if sender == "Assistant" and voice:
        threading.Thread(target = speak, args = (message,), daemon = True).start()

def process_command(user):
    user = user.lower()

    if "hello" in user or "hi" in user or "hey" in user or "hii" in user or "hyy" in user or "hlo" in user:
        replies = ["Hello!" ,
                  "Hii there!" ,
                  "Hey! How can I help You?" ,
                  "Hello! How can I assist you?" ,
                  "Hii! Nice to see you"
                  ]
        return random.choice(replies)
    elif "how are you" in user or "what's up" in user:
        replies1 = [
                   "I'm doing great! Thanks for asking",
                   "All good here! how about you?",
                   "I'm functioning perfectly!",
                   "I'm awesome! ready to help you"
                   ]
        return random.choice(replies1)

    elif "help" in user:
        replies2 = [
                  "What can I assist you with?", 
                  "Hey! How can I help You?" ,
                  "Hello! How can I assist you?" ,
                  "I'm here to help you"
                   ]
        return random.choice(replies2)

    elif "thank" in user:
        replies3 = [
                  "You're welcome!", 
                  "Anytime!" ,
                  "Happy to help!" ,
                  "No problem at all!"
                  ]
        return random.choice(replies3)

    elif "what can you do" in user:
        return "I can tell time, date, open apps,and chat with you!"

    elif "who are you" in user:
        return "I'm your AI assistant and I'm here to help you"
         
    elif "time" in user:
        return "The current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "Today's date is " + datetime.date.today().strftime("%d %B %Y")

    elif "open notepad" in user:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    elif "open calculator" in user:
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    elif "open google" in user or "open browser" in user:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open spotify" in user:
        os.system("start spotify:")
        return "Opening Spotify"

    elif "open whatsapp" in user:
        os.system("start whatsapp:")
        return "Opening Whatsapp" 

    elif "bye" in user or "exit" in user or "by" in user:
        return "Goodbye"

    else:
        fallback = [
                   "Sorry, I didn't understand that",
                   "Can you say that differently?",
                   "I'm still learning try something else!",
                   "Interesting.... tell me more!"
                   ]
        return random.choice(fallback)

def send_message(event=None):
    user_text = entry.get().strip()
    if not user_text:
        return

    add_chat("You", user_text, voice=False)
    entry.delete(0, tk.END)

    reply = process_command(user_text)
    if reply:
        add_chat("Assistant", reply)


# GUI SETUP

root = tk.Tk()
root.title("AI Assistant with Voice")
root.state("zoomed")
root.configure(bg=BG)
root.resizable(False, False)

card = tk.Frame(root, bg=CARD)
card.pack(padx=10, pady=10, fill="both", expand=True)

title = tk.Label(
    card,
    text="AI ASSISTANT",
    font=("Segoe UI", 20, "bold"),
    bg=CARD,
    fg=TEXT
)
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    card,
    height=20,
    state="disabled",
    font=("Consolas", 14),
    bg=CHAT_BG,
    fg=TEXT,
    insertbackground=TEXT
)
chat_area.pack(padx=10, pady=5, fill="both", expand=True)

chat_area.tag_config("user",foreground = USER_COLOR)
chat_area.tag_config("user",foreground = ASSISTANT_COLOR)
# Input area
input_frame = tk.Frame(card, bg=CARD)
input_frame.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 14),
    bg=ENTRY_BG,
    fg=TEXT,
    insertbackground=TEXT
)
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
entry.bind("<Return>", send_message)

send_btn = tk.Button(
    input_frame,
    text="Send",
    bg=BUTTON,
    fg="white",
    width=10,
    command=send_message
)

send_btn.pack(side="right")


# Welcome
add_chat("Assistant", "Hello! How can I help you? ")

entry.focus()
root.mainloop()