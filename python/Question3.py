# modify this function, and create other functions below as you wish
def question03(scores, alice):
    # modify and then return the variable below
    
    ar_score = []
    my_score = []
    rank = []

    n = int(input())
    for i in range(n):
    	x = int(input())
    	if x not in ar_score:
    		ar_score.append(x)

    m = int(input())
    for i in range(m):
    	x = int(input())
    	my_score.append(x)

    for i in range(m):
    	for j in range(n):
    		if my_score[i] == ar_score[j]:
    			rank.append(j+1)

    		elif my_score[i]>ar_score[j]:
    			if my_score[i]<ar_score[j-1]:
    				rank.append(j+1)
    		else:
    			rank.append(len(ar_score)+1)

    for i in rank:
    	if rank[i] == rank[i+1]:
    		answer = rank[i]
    	else:
    		pass

    return answer
