N = int(input())
array = []
mod_count = 0

for i in range(N):
    a , b , c = map(int,input().split())
    for x in range(1,a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if x%y == y%z == z%x:
                    mod_count = mod_count+1
    array.append(mod_count)
    mod_count = 0
    
for i in array:
    print(i)
