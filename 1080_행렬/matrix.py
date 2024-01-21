# 20240121 행렬
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = [list(map(int, list(input().strip()))) for _ in range(N)]
arr2 = [list(map(int, list(input().strip()))) for _ in range(N)]

cnt = 0


# 3x3 범위를 돌면서 1이면 0으로, 0이면 1으로 flip 해줌
def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            if arr1[x][y] == 0:
                arr1[x][y] = 1
            else:
                arr1[x][y] = 0


# 만약 리스트가 3x3보다 작으면서 arr1과 arr2가 다르다면
if (N < 3 or M < 3) and arr1 != arr2:
    cnt = -1
else:
    # -2 해주는 이유 = 리스트 끝 쪽에 있는 두 블럭은 개별 뒤집기가 불가능 하기 때문. (기본 뒤집기 사이즈가 3x3)
    for r in range(N - 2):
        for c in range(M - 2):
            if arr1[r][c] != arr2[r][c]:
                cnt += 1
                flip(r, c)
if cnt != -1:
    if arr1 != arr2:
        cnt = -1
print(cnt)
