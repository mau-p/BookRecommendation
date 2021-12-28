import tkinter as tk
from tkinter.constants import CENTER

class Window:
    def basic_layout(self, root):
        geometry = root.geometry("960x600")
        return geometry

# The window that is displayed when the user first launches the program
class IntroWindow(Window):
    def __init__(self) -> None:
        root.geometry = self.basic_layout(root)
        self.text = tk.Label(root, text=("Welcome to Bookrecommendation! \n \n"
            "This knowledge system uses expert knowledge to give you a book recommendation. \n"
            "Developed by Matthew Melcherts, Maurits Merks and Julius Wagenbach. \n"))
        self.text.place(relx=.5, rely=.3, anchor=CENTER)


# Type of window that asks the user for value (for example their age or a book rating)
class IntegerWindow(Window):
    def __init__(self, question: str) -> None:
        root.geometry = self.basic_layout(root)
        self.text = tk.Label(root, text= question)
        self.text.place(relx=.5, rely=.3, anchor=CENTER)
        self.entry = tk.Entry(root, width=3)
        self.entry.place(relx=.5, rely=.5, anchor=CENTER)

# Type of window that shows the user different options to choose from (for example gender, yes/no or reading preferences)
class CategoryWindow(Window):
    def __init__(self, question: str, categories: list) -> None:
        root.geometry = self.basic_layout(root)
        self.text = tk.Label(root, text= question)
        self.text.place(relx=0.5, rely=.3, anchor=CENTER)
        self.categories = categories
        self.category_variables = [tk.IntVar]*len(categories)
        self.boxes = []
        self.create_checkboxes()
        self.place_checkboxes()

    def create_checkboxes(self):
        for category, category_variable in zip(self.categories, self.category_variables):
            self.boxes.append(tk.Checkbutton(root, text=category, variable=category_variable))

    # This is terrible, but havent found a better way for now    
    def place_checkboxes(self):
        if len(self.boxes) == 2:
            self.boxes[0].place(relx=.40, rely=.5)
            self.boxes[1].place(relx=.60, rely=.5)
        elif len(self.boxes) == 3:
            self.boxes[0].place(relx=.35, rely=.5)
            self.boxes[1].place(relx=.45, rely=.5)
            self.boxes[2].place(relx=.55, rely=.5)
        elif len(self.boxes) == 8:
            self.boxes[0].place(relx=.20, rely=.5)
            self.boxes[1].place(relx=.40, rely=.5)
            self.boxes[2].place(relx=.60, rely=.5)
            self.boxes[3].place(relx=.80, rely=.5)
            self.boxes[4].place(relx=.20, rely=.6)
            self.boxes[5].place(relx=.40, rely=.6)
            self.boxes[6].place(relx=.60, rely=.6)
            self.boxes[7].place(relx=.80, rely=.6)

root = tk.Tk()
root.title("Book Recommendation")
app = IntroWindow()
root.mainloop()