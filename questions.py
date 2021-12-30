
class Question:
    def __init__(self, question_text, answer_type, possible_answers):
        self.question_text = question_text  # The actual question
        self.answer_type = answer_type      # The type of answer for the question
        self.possible_answers = possible_answers # If category: the possible answer categories
        self.answer = None # The answer to the question


# Not an ideal implementation, but does for now
welcome = Question(None, "welcome", None)
age_question = Question("How old are you?", "value", None)
gender_question = Question("I am a", "category", ["Man", "Woman"])
readinglevel_question = Question("What is your reading level?", "category", ["average", "good", "excellent"])


question_list = []
question_list.append(welcome)
question_list.append(age_question)
question_list.append(gender_question)
question_list.append(readinglevel_question)

# Functions for next and previous buttons
question_ref = 1
def get_next_question():
    global question_ref
    question_ref += 1
    return question_list[question_ref-2], question_list[question_ref-1] #returns current and next question

def get_previous_question():
    global question_ref
    question_ref -= 1
    return question_list[question_ref-1]
