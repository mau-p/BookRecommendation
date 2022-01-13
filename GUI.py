import tkinter as tk
from tkinter.constants import CENTER, DISABLED, INSERT, TOP
import bookmanagement
import rules
import bookselect
from quizmaster import quizmaster
cursor = bookmanagement.get_cursor()

# Basic properties for all windows
class Window:
    def __init__(self) -> None:
        self.background_color = "slate gray"
        self.highlight_background = "black"
        self.text_color = "grey99"
        root.configure(bg=self.background_color)
        self.window_width = 960
        self.window_height = 600
        self.x_pos = root.winfo_screenwidth()/2 - self.window_width/2
        self.y_pos = root.winfo_screenheight()/2 - self.window_height/2
        self.geometry = root.geometry(
            '%dx%d+%d+%d' % (self.window_width, self.window_height, self.x_pos, self.y_pos))
        self.previous = tk.Button(
            root, text="Previous", bg="red3", activebackground="red", highlightbackground=self.highlight_background,
            fg=self.text_color, width=10, command=lambda: self.go_back())
        self.previous.place(relx=.05, rely=.9)
        self.next = tk.Button(root, text="Next", bg="forest green", activebackground="green yellow", fg=self.text_color,
                              highlightbackground=self.highlight_background, width=10, command=lambda: self.next_slide())
        self.next.place(relx=.85, rely=.9)
        self.no_answer_label1 = tk.Label(
            root, text="In order to find your ideal book, we need your answer to this question", fg='red', font=("Arial", 15))

    def move_on(self, next_question, no_answer):
        global app
        global progress_var
        self.next.destroy()
        self.previous.destroy()
        progress_var += 1
        if next_question.answer_type == "value":
            app = IntegerWindow(next_question.question_text, no_answer)
        elif next_question.answer_type == "category":
            app = CategoryWindow(next_question.question_text,
                                 next_question.possible_answers, no_answer)
        elif next_question.answer_type == "knowledgebase":
            q_list = quizmaster.get_questions()
            preferences = rules.initialise_knowledge_base(q_list)
            bookselect.get_recommendations(preferences)
            app = KnowledgeBaseWindow()
        elif next_question.answer_type == "summarywindow":
            app = SummaryWindow(next_question.possible_answers, no_answer)
        elif next_question.answer_type == "suggestion":
            app = SuggestionWindow(int(next_question.possible_answers))

    def go_back(self):
        global app
        global progress_var
        self.destroy_window()
        progress_var -= 1
        question = quizmaster.get_previous_question()
        if question.answer_type == "value":
            app = IntegerWindow(question.question_text, False)
        if question.answer_type == "category":
            app = CategoryWindow(question.question_text,
                                 question.possible_answers, False)
        elif question.answer_type == "welcome":
            app = IntroWindow()
        elif question.answer_type == "knowledgebase":
            quizmaster.pop_possible_last_books()
            app = KnowledgeBaseWindow()
        elif question.answer_type == "summarywindow":
            quizmaster.pop_possible_last_books()
            app = SummaryWindow(question.possible_answers, False)
        elif question.answer_type == "suggestion":
            app = SuggestionWindow(int(question.possible_answers))

    def check_answer(self, wrong_answer: bool, current_question, next_question):
        global progress_var
        if wrong_answer:
            no_answer = True
            next_question = current_question
            progress_var -= 1
            quizmaster.revert_question()
        else:
            no_answer = False
        return next_question, no_answer


# The window that is displayed when the user first launches the program
class IntroWindow(Window):
    def __init__(self) -> None:
        Window.__init__(self)
        self.title = tk.Label(root, text="Welcome to BookRecommendation!", font=(
            'Arial', 30), bg=self.background_color, fg=self.text_color)
        self.presentation = tk.Label(root, text=("This knowledge system uses expert knowledge to give you a book recommendation. \n"
                                                 "Developed by Matthew Melcherts, Maurits Merks and Julius Wagenbach. \n"),
                                     bg=self.background_color, fg=self.text_color, font=("Arial", 12))
        self.presentation.place(relx=.5, rely=.4, anchor=CENTER)
        self.title.place(relx=.5, rely=.3, anchor=CENTER)
        self.previous.configure(state=DISABLED)

    # Retrieves index of next question, and makes a window depending on type
    def next_slide(self):
        self.title.destroy()
        self.presentation.destroy()
        _, question = quizmaster.get_next_question()
        self.move_on(question, False)


