import numpy as np
import pandas as pd
import cvxpy


#v=[9, 13, 8, 10, 10, 13, 13, 0, 9, 0, 16, 4, 19, 17, 16, 17, 9, 6]
#c=[14, 76, 88, 74, 82, 33, 1, 92, 35, 83, 68, 59, 69, 20, 97, 25, 75, 68]
#mc=1025
#output=189
#
#v=[2, 14, 7, 1, 14, 3, 19, 14, 11, 4, 3, 12, 17, 5, 5, 2, 7, 2, 17, 8, 12, 14, 11, 9, 5, 8, 13, 8, 7, 10, 9, 9, 5, 14, 17, 1, 17, 1, 3, 12, 12, 3, 12, 10, 16, 12, 13, 3, 15, 10, 8, 8, 11, 6, 18, 14, 12, 15, 1, 15, 2, 14, 6, 2, 14, 12, 6, 4, 3, 11, 16, 17, 12, 14, 15, 7, 11, 10, 3, 3, 18, 10, 8, 3, 15, 9, 1, 15, 0, 13, 15, 6, 0, 19, 11, 9, 16, 1, 18, 15, 11, 14, 6, 9, 6, 18, 3, 9, 0, 12, 15, 19, 2, 0, 5, 1, 19, 14, 15, 0, 11, 11, 1, 13, 14, 8, 6, 6, 11, 9, 1, 2, 5, 12, 14, 0, 12, 10, 18, 1, 1, 12, 1, 14, 2, 16, 9, 2, 13, 5, 15, 0, 12, 17, 0, 1, 9, 8, 14, 1, 14, 8, 11, 0, 6, 3, 15, 13, 11, 0, 13, 9, 4, 0, 13, 3, 19, 8, 16, 10, 9, 10, 5, 9, 12, 1, 11, 4, 14, 7, 8, 3, 0, 2, 14, 16, 6, 1, 6, 8, 10, 5, 14, 4, 10, 7, 4, 1, 7]
#c=[84, 1, 53, 83, 13, 86, 86, 54, 41, 6, 32, 35, 28, 31, 49, 85, 68, 67, 89, 8, 97, 29, 26, 73, 3, 17, 89, 79, 3, 14, 58, 5, 87, 47, 14, 64, 1, 66, 19, 88, 72, 69, 14, 13, 66, 60, 57, 17, 16, 28, 97, 69, 56, 72, 28, 9, 2, 90, 33, 78, 80, 99, 3, 94, 83, 65, 73, 4, 54, 51, 24, 73, 5, 21, 24, 54, 32, 46, 74, 38, 5, 48, 49, 16, 85, 0, 92, 5, 29, 49, 8, 75, 10, 91, 33, 95, 76, 50, 56, 38, 51, 32, 4, 78, 43, 82, 41, 76, 77, 90, 3, 6, 94, 48, 93, 43, 37, 92, 16, 60, 50, 51, 16, 36, 54, 44, 76, 58, 24, 47, 16, 9, 63, 42, 50, 51, 68, 19, 55, 79, 1, 84, 23, 36, 76, 21, 6, 47, 39, 45, 32, 74, 74, 73, 36, 5, 29, 0, 87, 64, 62, 72, 59, 79, 40, 66, 19, 95, 75, 83, 20, 31, 86, 24, 8, 81, 25, 43, 8, 83, 81, 31, 33, 60, 90, 18, 74, 43, 45, 55, 13, 78, 60, 13, 2, 64, 27, 32, 8, 39, 98, 47, 84, 7, 95, 51, 83, 69, 13]
#mc= 5331
#output=1574
##
#v=[17, 7, 14, 11, 15, 19, 1, 10, 17, 4, 13, 3, 8, 17, 9, 7, 13, 3, 1, 3, 5, 0, 11, 2, 18, 19, 1, 7, 11, 19, 16, 5, 18, 19, 10, 15, 3, 9, 19, 15, 10, 2, 14, 18, 0, 8, 19, 11, 9, 0, 1, 1, 6, 18, 4, 8, 12, 13, 5, 2, 6, 4, 13, 1, 15, 3, 16, 18, 11, 15, 8, 11, 1, 16, 5, 12, 1, 10, 3, 8, 14, 10, 8, 3, 10, 13, 9, 5, 4, 3, 13, 9, 19, 5, 13, 18, 12, 10, 1, 15, 13, 2, 15, 4, 19, 4, 12, 10, 8, 3, 16, 11, 2, 0, 0, 8, 0, 2, 6, 2, 17, 14, 11, 12, 18, 5, 7, 15, 5, 7, 10, 11, 10, 9, 6, 17, 6, 0, 17, 13, 14, 0, 6, 8, 8, 2, 16, 11, 6, 9, 8, 5, 19, 4, 4, 17, 4, 8, 6, 4, 8, 3, 10, 1, 17, 15, 15, 16, 19, 15, 2, 15, 17, 12, 12, 2, 8, 10, 11, 9, 16, 17, 7, 4, 18, 18, 14, 5, 17, 1, 8, 13, 0, 16, 15, 16, 8, 2, 4, 5, 7, 14]
#c=[68, 43, 7, 53, 36, 14, 73, 28, 26, 88, 9, 10, 64, 48, 23, 86, 9, 50, 76, 54, 35, 44, 33, 0, 86, 52, 14, 59, 29, 38, 12, 11, 9, 36, 30, 63, 65, 6, 57, 1, 9, 75, 39, 0, 36, 58, 63, 50, 14, 90, 12, 56, 28, 51, 32, 49, 23, 83, 52, 40, 46, 35, 84, 75, 57, 75, 65, 34, 1, 18, 89, 52, 1, 48, 15, 80, 47, 14, 59, 71, 69, 51, 44, 46, 54, 25, 23, 52, 83, 70, 97, 74, 35, 69, 14, 47, 1, 8, 36, 93, 75, 8, 68, 99, 64, 88, 53, 95, 94, 65, 19, 91, 87, 27, 72, 36, 18, 58, 7, 64, 25, 66, 6, 97, 32, 14, 80, 35, 26, 84, 47, 81, 72, 42, 52, 61, 19, 5, 78, 98, 21, 24, 64, 95, 82, 54, 30, 60, 8, 73, 40, 97, 67, 2, 55, 0, 19, 65, 73, 95, 77, 48, 62, 54, 41, 88, 74, 17, 17, 69, 39, 46, 45, 28, 79, 63, 20, 87, 56, 97, 5, 95, 32, 75, 55, 64, 9, 20, 79, 28, 71, 49, 25, 72, 5, 94, 3, 13, 45, 58, 6, 88]
#mc=6334
#output=1735
#
#v=[11,1]
#c=[21,18]
#mc=22
#output=11
#
#v= [5, 12, 15, 4, 9, 11, 0, 19, 11, 18, 12, 16, 18, 7, 5, 4, 18, 16, 14, 2, 9, 3, 9, 7, 19, 2, 4, 2, 11, 4, 3, 19, 7, 9, 3, 12, 3, 19, 19, 16, 13, 17, 12, 7, 17, 2, 6, 4, 11]
#c=[14, 79, 0, 80, 38, 43, 54, 23, 20, 3, 26, 60, 29, 98, 70, 47, 90, 72, 59, 66, 71, 90, 87, 56, 71, 58, 40, 48, 21, 38, 11, 85, 94, 91, 28, 42, 2, 87, 52, 33, 5, 32, 33, 17, 11, 93, 8, 77, 26]
#mc=1373
#output=430

