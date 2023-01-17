N = int(input())
M = int(input())
remote = {str(x) for x in range(10)}

if M != 0:
    remote = remote - set(map(input().split()))

minCount = abs(100 - N)

for k in range(1000001):
    num= str(k)
    for i in range(len(k)):
        if num[i] not in remote:
            break
        if i == len(num)-1:
            minCount = min(minCount, abs(N-k)+len(num))

print(minCount)
        