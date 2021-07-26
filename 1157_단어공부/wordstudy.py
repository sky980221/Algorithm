a= input().upper()
A_SET = list(set(a))

count_list = []

for x in A_SET:
    cnt = a.count(x)
    count_list.append(cnt) #count 숫자를 리스트에 append 

if count_list.count(max(count_list)) > 1: #count 숫자 최대값이 중복시 
    print("?")
else : 
    max_index = count_list.index(max(count_list)) #count 숫자 최대값 위치
    print(A_SET[max_index])