def lp(v, c, mc):
    
    df = pd.DataFrame(np.nan, index= range(len(c)), columns=['c','v','ratio'])
    
    df.v = v
    df.c = c
    
    df.ratio = df.v/df.c
    df= df.replace(np.inf, np.nan)
    
    df=df.sort_values('ratio',ascending=False, na_position='first')
    df[['c_sum','v_sum']] = df[['c','v']].cumsum()
       
    vector= np.zeros(len(c))
    try:
        vector[df[df['c_sum']<=mc].index]=1
    except:
        pass
    
    x = cvxpy.Variable(len(c), boolean=True)
    x.value = vector
    constraint = [c * x <= mc]
    obj = cvxpy.Maximize(v * x)
    
    prob = cvxpy.Problem(obj,constraint)
    answer = prob.solve(solver = cvxpy.GLPK_MI, maxiters=10, abstol=0.3, reltol=1e-4)
    
    answer = int(answer)
    
    return answer

def nump2(n, k):
    a = np.ones((k, n-k+1), dtype=int)
    a[0] = np.arange(n-k+1)
    for j in range(1, k):
        reps = (n-k+j) - a[j-1]
        a = np.repeat(a, reps, axis=1)
        ind = np.add.accumulate(reps)
        a[j, ind[:-1]] = 1-reps[1:]
        a[j, 0] = j
        a[j] = np.add.accumulate(a[j])
    return a

def combi(v, c, mc):
    
    n=len(c)
    k=n
    
    flag=0
    while flag==0:
        
        if k==0:
            return np.zeros(1)
        
        c_ix = nump2(n,k)
        c_sum = np.sum(c[c_ix],axis=0)
        
        if any(c_sum<=mc):
            v_ix = c_ix[:,c_sum<=mc]
            
            answer = np.max(np.sum(v[v_ix], axis=0))
            return int(answer)
        
        else:
            k=k-1
            
        
    

def question04(v, c, mc):
    v_np= np.asarray(v)
    c_np= np.asarray(c)
    
    if len(v)>40:
        answer = lp(v_np, c_np, mc)
    
    else:
        answer= combi(v_np, c_np, mc)
    
    return answer


