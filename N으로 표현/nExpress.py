def solution(N, number):
    num = []  # 숫자 조합을 담는 리스트

    for i in range(1, 9):  # i = 숫자 N을 사용하는 횟수
        case = {int(str(N) * i)}  # i번 사용하는 숫자 조합, 이어붙이는 경우의 수를 미리 넣어둠

        # 숫자 조합끼리의 사칙연산
        for j in range(0, i - 1):
            for x in num[j]:
                for y in num[-j - 1]:
                    case.add(x + y)
                    case.add(x - y)
                    case.add(x * y)
                    if y != 0:
                        case.add(x // y)
                        # 숫자 조합에 number 가 있는 경우
        if number in case:
            return i

        # 숫자 조합에 number 가 없으면 리스트에 추가
        num.append(case)

    return -1