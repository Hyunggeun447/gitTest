# 부분합
from collections import deque
import sys
input = sys.stdin.readline

n,s=map(int,input().split())


lst=list(map(int, input().split()))

left,right = 0,0

ans=n+1
check_sum=0
while True:
    if check_sum>=s:
        ans=min(ans,right-left)
        check_sum-=lst[left]
        left+=1
    elif right==n:
        break
    elif check_sum<s:
        check_sum+=lst[right]
        right+=1
    
    
if ans==n+1:
    print(0)
else:
    print(ans)