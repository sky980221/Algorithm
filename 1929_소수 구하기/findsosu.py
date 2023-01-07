import sys
import math
"""
M 이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오
"""

def findPrimeNum(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if findPrimeNum(i):
        print(i)

"""2로 나눠서 나머지가 있으면 소수가 아니다 3으로 나눠서 나머지가 잇으면 소수가 아니다 """