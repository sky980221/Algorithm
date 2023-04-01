import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    aArr = list(set([int(x) for x in input().split()]))
    M = int(sys.stdin.readline())
    bArr = list(set([int(x) for x in input().split()]))
    K = int(sys.stdin.readline())
    cArr = list(set([int(x) for x in input().split()]))
    luckyNum = []

    for i in range(len(aArr)):
        for j in range(len(bArr)):
            for k in range(len(cArr)):
                temp = str(aArr[i] + bArr[j] + cArr[k])
                lucky = True
                for l in range(len(temp)):
                    if not (temp[l] == '5' or temp[l] == '8'):
                        lucky = False
                        break
                if lucky:
                    luckyNum.append(temp)
    luckyNum = set(luckyNum)
    print(len(luckyNum))
