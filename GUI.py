import tkinter as tk
from tkinter.constants import CENTER, DISABLED
import questions

global app

# Basic properties for all windows
class Window:
    def __init__(self) -> None:
        self.window_width = 960
        self.widnow_height = 600
        self.x_pos = root.winfo_screenwidth()/2 - self.window_width/2
        self.y_pos = root.winfo_screenheight()/2 - self.widnow_height/2
        self.geometry = root.geometry('%dx%d+%d+%d' % (self.window_width, self.widnow_height, self.x_pos, self.y_pos))
        self.previous = tk.Button(root, text="Previous", command=lambda: self.previous_question()).place(relx=.1, rely=.9)
        self.quit = tk.Button(root, text="Quit", command=lambda: root.quit()).place(relx=.5, rely=.9)
        self.next = tk.Button(root, text="Next", command=lambda: self.next_question()).place(relx=.85, rely=.9)

        
# The window that is displayed when the user first launches the program
class IntroWindow(Window):
    def __init__(self) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=("Welcome to Bookrecommendation! \n \n"
                                         "This knowledge system uses expert knowledge to give you a book recommendation. \n"
                                         "Developed by Matthew Melcherts, Maurits Merks and Julius Wagenbach. \n"))
        self.text.place(relx=.5, rely=.3, anchor=CENTER)
        self.previous = tk.Button(root, text="Previous", state=DISABLED)
        self.previous.place(relx=.1, rely=.9)

    # Retrieves index of next question, and makes a window depending on type
    def next_question(self):
        global app
        self.text.place_forget()
        _,question = questions.get_next_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text, question.possible_answers)


# Type of window that asks the user for value (for example their age or a book rating)
class IntegerWindow(Window):
    def __init__(self, question: str) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=question)
        self.text.place(relx=.5, rely=.3, anchor=CENTER)
        self.entry = tk.Entry(root, width=3)
        self.entry.place(relx=.5, rely=.5, anchor=CENTER)

    # Retrieves index of next question, and makes a window depending on type
    def next_question(self):
        global app
        self.text.place_forget()
        self.entry.place_forget()
        current_question, next_question = questions.get_next_question()
        if next_question.answer_type == "value":
            app = IntegerWindow(next_question.question_text)
        if next_question.answer_type == "category":
            app = CategoryWindow(next_question.question_text, next_question.possible_answers)
        current_question.answer = self.entry.get()

    # Retrieves index of previous question, and makes a window depending on type  
    def previous_question(self):
        global app
        self.text.place_forget()
        self.entry.place_forget()
        _,question = questions.get_previous_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text, question.possible_answers)
        if question.answer_type == "welcome":
            app = IntroWindow()

# Type of window that shows the user different options to choose from (for example gender, yes/no or reading preferences)
class CategoryWindow(Window):
    def __init__(self, question: str, categories: list) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=question)
        self.text.place(relx=0.5, rely=.3, anchor=CENTER)
        self.categories = categories
        self.category_variables = []
        self.boxes = []
        self.set_category_variables()
        self.create_checkboxes()
        self.place_checkboxes()

    # Creates an tk.IntVar for each variable, (gets set to 1 if checked)
    def set_category_variables(self):
        for i in range(len(self.categories)):
            self.category_variables.append(tk.IntVar())

    def create_checkboxes(self):
        for category, category_variable in zip(self.categories, self.category_variables):
            self.boxes.append(tk.Checkbutton(
                root, text=category, variable=category_variable))

    # This is terrible, but havent found a better way for now
    def place_checkboxes(self):
        if len(self.boxes) == 2:
            self.boxes[0].place(relx=.40, rely=.5)
            self.boxes[1].place(relx=.60, rely=.5)
        elif len(self.boxes) == 3:
            self.boxes[0].place(relx=.35, rely=.5)
            self.boxes[1].place(relx=.45, rely=.5)
            self.boxes[2].place(relx=.55, rely=.5)
        elif len(self.boxes) == 4:
            self.boxes[0].place(relx=.20, rely=.5)
            self.boxes[1].place(relx=.40, rely=.5)
            self.boxes[2].place(relx=.60, rely=.5)
            self.boxes[3].place(relx=.80, rely=.5)
        elif len(self.boxes) == 8:
            self.boxes[0].place(relx=.20, rely=.5)
            self.boxes[1].place(relx=.40, rely=.5)
            self.boxes[2].place(relx=.60, rely=.5)
            self.boxes[3].place(relx=.80, rely=.5)
            self.boxes[4].place(relx=.20, rely=.6)
            self.boxes[5].place(relx=.40, rely=.6)
            self.boxes[6].place(relx=.60, rely=.6)
            self.boxes[7].place(relx=.80, rely=.6)

    # Retrieves index of next question, and makes a window depending on type
    def next_question(self):
        global app
        self.text.place_forget()
        for box in self.boxes:
            box.place_forget()
        current_question, next_question = questions.get_next_question()
        if next_question.answer_type == "value":
            app = IntegerWindow(next_question.question_text)
        if next_question.answer_type == "category":
            app = CategoryWindow(next_question.question_text, next_question.possible_answers)
        self.store_result(current_question)

    
    # Retrieves index of previous question, and makes a window depending on type
    def previous_question(self):
        global app
        self.text.place_forget()
        for box in self.boxes:
            box.place_forget()
        _,question = questions.get_previous_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text, question.possible_answers)
        if question.answer_type == "welcome":
            app = IntroWindow()

    # Goes through each of the box variables, if it is 1 (True), it appends the corresponding category to the result.
    def store_result(self, question):
        results = []
        for i in range(len(self.category_variables)):
            if self.category_variables[i].get() == 1:
                results.append(self.categories[i])
        question.answer = results
        
def launch_GUI():
    return IntroWindow()


root = tk.Tk()
root.title("Book Recommendation")
app = launch_GUI()
root.mainloop()
