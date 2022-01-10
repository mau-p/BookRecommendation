#   converts answers from the questions into something usable for the Knowledge Base
def convert_answers(question_list_from_GUI):

    answers_as_strings = []
    for question in question_list_from_GUI:
        q_text, q_type, q_pos_answer, q_answer = question

        if q_type == "category" and q_text != "I am a": #python does not have switch statements.exe
            if q_text == "I enjoy complex language":
                string = "like_complex "
            elif q_text == "Complex narratives with many subplots are often too complicate for me to enjoy":
                string = "like_simple_narratives "
            elif q_text == "I dont like it if reading feels like a task":
                string = "reading_task "
            elif q_text == "I dont mind if a book does not have humoristic elements":
                string = "humor "
            elif q_text == "I generally like comedy over drama":
                string = "comedy_v_drama "
            elif q_text == "I generally prefer it if stories have a happy ending":
                string = "happy_ending "
            elif q_text == "A main reason I like to read is because it helps me to relax and unwind":
                string = "relax "
            elif q_text == "I often think about social issues":
                string = "social_issues "
            elif q_text == "I generally enjoy history":
                string = "history "
            elif q_text == "I like intense stories":
                string = "intense "
            elif q_text == "I prefer books with stories that are similar to my own life":
                string = "own_life "
            elif q_text == "I like books that make me reflect upon the real world":
                string = "real_world "
            elif q_text == "I enjoy it when there are mysteries in the plot":
                string = "mysteries "
            elif q_text == "I would consider myself a romantic person":
                string = "romantic "
            elif q_text == "I like the feeling of not being able to stop reading":
                string = "keep_reading "
            elif q_text == "I don't like not finishing books":
                string = "finishing "
            elif q_text == "I dont like it if characters are overly moody and sentimental":
                string = "moody "

            string += q_answer
            answers_as_strings.append(string)
    
    return answers_as_strings

# Create an array of -1's, 0's and 1's (indicating which categories 
# are preferred) from the categories list  
def array_from_categories(KB):

    category_array = []
    if "ReadingCompetence" in KB["categories"]:
        category_array.append(1)
    elif "!ReadingCompetence" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)
    
    if "Entertaining" in KB["categories"]:
        category_array.append(1)
    elif "!Entertaining" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "Suspense" in KB["categories"]:
        category_array.append(1)
    elif "!Suspense" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)
    
    if "Romantic" in KB["categories"]:
        category_array.append(1)
    elif "!Romantic" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "Historic" in KB["categories"]:
        category_array.append(1)
    elif "!Historic" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "FeelGood" in KB["categories"]:
        category_array.append(1)
    elif "!FeelGood" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "Funny" in KB["categories"]:
        category_array.append(1)
    elif "!Funny" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "Gripping" in KB["categories"]:
        category_array.append(1)
    elif "!Gripping" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "Sad" in KB["categories"]:
        category_array.append(1)
    elif "!Sad" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    if "Social" in KB["categories"]:
        category_array.append(1)
    elif "!Social" in KB["categories"]:
        category_array.append(-1)
    else:
        category_array.append(0)

    return category_array


# forward chaining facts from rules
def forward_chaining(KB):
    empty = 0

    while empty != 1:   # most outer loop - just iterates. (like epochs)
        new = []
        for rule in KB["rules"]:    # loop over all rules
            premises, conclusion = rule  # the rule has a premise and a conclusion
            if conclusion not in KB["categories"]:
                flag = 1
                for p in premises:  
                    if p not in KB["questions"]:
                        flag = 0
                if flag == 1 and conclusion not in KB["categories"]:   # all premises are there, and the rule is new
                    new.append(conclusion)                        # new fact found!
        if new == []:   # we didn't find any new fact - stop the inference!
            empty = 1
        else:
            for item in new:
                KB["categories"].append(item)    # add all new facts to the KB

    return KB

