from collections import deque

bird = int(input())
bird_list = list()

for i in range(bird):
    bird_list.append(deque(map(str, input().split())))
sentence = deque(map(str, input().split()))

def possible(sentence, arr):
    m = 0
    j = 0
    while sentence:
        if arr[j] and sentence[0] == arr[j][0]:
            arr[j].popleft()
            sentence.popleft()
            m = 0 
        else:
            if m == bird:
                return False
            m += 1 
        j = (j + 1) % bird

    empty = 0
    for i in range(bird):
        if len(arr[i]) == 0:
            empty += 1

    if not sentence and empty == bird: 
        return True
    else:
        return False

if possible(sentence, bird_list):
    print("Possible")
else:
    print("Impossible")