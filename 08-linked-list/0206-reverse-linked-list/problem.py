"""
[0206] Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/

## 문제

단일 연결 리스트의 head가 주어진다.
리스트를 뒤집어서 새로운 head를 반환하라.

## 예시

Example 1:
    Input:  head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input:  head = [1,2]
    Output: [2,1]

Example 3:
    Input:  head = []
    Output: []

## 조건 (Constraints)

- 노드 개수: [0, 5000]
- -5000 <= Node.val <= 5000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


# --- 테스트 헬퍼 ---
def build(values):
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    print(to_list(reverseList(build([1, 2, 3, 4, 5]))))   # Expected: [5,4,3,2,1]
    print(to_list(reverseList(build([1, 2]))))             # Expected: [2,1]
    print(to_list(reverseList(build([]))))                 # Expected: []
