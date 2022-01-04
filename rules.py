# forward chaining facts from rules
def forward_chaining(KB):
    empty = 0

    while empty != 1:   # most outer loop - just iterates. (like epochs)
        new = []
        for rule in KB["rules"]:    # loop over all rules
            premises, conclusion = rule  # the rule has a premise and a conclusion
            flag = 1
            for p in premises:  
                if p not in KB["facts"]:
                    flag = 0
            if flag == 1 and conclusion not in KB["facts"]:   # all premises are there, and the rule is new
                new.append(conclusion)                        # new fact found!
        if new == []:   # we didn't find any new fact - stop the inference!
            empty = 1
        else:
            for item in new:
                KB["facts"].append(item)    # add all new facts to the KB

    return KB

# Run after obtaining cursor with Age, Gender and Reading Level
def initialise_knowledge_base(cursor):

    KB = {}
    KB["rules"] = [
        (["humor", "comedy_v_drama"], "Funny"),
        (["romantic"], "Romantic")
    ]

    KB["facts"] = []    #should be updated after each/all question(s)
    KB["entities"] = cursor

    return KB