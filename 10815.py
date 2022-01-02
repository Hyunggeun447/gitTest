# 숫자카드

import sys
input = sys.stdin.readline

n = int(input())

lst = set(map(int,input().split()))

m = int(input())
lst2=list(map(int,input().split()))
ans = []
for i in lst2:
    if i in lst:
        ans.append(1)
    else:
        ans.append(0)


print(' '.join(map(str, ans)))