class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currentOnes = 0

        for i in nums:
            if i is 1:
                currentOnes += 1
                maxOnes = max(maxOnes, currentOnes)
            else:
                maxOnes = max(maxOnes, currentOnes)
                currentOnes = 0

        return maxOnes


"""
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""