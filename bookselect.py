import bookmanagement
import questions

def get_best_books():

    cursor = bookmanagement.get_cursor()
    preferences = [-1,0,1,0,1,0,1,1,0,1] #has to get the real thing
    scores = []

    question_list = questions.get_question_list()


    for ID in range(1,bookmanagement.count_entries(cursor)+1):
        score = 0
        properties = bookmanagement.get_properties(cursor, ID)
        #gender 
        if question_list[2].answer == properties[0] or question_list[2].answer == "other" or properties[0] == "A":
            score+=1 
        #age 
        if question_list[1].answer >= properties[1]:
            score+=1
        #reading level 
        if properties[2]-2 <= preferences[0]: 
            score+=1

        for index in range(2, len(properties)):
            if properties[index] == preferences[index]:
                score += 1

        scores.append((score, ID))

    scores.sort(key=lambda x: x[0], reverse=True)

    return [scores[0](1), scores[1](1), scores[2](1)]

    #ask confirmation questions for the top three books
    #missing: a way for the interface to show the description of the book in question
    # question_list.append(Question("Would you see yourself liking this kind of story?", "category",["Yes","Neutral", "No"] ))
    # question_list.append(Question("Would you see yourself liking this kind of story?", "category",["Yes","Neutral", "No"] ))
    # question_list.append(Question("Would you see yourself liking this kind of story?", "category",["Yes","Neutral", "No"] ))


