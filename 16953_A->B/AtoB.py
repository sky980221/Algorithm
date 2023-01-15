a, b = map(int, input().split())
result = 1
while True:

    # a와 b가 같은 경우
    if a == b:
        break
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        result = -1
        break

    else:

        if b % 10 == 1:
            b = b // 10
            result += 1


        else:
            b = b // 2
            result += 1
