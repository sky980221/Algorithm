import sys
input = sys.stdin.readline

nums = [1,3,5]
target = 3
start, end = 0, len(nums) - 1

while start <= end:
    mid = (start + end) // 2
    if nums[mid] < target:
        start = mid + 1
    elif nums[mid] > target:
        end = mid - 1
    else:
        break

print(start)