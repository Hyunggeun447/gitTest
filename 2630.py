# 색종이

import sys
input=sys.stdin.readline


count_zero = 0
count_one = 0


def paper(start_x,start_y,n,arr):
    global count_one
    global count_zero
    if n==1:
        if arr[start_y][start_x] == 0:
            count_zero+=1
        elif arr[start_y][start_x] == 1:
            count_one+=1
        return
    else:
        for i in range(start_y,start_y+n):
            for j in range(start_x,start_x+n):
                if arr[start_y][start_x] != arr[i][j]:
                    n=n//2
                    paper(start_x,start_y,n,arr)
                    paper(start_x,start_y+n,n,arr)
                    paper(start_x+n,start_y,n,arr)
                    paper(start_x+n,start_y+n,n,arr)
                    return
        if arr[start_y][start_x] == 0:
            count_zero+=1
        elif arr[start_y][start_x] == 1:
            count_one+=1
        return


n = int(input())

lst=[]
for _ in range(n):
    tem_lst = list(map(int, input().split()))
    lst.append(tem_lst)

paper(0,0,n,lst)
# print(n)
# print(lst)
print(count_zero)
print(count_one)