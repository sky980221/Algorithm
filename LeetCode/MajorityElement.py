class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 1
        check = nums[0]  # 초기 값 설정
        for num in nums[1:]:  # 첫 번째 요소는 이미 체크했으므로 슬라이스로 시작
            if check == num:
                cnt += 1
            else:
                check = num
                cnt = 1  # cnt를 1로 재설정
            if cnt > len(nums) // 2:
                return check
        return check