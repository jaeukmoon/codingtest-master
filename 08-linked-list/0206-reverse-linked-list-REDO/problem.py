"""
[0206] Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/

## 문제

단일 연결 리스트의 head가 주어진다.
리스트를 뒤집어서 새 head를 반환하라.

## 예시

Example 1: head = [1,2,3,4,5] → [5,4,3,2,1]
Example 2: head = [1,2]       → [2,1]
Example 3: head = []          → []

## 조건

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
