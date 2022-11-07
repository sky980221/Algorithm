N, T = map(int,input().split())
result = []
for i in range(N):
    si, li, ci = map(int,input().split())
    for j in range(ci):
        if si + li * j >= T:
            result.append( si + li * j - T) 
            break

if len(result) == 0:
    print("-1")
else:
    print(min(result))
