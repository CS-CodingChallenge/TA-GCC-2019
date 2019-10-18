import numpy as np
from scipy import stats

#scores =[100, 90, 90, 80, 75, 60]
#alice =[50, 77, 77, 90]

def question03(scores, alice):
    # modify and then return the variable below
    scores = np.asarray(scores)
    alice = np.asarray(alice)
    
    rank = [stats.rankdata(1-np.append(scores,i), method='dense')[-1] for i in alice]
    values, counts = np.unique(rank, return_counts=True)
    answer = np.max(values[counts == counts.max()])
    
    return answer
