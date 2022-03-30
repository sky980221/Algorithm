T= int(input())

for _ in range(T):
    k = int(input()) #k층 
    n = int(input()) #n호

    k0 = [x for x in range(1, n+1)]

    for f in range (k):
        for i in range(1, n):
            k0[i] += k0[i-1]
    print(k0[-1])
'''while k >= 0:
    1+2+
    k=k-1
'''