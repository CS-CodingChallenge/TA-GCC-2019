# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    s=0
    a=0
    for skill in trader:
        for i in range(len(risk)):
            if risk[i] <= skill and a<bonus[i]:
                a=bonus[i]
        s+=a
    
    # modify and then return the variable below
    answer = s
    return answer
