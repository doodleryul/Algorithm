#15596 정수 N개의 합
def solve(a):
    ans = sum(a)
    return ans
  
#4673 셀프 넘버
original_set = set(range(1, 10001))
generated_set = set()

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  generated_set.add(i)

self_num = sorted(original_set - generated_set)
for num in self_num:
  print(num)

#1065 한수
N = int(input())

if N <= 99:
  print(N)

else:
  count = 99
  for i in range(100, N+1):
    fst_value = int(str(i)[1]) - int(str(i)[0])
    sec_value = int(str(i)[2]) - int(str(i)[1])
    if fst_value == sec_value:
      count += 1
    else: pass

  print(count)
