cursor = get_cursor() 
preferences = [-1,0,1,0,1,0,1,1,0,1] #has to get the real thing
scores = []
for id in range(1,count_entries(cursor)+1):
    score = 0
    #gender 
    if question_list[2].answer is get_properties(cursor, id)[0] or question_list[2].answer is "other" or get_properties(cursor, id)[0] is "A":
        score+=1 
    #age 
    if question_list[1].answer >= get_properties(cursor, id)[1]:
        score+=1
    #reading level 
    if get_properties(cursor, id)[2]-2 <= preferences[0]: 
        score+=1
    #entertaining 
    if get_properties(cursor, id)[3] is 1 and preferences[1] is 1: 
        score+=1
    #suspense 
    if get_properties(cursor, id)[4] is 1 and preferences[2] is 1: 
        score+=1
    #romantic 
    if get_properties(cursor, id)[5] is 1 and preferences[3] is 1: 
        score+=1
    #historic 
    if get_properties(cursor, id)[6] is 1 and preferences[4] is 1: 
        score+=1
    #feelgood 
    if get_properties(cursor, id)[7] is 1 and preferences[5] is 1: 
        score+=1
    #funny 
    if get_properties(cursor, id)[8] is 1 and preferences[6] is 1: 
        score+=1
    #gripping 
    if get_properties(cursor, id)[9] is 1 and preferences[7] is 1: 
        score+=1
    #sad 
    if get_properties(cursor, id)[10] is 1 and preferences[8] is 1: 
        score+=1
    #social
    if get_properties(cursor, id)[11] is 1 and preferences[9] is 1: 
        score+=1

    scores[i-1] = (score, id)
scores = scores.sort()

#ask confirmation questions for the top three books
#missing: a way for the interface to show the description of the book in question
question_list.append(Question("Would you see yourself liking this king of story?", "category",["Yes","Neutral", "No"] ))
question_list.append(Question("Would you see yourself liking this king of story?", "category",["Yes","Neutral", "No"] ))
question_list.append(Question("Would you see yourself liking this king of story?", "category",["Yes","Neutral", "No"] ))

    