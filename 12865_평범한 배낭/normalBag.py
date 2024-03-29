import sys


n, k = map(int, sys.stdin.readline().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])

"""
4 7
6 13
4 8
3 6
5 12

다른 테케 찾아보장 

4 9 
3 11
9 12 
4 8
2 5  
"""
