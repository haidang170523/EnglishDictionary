import tkinter as tk

def setup_gui(root, search, speak, meaningAudio, clear, iexit, suggest, on_suggestion_select):
    # Background
    bgImage = tk.PhotoImage(file='Photos/bg.png')
    bgLabel = tk.Label(root, image=bgImage)
    bgLabel.image = bgImage  # To prevent the image from being garbage collected
    bgLabel.place(x=0, y=0)

    # Enter Word Label
    enterWordLabel = tk.Label(root, text='Enter Word', font=('castellar', 29, 'bold'), foreground='red3', background='whitesmoke')
    enterWordLabel.place(x=530, y=20)

    # Text Field
    enterWordEntry = tk.Entry(root, font=('airal', 23, 'bold'), justify=tk.CENTER, bd=8, relief=tk.GROOVE)
    enterWordEntry.place(x=460, y=80)

    # Suggestions Listbox
    suggestions_list = tk.Listbox(root, font=('arial', 23, 'bold'), width=21, height=3)
    enterWordEntry.bind('<KeyRelease>', lambda event: suggest(event, enterWordEntry, suggestions_list))
    suggestions_list.bind('<<ListboxSelect>>', lambda event: on_suggestion_select(event, enterWordEntry, suggestions_list, meaningArea))

    # Search Button
    searchImage = tk.PhotoImage(file='Photos/search.png')
    searchButton = tk.Button(root, image=searchImage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=lambda: search(enterWordEntry, meaningArea))
    searchButton.image = searchImage
    searchButton.place(x=820, y=72)

    # Mic Button
    micImage = tk.PhotoImage(file='Photos/mic.png')
    micButton = tk.Button(root, image=micImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2', command=lambda: speak(enterWordEntry))
    micButton.image = micImage
    micButton.place(x=890, y=75)

    # Meaning Label
    meaningLabel = tk.Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
    meaningLabel.place(x=580, y=240)

    # Meaning Area
    meaningArea = tk.Text(root, width=34, height=8, font=('arial', 18, 'bold'), bd=8, relief=tk.GROOVE, wrap='word')
    meaningArea.place(x=460, y=300)

    # Audio Button 
    audioImage = tk.PhotoImage(file='Photos/speaker.png')
    audioButton = tk.Button(root, image=audioImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2', command=lambda: meaningAudio(meaningArea))
    audioButton.image = audioImage
    audioButton.place(x=530, y=555)

    # Clear Button
    clearImage = tk.PhotoImage(file='Photos/clear.png')
    clearButton = tk.Button(root, image=clearImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2', command=lambda: clear(enterWordEntry, meaningArea))
    clearButton.image = clearImage
    clearButton.place(x=660, y=555)

    # Exit Button
    exitImage = tk.PhotoImage(file='Photos/exit.png')
    exitButton = tk.Button(root, image=exitImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2', command=lambda: iexit(root))
    exitButton.image = exitImage
    exitButton.place(x=790, y=555)

    return enterWordEntry, suggestions_list, meaningArea, searchButton
