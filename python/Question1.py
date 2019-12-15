def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below

    count = 0
    answer = initialLevelOfDebt*.1
    r = initialLevelOfDebt*(repaymentPercentage/100.0)

    while(initialLevelOfDebt>=r):
        initialLevelOfDebt = initialLevelOfDebt + initialLevelOfDebt*(interestPercentage/100.0)
        initialLevelOfDebt = initialLevelOfDebt - r
        count = count + 1

    print initialLevelOfDebt
    answer = answer + count * r + initialLevelOfDebt# + initialLevelOfDebt*(interestPercentage/100.0)
    if(initialLevelOfDebt>=50):
    	answer = answer + initialLevelOfDebt*(interestPercentage/100.0)
    return int(answer)
    
