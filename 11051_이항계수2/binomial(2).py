from math import factorial
n, k = map(int, input().split())
bino = (factorial(n) // (factorial(n-k) * factorial(k)))
answer = bino % 10007

print(answer)

