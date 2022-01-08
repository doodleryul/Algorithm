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
    
#1152 단어의 개수
char = input().split()
print(len(char))

#2908 상수
numbers = input().split()
a = int(numbers[0][::-1])
b = int(numbers[1][::-1])
print(max(a, b))

#5622 다이얼
dial = input().lower()

alphabet = list(map(chr, range(97, 123)))
dial_count = [3,3,3,3,3,4,3,4]

dial_alphabet = []
j = 0
k = 0
for i in dial_count:
  j += i
  dial_alphabet.append(alphabet[k:j])
  k += i

times = 0
for i in dial:
  for idx, j in enumerate(dial_alphabet):
    if i in j:
      times += idx + 3

print(times)

#2941 크로아티아 알파벳
word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
  if i in word:
    word = word.replace(i, '*')

print(len(word))

#1316 그룹 단어 체커
from copy import copy

N = int(input())

words = []
for i in range(N):
    words.append(input())

output = copy(words)

for word in words:
    chars = set(word)
    
    for char in chars:
        breaker = False
        char_loc = []
        
        for idx, alphabet in enumerate(word):
            if char == alphabet:
                char_loc.append(idx)
                
        for a, b in zip(char_loc, char_loc[1:]):
            if a+1 != b:
                output.remove(str(word))
                breaker = True
                break
        if breaker == True:
            break

print(len(output))

