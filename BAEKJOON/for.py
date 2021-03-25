#2739 N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
N = int(input())
for i in range(1, 10):
  print("{} * {} = {}".format(N, i, N*i))
  
#10950 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
T = int(input())
for i in range(T):
  A, B = input().split()
  print(int(A)+int(B))
  
#8393 n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
n = int(input())
sum = 0
for i in range(n+1):
  sum += i
print(sum)

#15552 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
import sys
T = int(sys.stdin.readline())
for i in range(T):
  A, B = sys.stdin.readline().split()
  print(int(A)+int(B))
  
#2741 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
import sys
N = int(sys.stdin.readline())
for i in range(1, N+1):
  print(i)
  
#2742 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
import sys
N = int(sys.stdin.readline())
for i in reversed(range(1, N+1)):
  print(i)
  
#11021 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
  A, B = sys.stdin.readline().split()
  print("Case #{}: {}".format(i, int(A)+int(B)))
  
#11022 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
  A, B = sys.stdin.readline().split()
  print("Case #{}: {} + {} = {}".format(i, int(A), int(B), int(A)+int(B)))

#2438 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
import sys
N = int(sys.stdin.readline())
for i in range(1, N+1):
  print("*"*i)
  
#2439 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
import sys
N = int(sys.stdin.readline())
for i in range(1, N):
  print(" "*(N-i-1), "*"*i)
print("*"*N)

#10871 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
import sys
N, X = map(int, sys.stdin.readline().split())
n = sys.stdin.readline().split()
for i in n:
  if int(i) < int(X):
    print(int(i), end=" ")
