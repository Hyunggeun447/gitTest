# 최소공배수, 최대공약수

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

# def gcd(a,b):
#     while b>0:
#         a,b = b, a%b
    
#     return a

# def lcm(a,b):
#     return a*b//gcd(a,b)

# print(gcd(a,b))
# print(lcm(a,b))

import math
print(math.gcd(a,b))
print(a*b//math.gcd(a,b))