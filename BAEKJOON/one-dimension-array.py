#10818 최소, 최대
import sys
N = int(sys.stdin.readline())
number_list = sys.stdin.readline().split()
number_int = []
for i in number_list:
    number_int.append(int(i))
print(min(number_int), max(number_int))

#2562 최댓값
numbers = {}
for i, n in enumerate(range(9)):
  numbers[int(input())] = i+1
max_num = max(list(numbers.keys()))
print(max_num)
print(numbers[max_num])

#2577 숫자의 개수
import collections
abc = 1
for i in range(3):
  abc = abc * int(input())
abc_list = [int(i) for i in str(abc)]
counters = collections.Counter(abc_list)
for i in range(0, 10):
  print(counters[i])
  
#3052 나머지
reminders = []
for _ in range(10):
  reminders.append(int(input())%42)
print(len(list(set(reminders))))

#1546 평균
scores = []
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

def calculator(x):
  return x/M*100

new_scores = list(map(lambda x:x/M*100, scores))
print(sum(new_scores)/N)

#8958 OX퀴즈
case_num = int(input())
for i in range(case_num):
  test_case = input()
  score = 0
  count = 0
  for i in test_case:
    if i == "O":
      count += 1
    elif i == "X":
      count = 0
    score += count  
  print(score)
  
#4344 평균은 넘겠지
C = int(input())
for i in range(C):
  N_scores = list(map(int, input().split()))
  N = N_scores[0]
  scores = N_scores[1:]
  average = sum(scores)/N
  larger = len(list(filter(lambda x: x>average, scores)))
  number = round(larger/N*100, 3)
  print("{:.3f}%".format(number))
