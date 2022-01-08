#1712 손익분기점
A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

if B>=C:
    BREAK_EVEN_POINT = -1
    print(BREAK_EVEN_POINT)
else:
    BREAK_EVEN_POINT = int(A/(C-B)+1)
    print(BREAK_EVEN_POINT)
    
#2292 벌집
N = int(input())
cnt, room = 1, 1
while N>room:
    room += 6*cnt
    cnt += 1
print(cnt)

#1193 분수찾기
n = int(input())

cnt = 1
big_cnt = 0
while n>big_cnt:
    big_cnt += cnt
    cnt +=1
frac_num = n - (big_cnt - (cnt-1)) 

if ((cnt-1) % 2) == 0: #even
    print(str(frac_num)+'/'+str(cnt-frac_num))
else: #odd
    print(str(cnt-frac_num)+'/'+str(frac_num))
