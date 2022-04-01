A,B,V = list(map(int, input().split())) 

#A는 낮에 올라가는 길이 2
#B는 밤에 미끄러지는 길이 1 
#V는 나무 막대의 길이 5

H = A - B 

Day = (V - A) // H 

if (V-A) % H  ==0:
    Day = Day + 1
else: 
    Day = Day + 2

print(Day) 

