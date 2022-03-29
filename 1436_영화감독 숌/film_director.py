N =int(input())

first = 666

while N != 0:
    if '666' in str(first):
        N = N -1
    if N == 0:
        break
    first = first + 1 #이 줄을 if문 안에 넣게 되면 N이 1일 때 first가 666이 아니라 667이 된다. 

print(first)


'''
1. 숫자를 넣어
2. first라는 변수에 666을 넣는다
3. N 이 0이 아니면 계속 반복
4. 만약 666이 문자열 안에 있으면 N을 1 감소 시킴 
5. N이 0이면 탈출 
  '''
