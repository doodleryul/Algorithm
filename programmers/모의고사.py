def solution(answers):
    import math
    math1 = [1, 2, 3, 4, 5]
    math2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ### inner function ###
    def math_correct(p):
        new_p = p*math.ceil(len(answers)/len(p))
        num=0
        for i in range(len(answers)):
            if answers[i] == new_p[i]:
                num+=1
        return num
    
    result = dict()
    result[1] = math_correct(math1)
    result[2] = math_correct(math2)
    result[3] = math_correct(math3)
    answer = []
    for key, value in result.items():
        if value == max(list(result.values())):
            answer.append(key)
    return answer