import tkinter as tk
from tkinter.constants import DISABLED

root = tk.Tk()
root.title("Bookrecommendation")

root.grid()
root.geometry('960x600')

text0 = ("Welcome to Bookrecommendation! \n \n"
"This knowledge system uses expert knowledge to give you a book recommendation. \n"
"Developed by Matthew Melcherts, Maurits Merks and Julius Wagenbach. \n")
text1 = ("How old are you?")
text2 = ("What is your gender?")
text3 = ("What is your reading level?")
text4 = ("text4")

text = tk.Label(root, text=text0)
text.place(relx=.5, rely=.3, anchor='center')

progress_list = [text0, text1, text2, text3, text4]

def place_buttons():
    text.place(relx=.5, rely=.3, anchor='center')
    button_previous.place(relx=.1, rely=.9, anchor='center')
    button_next.place(relx=.9, rely=.9, anchor='center')

def previous(progress_number):
    global text
    global button_previous
    global button_next

    text.grid_forget()
    text = tk.Label(root, text=progress_list[progress_number-1])
    button_previous = tk.Button(root, text="Previous", command=lambda: previous(progress_number-1))
    button_next = tk.Button(root, text="Next", command=lambda: next(progress_number+1))

    if progress_number == 1:
        button_previous = tk.Button(root, text="Previous", state=DISABLED)
    
    place_buttons()

def next(progress_number):
    global text
    global button_previous
    global button_next

    text.place_forget()
    text = tk.Label(root, text=progress_list[progress_number-1])
    button_previous = tk.Button(root, text="Previous", command=lambda: previous(progress_number-1))
    button_next = tk.Button(root, text="Next", command=lambda: next(progress_number+1))

    if progress_number == len(progress_list):
        button_next = tk.Button(root, text="Next", state=DISABLED)

    place_buttons()

button_previous = tk.Button(root, text="Previous", command=previous, state=DISABLED).place(relx=.1, rely=.9, anchor='center')
button_quit = tk.Button(root, text="Quit", command=root.quit).place(relx=.5, rely=.9, anchor='center')
button_next = tk.Button(root, text="Next", command=lambda: next(2)).place(relx=.9, rely=.9, anchor='center')

root.mainloop()