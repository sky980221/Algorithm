N = int(input())  # 가입한 사람의 수 입력
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))  # 나이를 정수로 변환하여 저장

# 나이를 기준으로 정렬 (나이가 같으면 가입 순서 유지)
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])

'''
1. 이름과 age를 N번 만큼 입력 받은 후  배열에 넣는다 
2. age만 비교해서 더 어린 놈하고  
3. 만약 age가 같다면 그대로 



'''