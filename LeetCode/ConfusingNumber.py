# 1056
class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated, original = 0, n
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        for digit in str(n):
            digit = int(digit)
            if digit not in mapping:  # 숫자가 dictionary의 value 값에 안 들어간다면 False
                return False
            else:  # dictionary 값에 해당이 된다면 rotate 시켜주자
                rotated *= 10
                rotated += mapping[digit]
        #만약 바꾼 rotate 수가 입력 받았던 값하고 다르면 True 같으면 False
        if rotated != original:
            return True
        else:
            return False



"""
Input: n = 89
Output: true
Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.
"""
