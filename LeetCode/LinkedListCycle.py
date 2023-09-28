# Definition for singly-linked list.
"""class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = [] #이미 방문한 노드의 주소 저장
        curr = head #현재 노드를 시작 노드로 초기화

        while curr is not None:
            arr.append(curr)
            curr = curr.next
            if curr in arr:
                return True
        return False