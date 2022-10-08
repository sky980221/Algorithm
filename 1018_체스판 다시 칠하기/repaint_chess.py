N, M = map(int, input().split())
before = []
cnt = []

for _ in range(N):
    before.append(input())

for a in range(N-7):
    for b in range(M-7):
        start_W = 0
        start_B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if before[i][j] != 'W':
                        start_W += 1
                    if before[i][j] != 'B':
                        start_B += 1
                else:
                    if before[i][j] != 'B':
                        start_W += 1
                    if before[i][j] != 'W':
                        start_B += 1
        cnt.append(min(start_W, start_B))

print(min(cnt))