# Type of window that asks the user for value (for example their age or a book rating)
class IntegerWindow(Window):
    def __init__(self, question: str, no_answer: bool) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=question, bg=self.background_color,
                             fg=self.text_color, font=("Arial", 14))
        self.text.place(relx=.5, rely=.3, anchor=CENTER)
        self.entry = tk.Entry(
            root, width=5, highlightbackground=self.highlight_background, justify=CENTER)
        self.entry.insert(2, 20)
        self.entry.place(relx=.5, rely=.5, anchor=CENTER)
        string = 'Question', progress_var, ' of 19'
        self.progress = tk.Label(root, text= string, bg=self.background_color,
                            fg=self.text_color, font=("Arial", 14))
        self.progress.place(relx=.45, rely=.9)
        if no_answer:
            self.no_answer_label1.pack(side=TOP)

    def destroy_window(self):
        self.text.destroy()
        self.progress.destroy()
        self.entry.destroy()
        self.no_answer_label1.destroy()

    # Retrieves index of next question, and makes a window depending on type
    def next_slide(self):
        current_question, next_question = quizmaster.get_next_question()
        current_question.answer = int(self.entry.get())
        next_question, no_answer = self.check_answer(current_question.answer < 0 or type(
            current_question.answer) is not int, current_question, next_question)
        self.destroy_window()
        self.move_on(next_question, no_answer)


# Type of window that shows the user different options to choose from (for example gender, yes/no or reading preferences)
class CategoryWindow(Window):
    def __init__(self, question: str, categories: list, no_answer: bool) -> None:
        Window.__init__(self)
        self.text = tk.Label(root, text=question, bg=self.background_color,
                             fg=self.text_color, font=("Arial", 14))
        self.text.place(relx=0.5, rely=.3, anchor=CENTER)
        self.categories = categories
        self.boxes = []
        self.checkbox = tk.IntVar(value=0)
        self.init_checkboxes()
        string = 'Question', progress_var, ' of 19'
        self.progress = tk.Label(root, text= string, bg=self.background_color,
                            fg=self.text_color, font=("Arial", 14))
        self.progress.place(relx=.45, rely=.9)
        if no_answer:
            self.no_answer_label1.pack(side=TOP)

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

    def destroy_window(self):
        self.text.destroy()
        self.progress.destroy()
        self.no_answer_label1.pack_forget()
        for box in self.boxes:
            box.destroy()

    # Retrieves index of next question, and makes a window depending on type
    def next_slide(self):
        self.destroy_window()
        current_question, next_question = quizmaster.get_next_question()
        current_question.answer = self.categories[self.checkbox.get()-1]
        next_question, no_answer = self.check_answer(
            self.checkbox.get() == 0, current_question, next_question)
        self.move_on(next_question, no_answer)


# Window after category questions, explains final summary part and initialises database
class KnowledgeBaseWindow(Window):
    def __init__(self) -> None:
        Window.__init__(self)
        self.title = tk.Label(root, text="BookRecommendation is about to recommend some books!", font=(
            'Arial', 25), bg=self.background_color, fg=self.text_color)
        self.presentation = tk.Label(root, text=("Based on your answers BookRecommendation will show you a few books with their summaries. \n"
                                                 "Please read the summary and judge whether you would read this book or not. \n"),
                                     bg=self.background_color, fg=self.text_color, font=("Arial", 12))
        self.presentation.place(relx=.5, rely=.4, anchor=CENTER)
        self.title.place(relx=.5, rely=.3, anchor=CENTER)
        self.previous.configure(state=DISABLED)

    # Retrieves index of next question, and makes a window depending on type
    def next_slide(self):
        self.title.destroy()
        self.presentation.destroy()
        _, question = quizmaster.get_next_question()
        self.move_on(question, False)


