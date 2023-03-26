n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
start = min(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    charge = mid
    num = 1
    for i in range(n):
        if charge < arr[i]:
            charge = mid
            num += 1
        charge -= arr[i]

    if num > m or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        k = mid

print(k)