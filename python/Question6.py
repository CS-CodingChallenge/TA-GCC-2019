
#import numpy as np
#import pandas as pd

#portfolio=["EPANAHZWEW", "XNOMQDND","USJXIKC", "EKW", "PJJGKILZ", "DXZQ",
#           "ELHSW", "EBV", "BNYWLTGSFI", "EVOUKGMW", "MUQUDJLUQ", "QGGNGSDZET"]
#output=9

#portfolio = ["ILDOEWUEQIX", "WTUKGLWH", "OUPMYQWFJL", "JXER", "WVUIFWLTC", "WZNN", "XPVCELNJQ", "SMS", "RZC", "YTNSDMZBRKV", "TAOLJEU", "OVJLE", "DWISP", "BPGIFBQDBWZ", "RLIRCASQOPIA", "UZOCWEQ", "HKVAL", "CZZFHXUKDYNF", "SFCZW", "TTKBL"]

def maximum_keys(dic):
    maximum = max(dic.values())
    keys = filter(lambda x:dic[x] == maximum,dic.keys())
    return keys,maximum

def get_position(port_np, n, ix=None):
    
    if ix is not None:
        range_iter = ix
    else:
        range_iter = range(len(port_np))
    
    letter_index ={}
    letter_count ={}
    
    for i in range_iter:
        v=port_np[i]
        if (v[0:n],v[-n:]) in letter_index:
            letter_index[v[0:n],v[-n:]].append(i)
            letter_count[v[0:n],v[-n:]] +=1
        else:
            letter_index[v[0:n],v[-n:]] = [i]
            letter_count[v[0:n],v[-n:]] =1
     
    k1,v1 = maximum_keys(letter_count)
    
    if v1>1:
        return letter_index[k1[0]]
    
    elif ix is None:
        return[-1]
        
    else:
        k2,v2 = maximum_keys(letter_index)
        return v2


def question06(portfolio):

    portfolio = eval(portfolio)
    
    i=1
    answer = get_position(portfolio,i)
    
    while len(answer)!=1:
        i=i+1
        answer = get_position(portfolio,i, answer)
        
    return answer[0]

