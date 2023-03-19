import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push":
        value = word[1]
        arr.append(value)
    elif order == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(len(arr))
    elif order == "size":
        print(len(arr))
    elif order == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(stack[-1])
