#Use chr, ord

# 6025 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a, b = input().split()
c = int(a) + int(b)
print(c)

# 6026 실수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a = input()
b = input()
c = float(a) + float(b)
print(c)

#6029 16진수를 입력받아 8진수(octal)로 출력해보자. 
a = input()
n = int(a, 16)
print('%o'%n)

#6030 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
n = ord(input())
print(n)

#6031 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
n = int(input())
print(chr(n))
