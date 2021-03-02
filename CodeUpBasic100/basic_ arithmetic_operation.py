#6032 입력된 정수의 부호를 바꿔 출력해보자. 
n = int(input())
print(-n)

#6033 문자 1개를 입력받아 그 다음 문자를 출력해보자. 
n = input()
print(chr(ord(n)+1))

#6034 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자. 
a, b = input().split()
c = int(a) - int(b)
print(c)

#6035 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자. 
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)

#6036 단어와 반복 횟수를 입력받아 여러 번 출력해보자. 
w, n = input().split()
print(w*int(n))

#6037 반복 횟수와 문장을 입력받아 여러 번 출력해보자. 
n = input()
s = input()
print(int(n)*s)

#6038 정수 2개(a, b)를 입력받아 
#a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a, b = input().split()
c = int(a)**int(b)
print(c)

#6039 실수 2개(f1, f2)를 입력받아 
#f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
f1, f2 = input().split()
c = float(f1)**float(f2)
print(c)

#6040 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자. 
a, b = input().split()
print(int(a)//int(b))

#6041 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자. 
a, b = input().split()
print(int(a)%int(b))
