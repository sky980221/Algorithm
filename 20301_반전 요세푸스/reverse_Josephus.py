import sys
N,K,M = map(int,sys.stdin.readline().split())
array = []
answer = []
number = 0
reverse_state = False
for i in range(N):
    array.append(i+1)
while len(array) > 0 :
    if len(answer) % M == 0:
        reverse_state = not reverse_state
    if reverse_state:
        number = (number + K - 1) % len(array)
    else:
        number = (number - K) % len(array)
        while number < 0:
            number += len(array)
    answer.append(array[number])
    array.pop(number)

for i in answer:
    print(i)
