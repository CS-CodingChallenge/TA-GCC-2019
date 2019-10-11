# modify this function, and create other functions below as you wish
def question03(scores, alice):
    # modify and then return the variable below
    
    i = 0
    j = 0
    k = 0
    c = 0
    answer = 0
    n = len(scores)        
    m = len(alice)

    rank = [0  for i in range(n+m)]
    ref = [0 for i in range(0, m+n)]
    duplicate = []
    while(i<n):
    	rank[k] = scores[i]
    	i+=1
    	k+=1

    while (j<m):
    	rank[k] = alice[j]
    	j+=1
    	k+=1
    
    for w in range(0,len(rank)):
    	ref[w] = rank[w]

    for i in range(n, len(rank)-1):
    	if rank[i] == rank[i+1]:
    		c = rank[i]

    ref.sort(reverse=True)
    for num in ref:
    	if num not in duplicate:
    		duplicate.append(num)
    
    for i in range(len(duplicate)):
    	if c == duplicate[i]:
    		answer = i+1

    return answer
