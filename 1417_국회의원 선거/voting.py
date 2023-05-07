import sys
n = int(sys.stdin.readline())
num = int(sys.stdin.readline())
vote = []
count = 0
for _ in range(n - 1):
  vote.append(int(sys.stdin.readline()))
vote.sort(reverse=True)
if n == 1:
  print(0)
else:
  while vote[0] >= num:
    num += 1
    vote[0] -= 1
    count += 1
    vote.sort(reverse=True)
  print(count)