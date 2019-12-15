def question03(scores, alice):
    # modify and then return the variable below
    d={}
    ans=[]
    for i in alice:
        scores.append(i)
        scores.sort()
        scores.reverse()
        count=1
        num=scores[0]
        for j in range(len(scores)):
            if(scores[j]<num):
                count+=1
                num=scores[j]
                if(scores[j]==i):
                    ans.append(count)
                    break
    for i in ans:
        d[i]=0
    for i in ans:
        d[i]+=1
    max=0
    for i in sorted(d.keys()):
        if(d[i]>max):
            max=d[i]
            index=i
    answer = index
    return answer
