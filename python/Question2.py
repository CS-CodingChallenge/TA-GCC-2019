import numpy as np


#trader = [2, 10, 9, 10, 10]
#risk = [9, 1, 1, 6, 1]
#bonus = [9, 9, 8, 10, 10]

def question02(risk, bonus, trader):
    # modify and then return the variable below
    
    trader = np.asarray(trader)
    risk = np.asarray(risk)
    bonus = np.asarray(bonus)
     
    answer = [np.max(bonus[risk<=i]) if (bonus[risk<=i]).size >0 else 0 for i in trader]
    answer = np.sum(answer)

    return answer
