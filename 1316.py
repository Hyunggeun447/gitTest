# 그룹 단어 체커

import sys
input = sys.stdin.readline

n = int(input())
ans=n
for _ in range(n):
    k = str(input().strip())

    for i in range(0,len(k)-1):
        if k[i] == k[i+1]:
            pass
        else:
            if k[i] in k[i+1:]:
                ans-=1
                break

print(ans)