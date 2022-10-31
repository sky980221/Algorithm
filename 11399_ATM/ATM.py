N = int(input())
sum = 0
P = list(map(int,input().split()))
P.sort()

for i in range(N):
    for j in range(i+1):
        sum = sum+ P[j]

print(sum)
'''    
12334 

1 1+2 1+2+3 1+2+3+3 1+2+3+3+4 

32 
'''