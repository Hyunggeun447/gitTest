# 하노이의 탑(재귀함수로 푸는.. 재공부 요망)
def hanoi(f, t, m, n):
    if n == 0:
        return []

    return hanoi(f, m, t, n-1) + [[f, t]] + hanoi(m, t, f, n-1)


def solution(n):
    return hanoi(1, 3, 2, n)


n=int(input())
ans=solution(n)

print(len(ans))
for a,b in ans:
    print(a,b)