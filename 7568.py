# 덩치

import sys
input = sys.stdin.readline

n = int(input())
lst=[]
for _ in range(n):
    a,b=map(int,input().split())
    lst.append([a,b])

ans=[]
for c in lst:
    count = 1

    for n in lst:
        if (c[0]!=n[0]) and (c[1]!=n[1]):
            if (c[0]<n[0]) and (c[1]<n[1]):
                count += 1
    ans.append(count)

print(' '.join(map(str, ans)))
# print(lst)