wave = [0 for i in range(101)]
wave[1] = 1
wave[2] = 1
wave[3] = 1
for i in range(0, 98):
    wave[i + 3] = wave[i] + wave[i + 1]
T = int(input())
for i in range(T):
    N = int(input())
    print(wave[N])