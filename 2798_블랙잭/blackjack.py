""" 3중 포문을 이용한 블랙잭 풀이 
n, m = map(int, input().split())
num = list(map(int, input().split()))
l = len(num)
ans = 0
for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if(num[i] + num[j] + num[k] > m):
                continue
            else:
                ans = max(ans ,num[i] + num[j] + num[k])

print(ans)
"""
#순열 조합을 이용한 블랙잭 풀이 

from itertools import permutations

n, m = map(int, input().split())

num = list(map(int, input().split()))
permutationArray = permutations(num, 3) #combinations도 사용 가능함 
ans = 0
for i in permutationArray:
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans) 