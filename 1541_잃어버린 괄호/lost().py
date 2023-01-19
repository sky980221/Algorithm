senti = input().split("-")
# -를 기준으로 나눠줌 55-50+40이면 55와 50+40으로 나뉨
num = []
result = 0
for i in senti:
    sum = 0
    tmp = i.split("+")  # + 부호를 기준으로 split
    for j in tmp:
        sum += int(j)

    num.append(sum)

n = num[0]

for i in range(len(num) - 1):
    result = result + num[i + 1]
result = n - result
print(result)
"""
Test Case 1 
55-50+40

출력 
-35
"""
