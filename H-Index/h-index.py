# def solution(citations):
#     h = 0
#     cnt = 0
#     # citations는 인용된 횟수 배열
#     citations.sort()
#     # 배열의 원소가 h보다 큰게 h개 이상
#     if sum(citations) == 0:
#         return 0
#
#     while cnt >= h:
#         cnt = 0
#         for i in citations:
#             if i >= h:
#                 cnt += 1
#         if h > cnt:
#             return h - 1
#         h += 1
#
#     return h - 1


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer