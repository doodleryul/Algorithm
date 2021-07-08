#10952 A+B - 5
while True:
  a, b = input().split()
  a = int(a)
  b = int(b)
  if a == 0:
    break
  print(a+b)

#10951 	A+B - 4
while True:
  try:
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)
  except:
    break
    
#1110 더하기 사이클
number = original = int(input())
i = 0
while True:
    number = (number%10)*10 + ((number//10 + number%10) % 10)
    if number == original:
        i += 1
        break
    else:
        i += 1
print(i)

