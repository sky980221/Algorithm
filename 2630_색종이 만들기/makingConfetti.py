#20230824 재 풀이
import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
b = []
w = []


def soulution(x, y, n):
    color = array[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != array[i][j]:
                # 4 분할
                soulution(x, y, n // 2)
                soulution(x + n // 2, y, n // 2)
                soulution(x, y + n // 2, n // 2)
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

# 모든 칸이 0이거나 1이 아니면 분열
# 첫째 줄엔 하얀색 출력, 둘째 줄엔 파란색 출력


"""
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

"""
