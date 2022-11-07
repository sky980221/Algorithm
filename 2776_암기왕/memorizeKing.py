T = int(input())

for _ in range(T):
    note1 = int(input())
    note1Array = set(map(int,input().split()))
    note2= int(input())
    note2Array = list(map(int,input().split()))

    for i in note2Array:
        print(1 if i in note1Array else 0)