N = int(input())
array = [[0 for col in range(2)] for row in range(100000)]
for _ in range(N):
    age, name = input().split
    #입력 받았으니까 나이하고 이름 배열에 넣어줌
    array.append(age,name)

print(array)

'''
1. 이름과 age를 N번 만큼 입력 받은 후  배열에 넣는다 
2. age만 비교해서 더 어린 놈하고  
3. 만약 age가 같다면 그대로 



'''