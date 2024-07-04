import tkinter as tk
import functions as f
import gui

# Initialize Tkinter
root = tk.Tk()

# Setup GUI
enterWordEntry, suggestions_list, meaningArea, searchButton = gui.setup_gui(root, f.search, f.speak, f.meaningAudio, f.clear, f.iexit, f.suggest, f.on_suggestion_select)

# Binding Enter key to search function
root.bind('<Return>', lambda event: f.enter_function(event, searchButton))

# Frame
root.geometry('1000x626+100+30')
root.title('English Dictionary')
root.resizable(False, False)

# Main loop
if __name__ == '__main__':
    root.mainloop()
