n = int(input())

num = '0123456789'

cnt = 1

nums = []
for i in num:
    nums.append(i)

while cnt < 10:
    for i in nums:
        if len(i) == cnt:

            for j in range(10):
                if int(i[-1]) > j:
                    nums.append(i + str(j))

    cnt += 1

if n > 1022:
    print(-1)
else:
    print(nums[n])
