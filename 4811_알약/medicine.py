import sys
input = sys.stdin.readline

medi = [[0 for _ in range(31)] for _ in range(31) ]
for j in range(1,31):
    medi[0][j] = 1

for i in range(1,31):
    for j in range(30):
        if j == 0:
            medi[i][j] = medi[i-1][j+1]
        else:
            medi[i][j] = medi[i-1][j+1] + medi[i][j-1]

while 1:
    n = int(input())
    if n == 0:
        break
    print(medi[n][0])