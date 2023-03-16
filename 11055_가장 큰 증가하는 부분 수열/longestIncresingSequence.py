N = int(input())
numbers = list(map(int, input().split()))

dp = numbers[:]
dp[0] = numbers[0]
for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
        #수열에서 자신보다 앞 쪽에 있는 값 중에서 자신보다 작은 값의 인덱스를 찾는다.
            dp[i] = max(dp[i], dp[j] + numbers[i])
            #해당 인덱스의 dp값중 가장 큰 값과 자신의 값을 더해 dp를 다시 채운다.
print(max(dp))
