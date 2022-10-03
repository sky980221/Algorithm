
def find(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def backtracking(x):
    global answer

    if x == N:
        answer = answer+1
        return
    else:
        for i in range(N):
            row[x] = i
            if find(x):
                backtracking(x+1)
N = int(input())
answer = 0
row = [0] * N 
backtracking(0)

print(answer)