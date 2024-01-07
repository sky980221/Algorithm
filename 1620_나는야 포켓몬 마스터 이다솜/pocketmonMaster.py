import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokedex = {}  # 빈 딕셔너리 생성

for i in range(1, N + 1):
    pokemon_name = input().strip()
    pokedex[i] = pokemon_name
    pokedex[pokemon_name] = i
print(pokedex)
for j in range(M):
    find = input().strip()
    if find.isdigit():  # 입력이 숫자인 경우
        print(pokedex[int(find)])
    else:  # 입력이 문자열인 경우
        print(pokedex[find])
