# 감소하는 수

import sys
input = sys.stdin.readline
from itertools import combinations
n=int(input())

lst=[]

for i in range(1,11):
    for comb in combinations(range(0,10),i):
        comb = list(comb)
        comb.sort(reverse=True)
        lst.append(int(''.join(map(str, comb))))
        
lst.sort()
try:
    print(lst[n])
except:
    print(-1)