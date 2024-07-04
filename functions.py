import tkinter as tk
from tkinter import messagebox
from difflib import get_close_matches
import speech_recognition as sr
import pyttsx3
import json



# Initialize Pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
# Function to read out meaning
def meaningAudio(meaningArea):
    engine.say(meaningArea.get(1.0, tk.END))
    engine.runAndWait()


# Function to search the meaning of a word
def search(enterWordEntry, meaningArea):
    data = json.load(open('data.json'))
    word = enterWordEntry.get().lower()
    if word in data:
        meaning = data[word]
        meaningArea.delete(1.0, tk.END)
        for item in meaning:
            meaningArea.insert(tk.END, u'\u2022' + item + '\n\n')
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('Confirm', f'Did you mean {close_match} instead?')
        if res:
            enterWordEntry.delete(0, tk.END)
            enterWordEntry.insert(tk.END, close_match)
            meaning = data[close_match]
            meaningArea.delete(1.0, tk.END)
            for item in meaning:
                meaningArea.insert(tk.END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error', "The word doesn't exist. Please double check it.")
            enterWordEntry.delete(0, tk.END)
            meaningArea.delete(1.0, tk.END)
    else: 
        messagebox.showinfo('Information', "The word doesn't exist")
        enterWordEntry.delete(0, tk.END)
        meaningArea.delete(1.0, tk.END)


# Function to delete EnterArea and MeaningArea
def clear(enterWordEntry, meaningArea):
    enterWordEntry.delete(0, tk.END)
    meaningArea.delete(1.0, tk.END)


# Function to recognize the voice
def speak(enterWordEntry):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            enterWordEntry.delete(0, tk.END)
            enterWordEntry.insert(tk.END, text)
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError) as e:
            print("Speech Recognition Error")


# Function to suggest words to enter
def suggest(event, enterWordEntry, suggestions_list):
    data = json.load(open('data.json'))
    word = enterWordEntry.get().lower()
    suggestions = [w for w in data.keys() if w.startswith(word)]
    if suggestions:
        suggestions_list.delete(0, tk.END)
        for suggestion in suggestions:
            suggestions_list.insert(tk.END, suggestion)
        suggestions_list.place(x=460, y=127)
    else:
        suggestions_list.place_forget()


# Function to choose a word from suggestions_list
def on_suggestion_select(event, enterWordEntry, suggestions_list, meaningArea):
    selected_word = suggestions_list.get(suggestions_list.curselection())
    enterWordEntry.delete(0, tk.END)
    enterWordEntry.insert(tk.END, selected_word)
    suggestions_list.place_forget()
    search(enterWordEntry, meaningArea)


# Function to exit the app
def iexit(root):
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res:
        root.destroy()
        
# Function to define clicking enter = search button        
def enter_function(event, searchButton):
    searchButton.invoke()
