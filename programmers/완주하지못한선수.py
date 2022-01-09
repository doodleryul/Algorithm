from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    answer = list(answer)[0]
    return answer