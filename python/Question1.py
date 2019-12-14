# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    repayment = repaymentPercentage * initialLevelOfDebt / 100
    LevelOfDebt = initialLevelOfDebt
    answer=0
    while LevelOfDebt*(1+(interestPercentage/100)) >= repayment :
        LevelOfDebt = LevelOfDebt*(1+(interestPercentage/100)) - repayment
        answer = answer + repayment
    if LevelOfDebt*(1+(interestPercentage/100)) < repayment and LevelOfDebt*(1+(interestPercentage/100)) > 50:
        answer = answer+ LevelOfDebt*(1+(interestPercentage/100))
    elif LevelOfDebt*(1+(interestPercentage/100)) <= 50:
        answer = answer + 50
    answer = answer + repayment
    return answer
