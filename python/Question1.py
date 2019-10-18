import math

initialLevelOfDebt = 1000
interestPercentage = 5
repaymentPercentage = 10

def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    
    
    paid_month = max(math.floor(initialLevelOfDebt*(repaymentPercentage))/100.0, 50.0)
    
    debt = float(initialLevelOfDebt)
    count=0
    while debt>paid_month:
        debt = math.floor(debt*(100 + interestPercentage))/100.0
        #debt = round(debt*(1.0 + interest),2)
        #print(debt)
        count += 1
        debt -= paid_month
        #print(debt)
        
    answer = count*paid_month+ debt + 0.1*initialLevelOfDebt
    
    return answer
