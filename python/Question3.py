# modify this function, and create other functions below as you wish
def question03(scores, alice):
    # modify and then return the variable below
    ## only unique values
    set_scores = set(scores)
    ## sort them to get their rank which is the index+1
    ranks = sorted(set_scores, reverse = True)
    my_ranks = []
    for a in alice:
    	temp_list = ranks
    	temp_list.append(a)
    	temp_list = sorted(temp_list, reverse = True)
    	index_of_a = temp_list.index(a)
    	my_ranks.append(index_of_a+1)
    ## find the mode
    answer = max(set(my_ranks), key=my_ranks.count)
    
    return answer



# RESULT:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 44.293s

# OK
# A question 3 test has timed out. Each individual test has a maximum of one second to run.
# A question 3 test has timed out. Each individual test has a maximum of one second to run.
# A question 3 test has timed out. Each individual test has a maximum of one second to run.
# A question 3 test has timed out. Each individual test has a maximum of one second to run.
# A question 3 test has timed out. Each individual test has a maximum of one second to run.
# A question 3 test has timed out. Each individual test has a maximum of one second to run.
# {'questionNumber': 3, 'testNumber': 0, 'correct': 'CORRECT', 'speed': 3179.9999999998495}
# {'questionNumber': 3, 'testNumber': 1, 'correct': 'CORRECT', 'speed': 3369.999999999762}
# {'questionNumber': 3, 'testNumber': 2, 'correct': 'INCORRECT', 'speed': 3029.999999998312}
# {'questionNumber': 3, 'testNumber': 3, 'correct': 'CORRECT', 'speed': 3090.0000000000373}
# {'questionNumber': 3, 'testNumber': 4, 'correct': 'INCORRECT', 'speed': 3019.999999998024}
# {'questionNumber': 3, 'testNumber': 5, 'correct': 'CORRECT', 'speed': 3129.999999998412}
# {'questionNumber': 3, 'testNumber': 6, 'correct': 'CORRECT', 'speed': 3460.00000000235}
# {'questionNumber': 3, 'testNumber': 7, 'correct': 'INCORRECT', 'speed': 3480.0000000001496}
# {'questionNumber': 3, 'testNumber': 8, 'correct': 'INCORRECT', 'speed': 3050.0000000016626}
# {'questionNumber': 3, 'testNumber': 9, 'correct': 'CORRECT', 'speed': 3130.0000000011873}
# {'questionNumber': 3, 'testNumber': 10, 'correct': 'CORRECT', 'speed': 3050.0000000016626}
# {'questionNumber': 3, 'testNumber': 11, 'correct': 'CORRECT', 'speed': 2719.9999999977244}
# {'questionNumber': 3, 'testNumber': 12, 'correct': 'INCORRECT', 'speed': 3210.000000000712}
# {'questionNumber': 3, 'testNumber': 13, 'correct': 'CORRECT', 'speed': 3310.000000000812}
# {'questionNumber': 3, 'testNumber': 14, 'correct': 'INCORRECT', 'speed': 3190.0000000001373}
# {'questionNumber': 3, 'testNumber': 15, 'correct': 'CORRECT', 'speed': 2840.000000001175}
# {'questionNumber': 3, 'testNumber': 16, 'correct': 'CORRECT', 'speed': 2930.0000000009873}
# {'questionNumber': 3, 'testNumber': 17, 'correct': 'CORRECT', 'speed': 3120.0000000009}
# {'questionNumber': 3, 'testNumber': 18, 'correct': 'CORRECT', 'speed': 3300.000000000525}
# {'questionNumber': 3, 'testNumber': 19, 'correct': 'CORRECT', 'speed': 2889.999999999837}
# {'questionNumber': 3, 'testNumber': 20, 'correct': 'INCORRECT', 'speed': 3190.0000000001373}
# {'questionNumber': 3, 'testNumber': 21, 'correct': 'CORRECT', 'speed': 2940.000000001275}
# {'questionNumber': 3, 'testNumber': 22, 'correct': 'CORRECT', 'speed': 2940.000000001275}
# {'questionNumber': 3, 'testNumber': 23, 'correct': 'CORRECT', 'speed': 2879.99999999955}
# {'questionNumber': 3, 'testNumber': 24, 'correct': 'INCORRECT', 'speed': 3690.000000000637}
# {'questionNumber': 3, 'testNumber': 25, 'correct': 'CORRECT', 'speed': 2959.9999999990746}
# {'questionNumber': 3, 'testNumber': 26, 'correct': 'INCORRECT', 'speed': 3339.9999999988995}
# {'questionNumber': 3, 'testNumber': 27, 'correct': 'INCORRECT', 'speed': 3699.999999998149}
# {'questionNumber': 3, 'testNumber': 28, 'correct': 'CORRECT', 'speed': 2999.9999999974493}
# {'questionNumber': 3, 'testNumber': 29, 'correct': 'CORRECT', 'speed': 3130.0000000011873}
# {'questionNumber': 3, 'testNumber': 30, 'correct': 'INCORRECT', 'speed': 3039.9999999985994}
# {'questionNumber': 3, 'testNumber': 31, 'correct': 'INCORRECT', 'speed': 3339.9999999988995}
# {'questionNumber': 3, 'testNumber': 32, 'correct': 'INCORRECT', 'speed': 3160.00000000205}
# {'questionNumber': 3, 'testNumber': 33, 'correct': 'INCORRECT', 'speed': 3369.999999999762}
# {'questionNumber': 3, 'testNumber': 34, 'correct': 'INCORRECT', 'speed': 3449.999999999287}
# {'questionNumber': 3, 'testNumber': 35, 'correct': 'INCORRECT', 'speed': 5620.000000000625}
# {'questionNumber': 3, 'testNumber': 36, 'correct': 'CORRECT', 'speed': 3059.9999999991746}
# {'questionNumber': 3, 'testNumber': 37, 'correct': 'INCORRECT', 'speed': 5869.999999999487}
# {'questionNumber': 3, 'testNumber': 38, 'correct': 'CORRECT', 'speed': 2900.0000000001246}
# {'questionNumber': 3, 'testNumber': 39, 'correct': 'CORRECT', 'speed': 2979.9999999996494}
# {'questionNumber': 3, 'testNumber': 40, 'correct': 'INCORRECT', 'speed': 4879.999999998774}
# {'questionNumber': 3, 'testNumber': 41, 'correct': 'CORRECT', 'speed': 3119.999999998124}
# {'questionNumber': 3, 'testNumber': 42, 'correct': 'CORRECT', 'speed': 2960.00000000185}
# {'questionNumber': 3, 'testNumber': 43, 'correct': 'INCORRECT', 'speed': 3390.000000000337}
# {'questionNumber': 3, 'testNumber': 44, 'correct': 'CORRECT', 'speed': 2810.0000000003124}
# {'questionNumber': 3, 'testNumber': 45, 'correct': 'CORRECT', 'speed': 3360.00000000225}
# {'questionNumber': 3, 'testNumber': 46, 'correct': 'INCORRECT', 'speed': 3529.9999999988117}
# {'questionNumber': 3, 'testNumber': 47, 'correct': 'CORRECT', 'speed': 4930.000000000212}
# {'questionNumber': 3, 'testNumber': 48, 'correct': 'INCORRECT', 'speed': 3440.000000001775}
# {'questionNumber': 3, 'testNumber': 49, 'correct': 'CORRECT', 'speed': 2800.0000000000246}
# {'questionNumber': 3, 'testNumber': 50, 'correct': 'CORRECT', 'speed': 3810.0000000013124}
# {'questionNumber': 3, 'testNumber': 51, 'correct': 'CORRECT', 'speed': 3090.0000000000373}
# {'questionNumber': 3, 'testNumber': 52, 'correct': 'CORRECT', 'speed': 2950.0000000015625}
# {'questionNumber': 3, 'testNumber': 53, 'correct': 'CORRECT', 'speed': 2940.000000001275}
# {'questionNumber': 3, 'testNumber': 54, 'correct': 'INCORRECT', 'speed': 3330.0000000013874}
# {'questionNumber': 3, 'testNumber': 55, 'correct': 'CORRECT', 'speed': 2840.000000001175}
# {'questionNumber': 3, 'testNumber': 56, 'correct': 'CORRECT', 'speed': 3580.0000000002497}
# {'questionNumber': 3, 'testNumber': 57, 'correct': 'CORRECT', 'speed': 3600.000000000825}
# {'questionNumber': 3, 'testNumber': 58, 'correct': 'CORRECT', 'speed': 6119.999999998349}
# {'questionNumber': 3, 'testNumber': 59, 'correct': 'CORRECT', 'speed': 3720.0000000014998}
# {'questionNumber': 3, 'testNumber': 60, 'correct': 'TIMED_OUT', 'speed': -1}
# {'questionNumber': 3, 'testNumber': 61, 'correct': 'TIMED_OUT', 'speed': -1}
# {'questionNumber': 3, 'testNumber': 62, 'correct': 'TIMED_OUT', 'speed': -1}
# {'questionNumber': 3, 'testNumber': 63, 'correct': 'TIMED_OUT', 'speed': -1}
# {'questionNumber': 3, 'testNumber': 64, 'correct': 'TIMED_OUT', 'speed': -1}
# {'questionNumber': 3, 'testNumber': 65, 'correct': 'TIMED_OUT', 'speed': -1}
