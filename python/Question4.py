import numpy as np
from itertools import combinations

def question04(v, c, mc):
    # modify and then return the variable below
    n = len(c)
    
    c = [comb for i in range(n) for comb in combinations(c, i + 1)]
    c_sum = [np.sum(i) for i in c]
    c_sum = np.asarray(c_sum)

    
    
    v = [comb for i in range(n) for comb in combinations(v, i + 1)]
    v_sum = [np.sum(i) for i in v]
    v_sum = np.asarray(v_sum)
    
    
    answer = np.max(v_sum[c_sum<=mc])
    return answer