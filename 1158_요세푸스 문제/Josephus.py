N,K= map(int, input().split())
array = []
answer =[]
number = 0
for i in range(N):
    array.append(i+1)
for i in range(N):
    number = number + (K-1)
    if number >= len(array):
        number = number % len(array)

    answer.append(str(array.pop(number)))
print("<",', '.join(answer),">", sep="")
   



 

        

