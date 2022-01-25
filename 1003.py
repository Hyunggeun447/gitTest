# 피보나치 함수

import sys
input = sys.stdin.readline

check_zero=[1,0,1,1]
check_one=[0,1,1,2]

for i in range(41):
    check_zero.append(check_zero[-1]+check_zero[-2])
    check_one.append(check_one[-1]+check_one[-2])
    



n= int(input())
for _ in range(n):
    k=int(input())
    print(check_zero[k],check_one[k])

