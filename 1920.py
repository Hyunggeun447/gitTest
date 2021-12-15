# 수 찾기

import sys
input = sys.stdin.readline

N = int(input())

N_list = input().rsplit()

M = int(input())

M_list = input().rsplit()

N_list=set(N_list)

# M_list=set(M_list)

# print(N_list , M_list)

for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)
