N= int(input())
arr= list(map(int, input().split())) #정수를 여러개 받아서 배열에 저장 


cnt = 0
start=0
result = 0
for i in arr:
    if i> start:
        start= i
        cnt =0
    else:
        cnt = cnt + 1
    
    result = max(cnt,result)

print(result)   