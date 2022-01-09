days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
week = ['FRI','SAT','SUN','MON','TUE','WED','THU']

def solution(a, b):
    total_days = 0
    for i in range(a):
        total_days += days[i]
    total_days += b
    answer = week[total_days%7-1]
    return answer
