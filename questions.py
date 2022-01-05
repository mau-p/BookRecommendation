
class Question:
    def __init__(self, question_text, answer_type, possible_answers):
        self.question_text = question_text  # The actual question
        self.answer_type = answer_type      # The type of answer for the question
        # If category: the possible answer categories
        self.possible_answers = possible_answers
        self.answer = None  # The answer to the question

def initialize_questions():
    global question_list
    question_list=[]
    question_list.append(Question(None, "welcome", None))
    question_list.append(Question("How old are you?", "value", None))
    question_list.append(Question("I am a", "category", ["Man", "Neutral", "Woman"]))
    question_list.append(Question("I enjoy complex language", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("Complex narratives with many subplots are often too complicate for me to enjoy", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I dont like it if reading feels like a task", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I dont mind if a book does not have humoristic elements", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I generally like comedy over drama", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I generally prefer it if stories have a happy ending", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("A main reason I like to read is because it helps me to relax and unwind", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I often think about social issues", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I generally enjoy history", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I like intense stories", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I prefer books with stories that are similar to my own life", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I like books that make me reflect upon the real world", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I enjoy it when there are mysteries in the plot", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I would consider myself a romantic person", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I like the feeling of having not being able to stop reading", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append( Question("I don't like not finishing books", "category", [
                        "Disagree", "Neutral", "Agree"]))
    question_list.append(Question("I dont like it if characters are overly moody and sentimental", "category", [
                        "Disagree", "Neutral", "Agree"]))

# Functions for next and previous buttons
question_ref = 1

def revert_question():
    global question_ref
    question_ref -=1

def get_question_list_length():
    return len(question_list)

def get_next_question():
    global question_ref
    question_ref += 1
    # returns current and next question
    return question_list[question_ref-2], question_list[question_ref-1]


def get_previous_question():
    global question_ref
    question_ref -= 1
    return question_list[question_ref-1]
