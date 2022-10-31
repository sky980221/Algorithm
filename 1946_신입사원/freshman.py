from sys import stdin

for i in range(int(stdin.readline())):
    people = []

    for j in range(int(stdin.readline())):
        people.append(list(map(int, stdin.readline().split())))

    people.sort()
    temp = people[0][1]
    cnt = 1

    for j in range(len(people)):
        if temp > people[j][1]:
            cnt += 1
            temp = people[j][1]

    print(cnt)