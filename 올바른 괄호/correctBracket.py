def solution(s):
    stack = []
    for c in s:
        #C가 열린 괄호라면 스택에 저장함.
        if c == "(":
            stack.append(c)
        #닫힌 괄호라면, 스택이이 차 있는지 확인하고 차 있다면 맨 뒤에 것을 제거, 비어있다면 False 출력
        else:
            if stack:
                stack.pop()
            else:
                return False
        #일련의 과정을 끝낸 뒤 스택이 비어있지 않다면 False 출력, 비어있어야 True.
    if stack:
        return False
    return True