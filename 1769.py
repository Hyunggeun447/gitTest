# 3의 배수

import sys
input = sys.stdin.readline

n = str(input().strip())
ans=0
while len(n)>1:
    temp=0
    for i in range(len(n)):
        temp+=int(n[i])
    n=str(temp)
    ans+=1

print(ans)
if int(n)%3 == 0:
    print('YES')
else:
    print('NO')