from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = deque(nums)
        q.rotate(k)
        for i in range(len(nums)):
            nums[i]= q[i]
