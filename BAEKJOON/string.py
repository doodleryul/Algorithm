#11654 아스키 코드
char = input()
print(ord(char))

#11720 숫자의 합
N = int(input())
char = input()
result = 0
for i in range(N):
  result += int(char[i])
print(result)

#10809 알파벳 찾기
S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
  if i in S:
    for idx, s in enumerate(S):
      if s == i:
        print(idx)
        break
  else: print(-1)
    
#2675 문자열 반복
N = int(input())
for i in range(N):
  R, S = input().split()
  P = []
  for i in str(S):
    P += i*int(R)
  print(''.join(P))
  
#1157	단어 공부
from collections import Counter

s = input().lower()
count_dict = Counter(s)
if len(count_dict) == 1:
  print(list(count_dict)[0].upper())
else:
  sorted_count = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)[:2]
  if sorted_count[0][1] == sorted_count[1][1]:
    print('?')
  else:
    print(sorted_count[0][0].upper())
