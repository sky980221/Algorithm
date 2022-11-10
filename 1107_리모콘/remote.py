N = int(input())
M = int(input())
remote = {str(x) for x in range(10)}

if M != 0:
    remote = remote - set(map(input().split()))

mincount = abs(100 - N) 

for k in range(1000001):
    num= str(k)
    for i in range(len(k)):
        if num[i] not in remote:
            break
        if i == len(num)-1:
            mincount = min(mincount, abs(N-k)+len(num))

print(mincount)
        