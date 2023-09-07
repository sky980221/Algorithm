class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if i in '([{':
                arr.append(i)
            else:
                if not arr or \
                    (i == ')' and arr[-1] != '(') or \
                    (i == '}' and arr[-1] != '{') or \
                    (i == ']' and arr[-1] != '['):
                    return False
                arr.pop()
        return not arr