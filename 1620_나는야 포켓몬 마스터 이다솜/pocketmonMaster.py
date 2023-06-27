from sys import stdin

def input():
    return stdin.readline().rstrip()


n, m = map(int, input().split())
findId = {}
findName = {}
for i in range(1, n + 1):
    pokemon = input()
    findId[i] = pokemon
    findName[pokemon] = i

for _ in range(m):
    x = input()
    if x.isdigit():
        print(findId[int(x)])
    else:
        print(findName[x])