# 백준 Z만들기
import sys
input=sys.stdin.readline

N, r, c = map(int, input().split())

standard=0

while N>0: 
    k=2**(N-1)
    temp_y=r//k
    temp_x=c//k
    r=r%k
    c=c%k

    M=(2**N)**2
    # print(k, temp_y, temp_x,r,c,M)
    
    temp_list=[[standard, standard+M//4],[standard+M//2,standard+M*3//4]]

    # print(temp_list)
    
    standard=temp_list[temp_y][temp_x]
    # print(standard)
    
    N-=1

# print(N, r, c)
print(standard)