# Run after obtaining cursor with Age, Gender and Reading Level
def initialise_knowledge_base(question_list_from_GUI):

    KB = {}
    KB["rules"] = [
        (["like_complex Agree", "like_simple_narratives Disagree"], "ReadingCompetence"),  # ReadingCompetence category 12 total: 3^3 - 7 (neutral options) - 8 (reduced problem)
        (["like_complex Agree", "reading_task Disagree"], "ReadingCompetence"),  # reduced problem: if 2 of the 3 options are both Agree/Disagree then the outcome is as such
        (["like_simple_narratives Disagree", "reading_task Disagree"], "ReadingCompetence"),
        (["like_complex Agree", "like_simple_narratives Neutral", "reading_task Neutral"], "ReadingCompetence"),
        (["like_complex Neutral", "like_simple_narratives Disagree", "reading_task Neutral"], "ReadingCompetence"),
        (["like_complex Neutral", "like_simple_narratives Neutral", "reading_task Disagree"], "ReadingCompetence"),
        (["like_complex Disagree", "like_simple_narratives Agree"], "!ReadingCompetence"),  # Lower reading competence books
        (["like_complex Disagree", "reading_task Agree"], "!ReadingCompetence"),
        (["like_simple_narratives Agree", "reading_task Agree"], "!ReadingCompetence"),
        (["like_complex Disagree", "like_simple_narratives Neutral", "reading_task Neutral"], "!ReadingCompetence"),
        (["like_complex Neutral", "like_simple_narratives Agree", "reading_task Neutral"], "!ReadingCompetence"),
        (["like_complex Neutral", "like_simple_narratives Neutral", "reading_task Agree"], "!ReadingCompetence"),

        (["humor Disagree", "relax Agree"], "Entertaining"),    # Entertaining category 6 total: 3^2 - 3 (neutral options)
        (["humor Neutral", "relax Agree"], "Entertaining"),
        (["humor Disagree", "relax Neutral"], "Entertaining"),
        (["humor Agree", "relax Disagree"], "!Entertaining"),   # No entertaining books
        (["humor Neutral", "relax Disagree"], "!Entertaining"),
        (["humor Agree", "relax Neutral"], "!Entertaining"),

        (["mysteries Agree", "finishing Agree"], "Suspense"),    # Suspenseful category 12 total: 3^3 - 7 (neutral options) - 8 (reduced problem)
        (["mysteries Agree", "keep_reading Agree"], "Suspense"),   # reduced problem: if 2 of the 3 options are both Agree/Disagree then the outcome is as such
        (["finishing Agree", "keep_reading Agree"], "Suspense"),
        (["mysteries Agree", "finishing Neutral", "keep_reading Neutral"], "Suspense"),  
        (["mysteries Neutral", "finishing Agree", "keep_reading Neutral"], "Suspense"),
        (["mysteries Neutral", "finishing Neutral", "keep_reading Agree"], "Suspense"),
        (["mysteries Disagree", "finishing Disagree"], "!Suspense"),   # No suspenseful books
        (["mysteries Disagree", "keep_reading Disagree"], "!Suspense"),
        (["finishing Disagree", "keep_reading Disagree"], "!Suspense"),
        (["mysteries Disagree", "finishing Neutral", "keep_reading Neutral"], "Suspense"),  
        (["mysteries Neutral", "finishing Disagree", "keep_reading Neutral"], "Suspense"),
        (["mysteries Neutral", "finishing Neutral", "keep_reading Disagree"], "Suspense"),

        (["romantic Agree"], "Romantic"),  # Romantic category 2 total: 3 - 1 (neutral option)
        (["romantic Disagree"], "!Romantic"),   # No romantic books

        (["history Agree", "own_life Disagree"], "Historic"),    # Historic category 6 total: 3^2 - 3 (neutral options)
        (["history Neutral", "own_life Disagree"], "Historic"),
        (["history Agree", "own_life Neutral"], "Historic"),
        (["history Disagree", "own_life Agree"], "!Historic"),   # No historic books
        (["history Neutral", "own_life Agree"], "!Historic"),
        (["history Disagree", "own_life Neutral"], "!Historic"),

        (["reading_task Agree", "happy_ending Agree"], "FeelGood"),  # Feel good category 12 total: 3^3 - 7 (neutral options) - 8 (reduced problem)
        (["reading_task Agree", "relax Agree"], "FeelGood"),  # reduced problem: if 2 of the 3 options are both Agree/Disagree then the outcome is as such
        (["happy_ending Agree", "relax Agree"], "FeelGood"),
        (["reading_task Agree", "happy_ending Neutral", "relax Neutral"], "FeelGood"),
        (["reading_task Neutral", "happy_ending Agree", "relax Neutral"], "FeelGood"),
        (["reading_task Neutral", "happy_ending Neutral", "relax Agree"], "FeelGood"),
        (["reading_task Disagree", "happy_ending Disagree"], "!FeelGood"),  # No feel good books
        (["reading_task Disagree", "relax Disagree"], "!FeelGood"),
        (["happy_ending Disagree", "relax Disagree"], "!FeelGood"),
        (["reading_task Disagree", "happy_ending Neutral", "relax Neutral"], "!FeelGood"),
        (["reading_task Neutral", "happy_ending Disagree", "relax Neutral"], "!FeelGood"),
        (["reading_task Neutral", "happy_ending Neutral", "relax Disagree"], "!FeelGood"),

        (["humor Disagree", "comedy_v_drama Agree"], "Funny"),    # Funny category 6 total: 3^2 - 3 (neutral options)
        (["humor Neutral", "comedy_v_drama Agree"], "Funny"),
        (["humor Disagree", "comedy_v_drama Neutral"], "Funny"),
        (["humor Agree", "comedy_v_drama Disagree"], "!Funny"),   # No funny books
        (["humor Neutral", "comedy_v_drama Disagree"], "!Funny"),
        (["humor Agree", "comedy_v_drama Neutral"], "!Funny"),

        (["intense Agree", "keep_reading Agree"], "Gripping"),  # Gripping category 6 total: 3^2 - 3 (neutral option)
        (["intense Neutral", "keep_reading Agree"], "Gripping"),
        (["intense Agree", "keep_reading Neutral"], "Gripping"),
        (["intense Disagree", "keep_reading Disagree"], "!Gripping"),   # No gripping books
        (["intense Neutral", "keep_reading Disagree"], "Gripping"),
        (["intense Disagree", "keep_reading Neutral"], "Gripping"),

        (["comedy_v_drama Disagree", "happy_ending Disagree"], "Sad"),  # Sad category 12 total: 3^3 - 7 (neutral options) - 8 (reduced problem)
        (["comedy_v_drama Disagree", "moody Disagree"], "Sad"),  # reduced problem: if 2 of the 3 options are both Agree/Disagree then the outcome is as such
        (["happy_ending Disagree", "moody Disagree"], "Sad"),
        (["comedy_v_drama Disagree", "happy_ending Neutral", "moody Neutral"], "Sad"),
        (["comedy_v_drama Neutral", "happy_ending Disagree", "moody Neutral"], "Sad"),
        (["comedy_v_drama Neutral", "happy_ending Neutral", "moody Disagree"], "Sad"),
        (["comedy_v_drama Agree", "happy_ending Agree"], "!Sad"),  # No sad books
        (["comedy_v_drama Agree", "moody Agree"], "!Sad"),
        (["happy_ending Agree", "moody Agree"], "!Sad"),
        (["comedy_v_drama Agree", "happy_ending Neutral", "moody Neutral"], "!Sad"),
        (["comedy_v_drama Neutral", "happy_ending Agree", "moody Neutral"], "!Sad"),
        (["comedy_v_drama Neutral", "happy_ending Neutral", "moody Agree"], "!Sad"),

        (["social_issues Agree", "own_life Agree"], "Social"),  # Social category 12 total: 3^3 - 7 (neutral options) - 8 (reduced problem)
        (["social_issues Agree", "real_world Agree"], "Social"),  # reduced problem: if 2 of the 3 options are both Agree/Disagree then the outcome is as such
        (["own_life Agree", "real_world Agree"], "Social"),
        (["social_issues Agree", "own_life Neutral", "real_world Neutral"], "Social"),
        (["social_issues Neutral", "own_life Agree", "real_world Neutral"], "Social"),
        (["social_issues Neutral", "own_life Neutral", "real_world Agree"], "Social"),
        (["social_issues Disagree", "own_life Disagree"], "!Social"),  # No social books
        (["social_issues Disagree", "real_world Disagree"], "!Social"),
        (["own_life Disagree", "real_world Disagree"], "!Social"),
        (["social_issues Disagree", "own_life Neutral", "real_world Neutral"], "!Social"),
        (["social_issues Neutral", "own_life Disagree", "real_world Neutral"], "!Social"),
        (["social_issues Neutral", "own_life Neutral", "real_world Disagree"], "!Social"),
    ]

    KB["categories"] = []    
    KB["questions"] = convert_answers(question_list_from_GUI)   # should be updated after all questions
    
    KB = forward_chaining(KB)

    return KB
