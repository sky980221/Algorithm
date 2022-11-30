import sys
N = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
b = []
w = []

def soulution(x, y, n):
    color = array[x][y] 
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != array[i][j]: 
                # 4 분할
                soulution(x, y, n // 2)
                soulution(x + n // 2, y, n // 2)
                soulution(x, y+ n // 2, n // 2)
                soulution(x + n // 2, y + n // 2, n // 2)
                return
    if color == 1:
        b.append(n ** 2)
    else:
        w.append(n ** 2)
    return

soulution(0, 0, N)
print(len(w))
print(len(b))