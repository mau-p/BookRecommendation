import tkinter as tk
from tkinter import Text, font
from tkinter.constants import CENTER, DISABLED, INSERT
import questions


def incrementor():
    if hasattr(incrementor, "num"):
        incrementor.num += 1           # increment if not first call
    else:
        incrementor.num = 0         # initialize on first call
    return incrementor.num

# Basic properties for all windows


class Window:
    def __init__(self) -> None:
        self.background_color = "slate gray"
        self.highlight_background = "black"
        self.text_color = "grey99"
        root.configure(bg=self.background_color)
        self.index = incrementor()
        self.window_width = 960
        self.window_height = 600
        self.x_pos = root.winfo_screenwidth()/2 - self.window_width/2
        self.y_pos = root.winfo_screenheight()/2 - self.window_height/2
        self.geometry = root.geometry(
            '%dx%d+%d+%d' % (self.window_width, self.window_height, self.x_pos, self.y_pos))
        self.previous = tk.Button(
            root, text="Previous", bg="red3", activebackground="red", highlightbackground=self.highlight_background, fg=self.text_color,\
                 width=10, command=lambda: self.previous_question())
        self.previous.place(relx=.05, rely=.9)
        self.next = tk.Button(root, text="Next", bg="forest green", activebackground="green yellow", fg=self.text_color, \
            highlightbackground=self.highlight_background, width=10, command=lambda: self.next_question())
        if self.index == questions.get_question_list_length()-1:
            self.next.configure(state=DISABLED)
        self.next.place(relx=.85, rely=.9)

# The window that is displayed when the user first launches the program


class IntroWindow(Window):
    def __init__(self) -> None:
        Window.__init__(self)
        self.title = tk.Label(root, text="Welcome to BookRecommendation!", font=(
            'Arial', 30), bg=self.background_color, fg=self.text_color)
        self.presentation = tk.Label(root, text=("This knowledge system uses expert knowledge to give you a book recommendation. \n"
                                                 "Developed by Matthew Melcherts, Maurits Merks and Julius Wagenbach. \n"),\
                                                      bg=self.background_color, fg=self.text_color, font=("Arial", 12))
        self.presentation.place(relx=.5, rely=.4, anchor=CENTER)
        self.title.place(relx=.5, rely=.3, anchor=CENTER)
        self.previous.configure(state=DISABLED)

    # Retrieves index of next question, and makes a window depending on type
    def next_question(self):
        global app
        self.title.place_forget()
        self.presentation.place_forget()
        _, question = questions.get_next_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text,
                                 question.possible_answers)


# Type of window that asks the user for value (for example their age or a book rating)
class IntegerWindow(Window):
    def __init__(self, question: str) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=question, bg=self.background_color, fg=self.text_color, font=("Arial", 14))
        self.text.place(relx=.5, rely=.3, anchor=CENTER)
        self.entry = tk.Entry(root, width=5, highlightbackground=self.highlight_background, justify=CENTER)
        self.entry.insert(2, 20)
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
            app = CategoryWindow(next_question.question_text,
                                 next_question.possible_answers)
        current_question.answer = int(self.entry.get())

    # Retrieves index of previous question, and makes a window depending on type
    def previous_question(self):
        global app
        self.text.place_forget()
        self.entry.place_forget()
        question = questions.get_previous_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text,
                                 question.possible_answers)
        if question.answer_type == "welcome":
            app = IntroWindow()

# Type of window that shows the user different options to choose from (for example gender, yes/no or reading preferences)


class CategoryWindow(Window):
    def __init__(self, question: str, categories: list) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=question, bg=self.background_color, fg=self.text_color, font=("Arial", 14))
        self.text.place(relx=0.5, rely=.3, anchor=CENTER)
        self.categories = categories
        self.boxes = []
        self.checkbox = tk.IntVar(value=0)
        self.init_checkboxes()

    def init_checkboxes(self):
        for i in range(len(self.categories)):
            self.boxes.append(tk.Checkbutton(
                root, text=self.categories[i], onvalue=i+1, variable=self.checkbox, width=8, height=2, highlightbackground=self.highlight_background, anchor=CENTER))

        if len(self.boxes) == 2:
            self.boxes[0].place(relx=.40, rely=.5)
            self.boxes[1].place(relx=.60, rely=.5)
        elif len(self.boxes) == 3:
            self.boxes[0].place(relx=.26, rely=.5)
            self.boxes[1].place(relx=.46, rely=.5)
            self.boxes[2].place(relx=.67, rely=.5)

    # Retrieves index of next question, and makes a window depending on type
    def next_question(self):
        global app
        self.text.place_forget()
        for box in self.boxes:
            box.place_forget()
        current_question, next_question = questions.get_next_question()
        if self.checkbox.get() == 0:  # Checks if the questions has been answered
            next_question = current_question
            questions.revert_question()
            answer_warning_label = tk.Label(root, text="In order to find your ideal book, we need your answer to this question. \n \
                If you don't know the answer, you can answer neutral in most cases", fg='red')
            answer_warning_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        current_question.answer = self.categories[self.checkbox.get()-1]
        if next_question.answer_type == "value":
            app = IntegerWindow(next_question.question_text)
        if next_question.answer_type == "category":
            app = CategoryWindow(next_question.question_text,
                                 next_question.possible_answers)

    # Retrieves index of previous question, and makes a window depending on type

    def previous_question(self):
        global app
        self.text.place_forget()
        for box in self.boxes:
            box.place_forget()
        question = questions.get_previous_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text,
                                 question.possible_answers)
        if question.answer_type == "welcome":
            app = IntroWindow()


class SummaryWindow(Window):
    def __init__(self, title: str, author: str, summary: str) -> None:
        Window.__init__(self)
        self.question = tk.Label(
            root, text="What do you think about this book?", bg=self.background_color, fg=self.text_color, font =("Arial", 14))
        self.title = tk.Label(root, text=title, font=("Arial", 25), bg=self.background_color, fg=self.text_color)
        self.author = tk.Label(root, text=f'by {author}', bg="green2")
        self.textbox = tk.Text(root, height=13, width=110, wrap=tk.WORD)
        self.textbox.insert(INSERT, summary)
        self.textbox.config(state=DISABLED)
        self.textbox.place(relx=.5, rely=.55, anchor=CENTER)
        self.question.place(relx=.5, rely=.15, anchor=CENTER)
        self.title.place(relx=.5, rely=.25, anchor=CENTER)
        self.author.place(relx=.5, rely=.30, anchor=CENTER)
        self.checkbox = tk.IntVar()
        self.would = tk.Checkbutton(root, text="I would read this", onvalue=1, variable=self.checkbox, width=20, height=2, \
             highlightbackground=self.highlight_background)
        self.would_not = tk.Checkbutton(root, text="I would not read this", onvalue=1, variable=self.checkbox, width=20, height=2, \
             highlightbackground=self.highlight_background)
        self.would_not.place(relx=.25, rely=.75)
        self.would.place(relx=.55, rely=.75)
        

root = tk.Tk()
root.title("Book Recommendation")
app = IntroWindow()
# app = SummaryWindow("This is a title", "Author", "Summary")
root.mainloop()
