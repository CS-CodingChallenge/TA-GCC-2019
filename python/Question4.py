# modify this function, and create other functions below as you wish
def question04(v, c, mc):
    # modify and then return the variable below
    dp = [0]*(mc+1)
    for i in range(len(v)):
        
        for j in range(mc,c[i]-1,-1):
            
            dp[j] = max(dp[j],v[i]+dp[j-c[i]])
            
    answer = dp[mc]
    return answer
