from questions import Question


class Quizmaster:
    def __init__(self) -> None:
        self.final_books = []
        self.question_ref = 1
        self.question_list = Question.initialize_questions()

    def append_recommendations(self, options: list):
        for option in options:
            self.question_list.append(Question(None, 'summarywindow', option))

    def append_last_book(self):
        if len(self.final_books) < 1:
            self.question_list.append(Question(None, "suggestion", 0))
        else:
            self.question_list.append(
                Question(None, "suggestion", self.final_books[0]))
    
    def pop_possible_last_books(self):
        if len(self.final_books) > 0:
            self.final_books.pop()

    def possible_last_books(self, ID):
        self.final_books.append(ID)

    def revert_question(self):
        self.question_ref -= 1

    def get_questions(self):
        return self.question_list

    def get_next_question(self):
        self.question_ref += 1
        try:
            return self.question_list[self.question_ref-2], self.question_list[self.question_ref-1]
        except IndexError:
            self.question_ref -= 1
            return self.question_list[self.question_ref-2], self.question_list[self.question_ref-2]

    def get_previous_question(self):
        self.question_ref -= 1
        return self.question_list[self.question_ref-1]


quizmaster = Quizmaster()
