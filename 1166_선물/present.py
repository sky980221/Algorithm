N,L,W,H= map(int,input().split())


s,e = 0, max(L,W,H)

for _ in range(100):
    M = (s+e)/2 
    cnt = (L//M) * (W//M) * (H//M)
    if cnt >= N:
        s = M 
    else:
        e = M
    

print("%.10f" %(e))