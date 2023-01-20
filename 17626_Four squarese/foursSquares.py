import math

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j ** 2])
    dp.append(minValue + 1)

print(dp[n])
"""

- n보다 작거나 같은 제곱수를 찾고 n-제곱수를 인덱스로 가진 값에 1을 더해주면 된다.

 >> d[i - (j**2)] + 1

예를 들어 n= 27이면 25를 찾고 27-25를 인덱스로 가진 값에 1을 더 해주면 된다. 
2를 인덱스로 가진 값에 1 ? 
  
"""

