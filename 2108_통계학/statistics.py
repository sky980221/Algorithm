import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

print(round(sum(a) / n))  # round() => 반올림 하는 함수

print(sorted(a)[len(a) // 2])

count = Counter(a)
order = count.most_common()
max_frequency = order[0][1]

fq = []
for i in order:
    if i[1] == max_frequency:
        fq.append(i[0])

if len(fq) == 1:
    print(fq[0])
else:
    print(sorted(fq)[1])

print(max(a) - min(a))