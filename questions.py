
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
                        "Disagree", "Neutral", "Agree"])
like_simple_narratives = Question("Complex narratives with many subplots are often too complicate for me to enjoy", "category", [
                                  "Disagree", "Neutral", "Agree"])
reading_task = Question("I dont like it if reading feels like a task", "category", [
                        "Disagree", "Neutral", "Agree"])
regular_reader = Question("I consider myself a regular reader", "category", [
                          "Disagree", "Neutral", "Agree"])
read_more = Question("I would like to read more books then I currently do", "category", [
    "Disagree", "Neutral", "Agree"])
humor = Question("I dont mind if a book does not have humoristic elements", "category", [
    "Disagree", "Neutral", "Agree"])
comedy_v_drama = Question("I generally like comedy over drama", "category", [
                          "Disagree", "Neutral", "Agree"])
happy_ending = Question("I generally prefer it if stories have a happy ending", "category", [
    "Disagree", "Neutral", "Agree"])
relax = Question("A main reason I like to read is because it helps me to relax and unwind", "category", [
    "Disagree", "Neutral", "Agree"])
challenge = Question("I like it if books feel like a challenge", "category", [
    "Disagree", "Neutral", "Agree"])
social_issues = Question("I often think about social issues", "category", [
    "Disagree", "Neutral", "Agree"])
history = Question("I generally enjoy history", "category", [
    "Disagree", "Neutral", "Agree"])
intense = Question("I like intense stories", "category", [
    "Disagree", "Neutral", "Agree"])
own_life = Question("I prefer books with stories that are similar to my own life", "category", [
    "Disagree", "Neutral", "Agree"])
leisure_pace = Question("I prefer reading at a leisurely pace", "category", [
    "Disagree", "Neutral", "Agree"])
real_world = Question("I like books that make me reflect upon the real world", "category", [
    "Disagree", "Neutral", "Agree"])
mysteries = Question("I enjoy it when there are mysteries in the plot", "category", [
    "Disagree", "Neutral", "Agree"])
romantic = Question("I would consider myself a romantic person", "category", [
    "Disagree", "Neutral", "Agree"])
finishing = Question("I don't like not finishing books", "category", [
    "Disagree", "Neutral", "Agree"])
moody = Question("I dont like it if characters are overly moody and sentimental", "category", [
    "Disagree", "Neutral", "Agree"])


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

# Functions for next and previous buttons
question_ref = 1

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
