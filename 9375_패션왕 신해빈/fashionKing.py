T = int(input())

for i in range(T):
    n = int(input())
    weardict = {}
    for j in range(n):
        clothes = list(input().split())
        if clothes[1] in weardict:
            weardict[clothes[1]].append(clothes[0])
        else:
            weardict[clothes[1]] = [clothes[0]]

    cnt = 1 

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)