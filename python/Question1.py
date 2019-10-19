

#initialLevelOfDebt = 1000
#interestPercentage = 5
#repaymentPercentage = 10
#
#
#
#initialLevelOfDebt=646348.3073611051
#interestPercentage=8.311599872614883
#repaymentPercentage=75.18992827296624
#output=441


#initialLevelOfDebt=251.14010486284624
#interestPercentage=6.016428117673908
#repaymentPercentage=19.84449246401944
#output=333
#
#initialLevelOfDebt=253.93076180202192
#interestPercentage=4.707233913374964
#repaymentPercentage=17.792331417219103
#output=326

def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    
    
    paid_month = initialLevelOfDebt*(repaymentPercentage)/100.0
    
    debt = float(initialLevelOfDebt)
    count=0
    while debt>paid_month:
        debt = debt*(100 + interestPercentage)/100.0
        #debt = round(debt*(1.0 + interest),2)
        #print(debt)
        count += 1
        debt -= paid_month
        #print(debt)
        
    answer = count*paid_month+ debt + 0.1 * initialLevelOfDebt
    
    return int(round(answer))
