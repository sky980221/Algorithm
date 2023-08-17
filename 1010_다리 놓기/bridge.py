import sys

input = sys.stdin.readline


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


T = int(input())
for _ in range(T):
    N, R = list(map(int, input().split()))
    answer = factorial(R) / (factorial(N) * factorial(R - N))
    print(int(answer))
