# 프린터 큐
import sys
input = sys.stdin.readline
from collections import deque


N_test = int(input())

for _ in range(N_test):
    N, M = map(int, input().split())

    list = input().rsplit()

    main = deque()

    for i in range(len(list)):
        list[i]=int(list[i])
        main.append([int(list[i]),i])
    count=1
    # print(main,list)
    while deque:
        [a, b] = main.popleft()
        k=max(list)
        if a < k:
            main.append([a, b])
        else:
            if b == M:
                print(count)
                break

            else:
                list.remove(k)
                count+=1
        # print(count,list,main)