import sys
N = int(sys.stdin.readline())
count = 0
def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

num = list(map(int, str(factorial(N))))
for i in num[::-1]:
    if i != 0:
        break
    count += 1
print(count)