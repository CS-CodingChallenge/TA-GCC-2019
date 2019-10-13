# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    count=0
    curdebt=initialLevelOfDebt
    repay=initialLevelOfDebt*(repaymentPercentage/100)
    while(curdebt>50):
        count+=1
        curdebt=curdebt+((interestPercentage/100)*curdebt)-repay
    answer=curdebt+repay+(count*repay)

    
    return answer
