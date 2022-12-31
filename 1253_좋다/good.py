"""
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

"""
import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = len(arr)
cnt = 0 

for i in arr:
    tmp = arr[:i] + arr[i+2:]
    start = 0
    end = len(tmp)-1
    while start < end:
        mid = tmp[start] + tmp[end]
        if arr[mid] == target:
            cnt += 1 
            break
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid +1
 
print(cnt)