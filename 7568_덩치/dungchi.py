N = int(input())
array = []
for _ in range(N):
    x, y = map(int,input().split())
    array.append((x,y))

for i in array:
    ranking = 1
    for j in array:
        if i[0]< j[0] and i[1] < j[1]:
            ranking = ranking + 1 
    print(ranking, end = " ")