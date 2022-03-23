a= int(input())

x = 0
i = 0

while x < a:
    b= list(input().split())

    saveString = list(b[1])
    while i < int(b[0]):
        print(saveString[i]* int(b[0]),end = "")
        i = i+1
    print("")
    x = x+1
    