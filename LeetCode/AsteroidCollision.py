class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        newArr = []
        for i in asteroids:
            newArr.append(i)

            while len(newArr) > 1 and ((newArr[-1] < 0) and (newArr[-2] > 0)):
                j, i = newArr.pop(), newArr.pop()

                if abs(j) != abs(i):
                    if abs(j) > abs(i):
                        newArr.append(j)
                    else:
                        newArr.append(i)
        return newArr