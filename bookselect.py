import bookmanagement
from quizmaster import quizmaster

def get_recommendations(preferences):

    cursor = bookmanagement.get_cursor()
    scores = []

    question_list = quizmaster.get_questions()


    for ID in range(1,bookmanagement.count_books(cursor)+1):
        score = 0
        properties = bookmanagement.get_properties(cursor, ID)
        #gender 
        if question_list[2].answer == properties[0] or question_list[2].answer == "other" or properties[0] == "A":
            score+=1
        else: 
            score-=1
        #age 
        if question_list[1].answer >= properties[1]:
            score+=1
        else:
            score-=1
        #reading level 
        if properties[2]-2 <= preferences[0]: 
            score+=1
        else:
            score-=1
        for index in range(2, len(properties)):
            if properties[index] == 1 and preferences[index-2] == 1:
                score += 1
            elif properties[index] == 0 and preferences[index-2] == -1:
                score -= 1
        scores.append((score, ID))

    scores.sort(key=lambda x: x[0], reverse=True)
    scores = scores[0:3]
    quizmaster.append_recommendations([x[1] for x in scores])
