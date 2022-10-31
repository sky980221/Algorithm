N, K = map(int,input().split())
moneyArray = []
coins = 0
for i in range(N):
    moneyArray.append(int(input()))

moneyArray.sort(reverse=True)
for i in range(N):
    if K//moneyArray[i] >= 1:
        coins = coins +  K//moneyArray[i]
        K = K % moneyArray[i]

print(coins)