# Window used in the final stage where user is presented with a few options
class SummaryWindow(Window):
    def __init__(self, ID, no_answer:bool) -> None:
        Window.__init__(self)
        self.book_ID = ID
        book = bookmanagement.get_book(cursor, ID)
        book_title = book[0]
        book_author = book[1]
        summary = book[3]
        self.question = tk.Label(
            root, text="What do you think about this book?", bg=self.background_color, fg=self.text_color, font=("Arial", 14))
        self.title = tk.Label(root, text=book_title, font=(
            "Arial", 25), bg=self.background_color, fg=self.text_color)
        self.author = tk.Label(root, text=f'by {book_author}', bg="green2")
        self.textbox = tk.Text(root, height=13, width=110, wrap=tk.WORD)
        self.textbox.insert(INSERT, summary)
        self.textbox.config(state=DISABLED)
        self.textbox.place(relx=.5, rely=.55, anchor=CENTER)
        self.question.place(relx=.5, rely=.15, anchor=CENTER)
        self.title.place(relx=.5, rely=.25, anchor=CENTER)
        self.author.place(relx=.5, rely=.30, anchor=CENTER)
        self.checkbox = tk.IntVar()
        self.would = tk.Checkbutton(root, text="I would read this", onvalue=1, variable=self.checkbox, width=20, height=2,
                                    highlightbackground=self.highlight_background)
        self.would_not = tk.Checkbutton(root, text="I would not read this", onvalue=-1, variable=self.checkbox, width=20, height=2,
                                        highlightbackground=self.highlight_background)
        self.would_not.place(relx=.25, rely=.75)
        self.would.place(relx=.55, rely=.75)
        if no_answer:
            self.no_answer_label1.pack(side=TOP)

    def destroy_window(self):
        self.question.destroy()
        self.title.destroy()
        self.textbox.destroy()
        self.would.destroy()
        self.would_not.destroy()
        self.author.destroy()
        self.no_answer_label1.pack_forget()

    def next_slide(self):
        self.destroy_window()
        if self.checkbox.get() == 1:
            quizmaster.possible_last_books(self.book_ID)
        current_question, next_question = quizmaster.get_next_question()
        if current_question == next_question:
            quizmaster.append_last_book()
            current_question, next_question = quizmaster.get_next_question()
        next_question, no_answer = self.check_answer(
            self.checkbox.get() == 0, current_question, next_question)
        self.move_on(next_question, no_answer)

# Final window, the user is presented with their ideal book


class SuggestionWindow(Window):
    def __init__(self, ID) -> None:
        Window.__init__(self)
        if ID == 0:
            self.book_title = '-'
            self.book_author = '-'
            self.book_ISBN = '-'
            self.summary = ' '
            string = "No book suited your interests, maybe try again!"
            inference = "-"
        else:
            book = bookmanagement.get_book(cursor, ID)
            self.book_title = book[0]
            self.book_author = book[1]
            self.book_ISBN = book[2]
            self.summary = book[3]
            string = "Say hi to your next favorite book!"

            # Inference part, tells user which categories they liked and what the recommendation was based on
            book_categories = bookmanagement.get_properties(cursor, ID)
            inference = "" 
            q_list = quizmaster.get_questions()
            preferences = rules.initialise_knowledge_base(q_list)
            categories = ["(Entertaining) ", "(Suspense) ", "(Romantic) ", "(Historic) ", "(Feel good) ", 
                            "(Funny) ", "(Gripping) ", "(Sad) ", "(Social) "]
            if book_categories[0] == q_list[2].answer:
                inference += "(Gender) "
            if book_categories[1] <= q_list[1].answer:
                inference += "(Age) "
            if book_categories[2]-2 <= preferences[0]:
                inference += "(Reading level) "
            for i in range(1, len(preferences)):
                if preferences[i] == 1 and book_categories[i+2] == 1:
                    inference += categories[i-1]
            inference = "The recommendation was based on the inference of the following:\n" + inference

        self.title = tk.Label(root, text=self.book_title, font=(
            "Arial", 25), bg=self.background_color, fg=self.text_color)
        self.question = tk.Label(
            root, text=string, bg=self.background_color, fg=self.text_color, font=("Arial", 18))
        self.author = tk.Label(
            root, text=f'by {self.book_author}', bg="green3")
        self.ISBN = tk.Label(root, text=f'ISBN: {self.book_ISBN}', fg=self.text_color,
                             bg=self.background_color, width=20, font=("Arial", 12))
        self.infer = tk.Label(root, text=(inference), fg=self.text_color, bg=self.background_color, font=("Arial", 12))
        self.textbox = tk.Text(root, height=13, width=110, wrap=tk.WORD)
        self.textbox.insert(INSERT, self.summary)
        self.textbox.config(state=DISABLED)
        self.textbox.place(relx=.5, rely=.7, anchor=CENTER)
        self.question.place(relx=.5, rely=.15, anchor=CENTER)
        self.title.place(relx=.5, rely=.25, anchor=CENTER)
        self.author.place(relx=.5, rely=.30, anchor=CENTER)
        self.ISBN.place(relx=.41, rely=.35)
        self.infer.place(relx=.5, rely=.42, anchor=CENTER)
        self.quit = tk.Button(root, text="Done", bg="red3", activebackground="red", highlightbackground=self.highlight_background, fg=self.text_color,
                              width=10, command=lambda: quit())
        self.quit.place(relx=.45, rely=.9)
        self.next.destroy()
        self.previous.destroy()


def launch_GUI():
    global root
    global app
    global progress_var
    progress_var = 0
    root = tk.Tk()
    root.title("Book Recommendation")
    app = IntroWindow()
    root.mainloop()
