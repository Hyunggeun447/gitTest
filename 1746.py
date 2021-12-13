# 듣보잡 구하기
import sys
input=sys.stdin.readline

N, M=map(int, input().split())

no_listen=set()
no_saw=set()
for _ in range(N):
    no_listen.add(str(input().rstrip()))
# print(no_listen)
for _ in range(M):
    no_saw.add(str(input().rstrip()))

k=list(no_saw & no_listen)
k=sorted(k)
# print(k)
print(len(k))
for i in k:
    print(i)