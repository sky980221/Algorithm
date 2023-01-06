import sys 
import math
x,y,c = map(float, sys.stdin.readline().split())
#C = h1h2 / h1+h2 
# h1 = sqr(x**2 - w**2), h2 = sqr(y**2 - w**2)
start = 1
end = min(x,y)
result = 0

while start + 0.001 <= end:
    mid = (start + end)/2
    h1 = math.sqrt(x**2 - mid**2)
    h2 = math.sqrt(y**2 - mid**2)
    calculatedC = (h1*h2)/(h1+h2)
    if calculatedC >= c:
        result = mid    
        start = mid     
    else:
        end = mid
print(result)
"""
두 빌딩 사이에 너비가 되는 길이를 구하여라 그 말인 즉슨 w1 + w2 를 구하여라 
Test Case1 
12.619429 8.163332 3

출력 
7.000

"""

