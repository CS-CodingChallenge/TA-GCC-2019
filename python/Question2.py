# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    # modify and then return the variable below
    answer=0
    for i in trader:
        l=list()
        c=0
        for j in risk:
            if(i>=j):
                l.append(bonus[c])
            c+=1
        answer=answer+max(l)        
    return answer
