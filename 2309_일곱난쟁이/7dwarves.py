array= []

for i in range(9):
    array.append(int(input()))

sumheight = sum(array)

for i in range (len(array)):
    for j in range(i+1, len(array)):
        if sumheight - array[i] - array[j] == 100:
            fakedwarf1 = array[i]
            fakedwarf2 = array[j]
array.remove(fakedwarf1)
array.remove(fakedwarf2)            

array.sort()
for i in array:
    print(i)