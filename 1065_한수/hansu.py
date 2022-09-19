N= int(input())

hansu = 0

for i in range(1, N+1):  
    if i < 100:
        hansu += 1 
    else:
        suarray = list(map(int, str(i)))
        if suarray[2]- suarray[1] == suarray[1]-suarray[0]:
            hansu += 1

print(hansu)
