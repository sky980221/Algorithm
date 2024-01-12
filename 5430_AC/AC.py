import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    arr = deque(arr)  # 더 효율적인 pop을 위해 deque 사용
    error = False

    # 두 개의 포인터를 초기화
    left, right = 0, n - 1

    for op in p:
        if op == "R":
            # 순서를 뒤집기 위해 포인터를 교환
            left, right = right, left
        elif op == "D":
            if not arr or len(arr) == 0:
                print("error")
                error = True
                break
            if left < right:
                arr.popleft()  # 왼쪽 끝에서 효율적으로 제거
            else:
                arr.pop()  # 오른쪽 끝에서 효율적으로 제거

    if not error:
        result = list(arr)
        if left > right:
            result.reverse()  # 순서가 뒤집혔을 경우 원래 순서로 되돌림
        print("[" + ",".join(result) + "]")

    if error_code != 1:
        print(arr)
