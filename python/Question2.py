# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    # modify and then return the variable below
    sum = 0
    for i in range(0,len(trader)):
	b = 0
	for j in range(0,len(risk)):
		if trader[i]>=risk[j]:
			if bonus[j]>=b:
				b = bonus[j]
	sum = sum + b
    return sum
