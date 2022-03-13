# 가장 긴 증가하는 부분 수열 (이분탐색)
# 부분수열의 요소를 정확히 구하는 것보다 길이만 정확히 구하는게 신기한 페러다임
# 공부할 여지 있음.

import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

check=[0]

for i in lst:
    if check[-1]<i:
        check.append(i)
    else:
        lft=0
        rgt=len(check)

        while lft < rgt:
            mid= (lft + rgt) //2

            if check[mid] < i:
                lft = mid+1
            else:
                rgt = mid
        check[rgt] = i

print(len(check)-1)