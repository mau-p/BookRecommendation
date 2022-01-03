
class Question:
    def __init__(self, question_text, answer_type, possible_answers):
        self.question_text = question_text  # The actual question
        self.answer_type = answer_type      # The type of answer for the question
        # If category: the possible answer categories
        self.possible_answers = possible_answers
        self.answer = None  # The answer to the question


# Not an ideal implementation, but does for now
welcome = Question(None, "welcome", None)
age_question = Question("How old are you?", "value", None)
gender_question = Question("I am a", "category", ["Man", "Woman"])
like_complex = Question("I enjoy complex language", "category", [
                        "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
like_simple_narratives = Question("Complex narratives with many subplots are often too complicate for me to enjoy", "category", [
                                  "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
reading_task = Question("I dont like it if reading feels like a task", "category", [
                        "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
regular_reader = Question("I consider myself a regular reader", "category", [
                          "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
read_more = Question("I would like to read more books then I currently do", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
humor = Question("I dont mind if a book does not have humoristic elements", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
comedy_v_drama = Question("I generally like comedy over drama", "category", [
                          "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
happy_ending = Question("I generally prefer it if stories have a happy ending", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
relax = Question("A main reason I like to read is because it helps me to relax and unwind", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
challenge = Question("I like it if books feel like a challenge", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
social_issues = Question("I often think about social issues", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
history = Question("I generally enjoy history", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
intense = Question("I like intense stories", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
own_life = Question("I prefer books with stories that are similar to my own life", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
leisure_pace = Question("I prefer reading at a leisurely pace", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
real_world = Question("I like books that make me reflect upon the real world", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
mysteries = Question("I enjoy it when there are mysteries in the plot", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
romantic = Question("I would consider myself a romantic person", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
finishing = Question("I don't like not finishing books", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])
moody = Question("I dont like it if characters are overly moody and sentimental", "category", [
    "Completely disagree", "Mostly disagree", "Mostly agree", "Completely agree"])


# TODO: Find a better implementation of whatever this is.
question_list = []
question_list.append(welcome)
question_list.append(age_question)
question_list.append(gender_question)
question_list.append(like_complex)
question_list.append(like_simple_narratives)
question_list.append(reading_task)
question_list.append(regular_reader)
question_list.append(read_more)
question_list.append(humor)
question_list.append(comedy_v_drama)
question_list.append(happy_ending)
question_list.append(relax)
question_list.append(challenge)
question_list.append(social_issues)
question_list.append(history)
question_list.append(intense)
question_list.append(own_life)
question_list.append(leisure_pace)
question_list.append(real_world)
question_list.append(mysteries)
question_list.append(romantic)
question_list.append(finishing)
question_list.append(moody)


def get_question_list():
    return question_list


# Functions for next and previous buttons
question_ref = 1


def get_next_question():
    global question_ref
    question_ref += 1
    # returns current and next question
    return question_list[question_ref-2], question_list[question_ref-1]


def get_previous_question():
    global question_ref
    question_ref -= 1
    return question_list[question_ref-1]
