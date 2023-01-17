import sys
N = int(sys.stdin.readline())
goalArray = []
array = []
result = []
for _ in range(N):
    goalArray.append(int(sys.stdin.readline()))
for j in range(N):
    array.append(j+1)
    result.append("+")
    while array:
        if array[-1] == goalArray[0]:
            goalArray.pop(0)
            array.pop()
            result.append("-")
        else:
            break

if len(array) == 0:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")
"""
8
4
3
6
8
7
5
2
1

출력
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
    """