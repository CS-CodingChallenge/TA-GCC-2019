# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    p=initialLevelOfDebt
    i=interestPercentage
    r=repaymentPercentage
    d=p*0.1
    rep=max(p*r/100,50)
    c=0
    while(p>=50):
        c+=1
        p=p+p*i/100
        p=p-rep
    answer = int(d+rep*c+p)
    return answer
