import sys
T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    b = input()
    arr = list(b)
    for i in b:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
