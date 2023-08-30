class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # sorted array 확인하면 -> BS 일 확률 높음
        # 만약 리스트에서 찾는다면 해당 key index return, 못 찾으면 어디 뒤에 들어가는지 index return
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                break
        return start