# 수열의 합

import sys
input=sys.stdin.readline

n=int(input())
lst=[]

for _ in range(n):
    lst_temp = list(map(int,input().split()))
    lst.append(lst_temp)
ans=[]
total=0
# print(lst)
if n>2:
    
    for i in range(n):
        total+=sum(lst[i])

    total= total//((n-1)*2)

    for i in range(n):
        a = (sum(lst[i])-total)//(n-2)
        ans.append(str(a))

elif n==2:
    ans=[str(lst[0][1]//2),str(lst[0][1]//2)]

# print(ans)
print(" ".join(ans))
