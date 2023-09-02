#2#박상돈
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # 결과 연결 리스트의 헤드 노드를 생성합니다.
        current = head  # 현재 노드를 헤드 노드로 초기화합니다.
        over = 0  # 올림 값을 저장하는 변수를 초기화합니다.

        while l1 or l2 or over:
            total = over

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            over = total // 10
            current.next = ListNode(total % 10)
            current = current.next

        return head.next
