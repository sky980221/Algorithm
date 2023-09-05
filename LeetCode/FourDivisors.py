#1390
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        result = 0
        for i in nums:
            current = 0
            for j in range(1, i+1):
                if i % j == 0:
                    sum = sum + j
                    current += 1
                if current == 4:
                    result = sum

        return result

"""
Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0"""