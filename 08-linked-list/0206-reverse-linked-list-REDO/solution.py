"""
[0206] Reverse Linked List (Easy)
링크: https://leetcode.com/problems/reverse-linked-list/

## 문제

단일 연결 리스트의 head를 입력받아 뒤집어진 리스트의 새 head 반환.

## 예시

Example 1: [1,2,3,4,5] → [5,4,3,2,1]

## 조건

- 노드 개수: [0, 5000]
- -5000 <= Node.val <= 5000

---

핵심 아이디어 (Iterative — 정석):
    포인터 3개: prev, curr, nxt
    1) nxt에 curr.next 미리 저장
    2) curr.next = prev (방향 뒤집기)
    3) prev = curr, curr = nxt (한 칸 전진)
    curr가 None되면 prev가 새 head.

자료구조 / 패턴:
    - Linked List 포인터 조작

시간복잡도: O(n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I'll reverse pointers iteratively using three references: prev, curr, next.
     For each node, I save next, flip curr's pointer to prev, then advance.
     O(n) time and O(1) space."

엣지 케이스:
    - 빈 리스트: None
    - 한 노드: 그대로

## 손 추적 (Hand Trace)
# head = 1 → 2 → 3 → None
#
# 초기: prev=None, curr=1
#
#  Step | nxt 백업 | curr.next = prev    | prev | curr
# ------|----------|---------------------|------|------
#   1   | nxt = 2  | 1 → None            | 1    | 2
#   2   | nxt = 3  | 2 → 1 → None        | 2    | 3
#   3   | nxt = None | 3 → 2 → 1 → None | 3    | None
#
# curr == None → 종료, return prev = 3 (새 head)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next       # 다음 노드 백업
        curr.next = prev      # 방향 뒤집기
        prev = curr           # prev 한 칸 전진
        curr = nxt            # curr 한 칸 전진
    return prev


# 재귀 버전 (대안 — 면접 후 언급용)
# def reverseList(head):
#     if not head or not head.next:
#         return head
#     new_head = reverseList(head.next)
#     head.next.next = head
#     head.next = None
#     return new_head


def to_list(head):
    r = []
    while head:
        r.append(head.val)
        head = head.next
    return r


def from_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(reverseList(from_list([1,2,3,4,5]))))   # [5,4,3,2,1]
    print(to_list(reverseList(from_list([1,2]))))         # [2,1]
    print(to_list(reverseList(from_list([]))))             # []
