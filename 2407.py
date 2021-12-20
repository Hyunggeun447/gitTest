# 조합

import sys
import math
input = sys.stdin.readline

n , m = map(int, input().split())

ans = math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

print(ans)