import tkinter as tk
from tkinter.constants import DISABLED

root = tk.Tk()
root.title("Bookrecommendation")

root.grid()

text0 = ("Welcome to Bookrecommendation! \n \n"
"This knowledge system uses expert knowledge to give you a book recommendation. \n"
"Developed by Matthew Melcherts, Maurits Merks and Julius Wagenbach. \n"
"With expert knowledge from ... \n")
text1 = ("text1")
text2 = ("text2")
text3 = ("text3")
text4 = ("text4")

text = tk.Label(root, text=text0)
text.grid(column=0, row=0, columnspan=3, padx=5, pady=(10,0))

progress_list = [text0, text1, text2, text3, text4]

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

    text.grid(column=0, row=0, columnspan=3, padx=5, pady=(10,0))
    button_previous.grid(column=0, row=10, pady=10)
    button_next.grid(column=2, row=10, pady=10)

def next(progress_number):
    global text
    global button_previous
    global button_next
    
    text.grid_forget()
    text = tk.Label(root, text=progress_list[progress_number-1])
    button_previous = tk.Button(root, text="Previous", command=lambda: previous(progress_number-1))
    button_next = tk.Button(root, text="Next", command=lambda: next(progress_number+1))

    if progress_number == 5:
        button_next = tk.Button(root, text="Next", state=DISABLED)

    text.grid(column=0, row=0, columnspan=3, padx=5, pady=(10,0))
    button_previous.grid(column=0, row=10, pady=10)
    button_next.grid(column=2, row=10, pady=10)

button_previous = tk.Button(root, text="Previous", command=previous, state=DISABLED).grid(column=0, row=10, pady=10)
button_quit = tk.Button(root, text="Quit", command=root.quit).grid(column=1, row=10, pady=10)
button_next = tk.Button(root, text="Next", command=lambda: next(2)).grid(column=2, row=10, pady=10)

root.mainloop()

# Not sure how to implement a GUI yet, but that will be figured out. 