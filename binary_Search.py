import sys
arr = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
arr.sort()

start = 0
end = len(arr) -1
while start <= end:
  mid = (start + end)//2
  if arr[mid] == target:
    print(mid+1)
    break
  elif arr[mid] > target:
    end = mid -1 
  else: 
    start = mid + 1
  
"""
<< Binary Search 마스터 >>
왜 써야 하는가 ? : n(log n)으로 매우 속도가 빠름.
그러나 자료가 오름차순으로 되어 있어야 한다는 단점이 있다.
target : 찾아야 하는 값
data : 오름차순으로 정렬된 List
start : data의 맨 처음 값 인덱스
end : data의 마지막 값 인덱스

사용 방법 
mid 값이 target이랑 일치될 때까지 움직여준다. 
같다면 그대로 print나 return 해주면 되고 
아니라면 보통 대소 비교해서 start 와 end 값을 이동해준다.


"""