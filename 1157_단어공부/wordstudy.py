a= input().upper() #전부 다 대문자로 바꿔버림 
A_SET = list(set(a)) #중복되는 문자들을 하나의 문자로 만듦 

count_list = []
print(A_SET)
for x in A_SET:
    cnt = a.count(x) #문자열에서 찾고싶은 문자의 개수 사용법 : 변수.count(찾는 요소)
    print(cnt)
    count_list.append(cnt) #count 숫자를 리스트에 append 

if count_list.count(max(count_list)) > 1: #count 숫자 최대값이 중복시 ex) if   hello 에서 2번 나오는 알파벳의 개수가 1보다 크면:
    print("?")
else : 
    max_index = count_list.index(max(count_list)) #count 숫자 최대값 위치
    print(A_SET[max_index])
