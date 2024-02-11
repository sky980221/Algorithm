from collections import Counter


def solution(participant, completion):
    answer = ''
    # part - comple = 완주 못한 선수 출력
    #     for i in completion:
    #         if i in participant:
    #             participant.remove(i)

    #     for j in participant:
    #          answer = j
    p_dict = Counter(participant)
    c_dict = Counter(completion)

    p_dict = p_dict - c_dict
    for i in p_dict:
        answer = i
    return answer