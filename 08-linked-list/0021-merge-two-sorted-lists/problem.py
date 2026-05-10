"""
[0021] Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

## 문제

두 정렬된 연결 리스트 list1, list2가 주어진다.
두 리스트를 합쳐 정렬된 하나의 리스트로 만들고 head 반환.
**노드를 새로 만들지 말고 원래 노드를 이어붙이는 방식**으로 풀어라.

## 예시

Example 1:
    Input:  list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input:  list1 = [], list2 = []
    Output: []

Example 3:
    Input:  list1 = [], list2 = [0]
    Output: [0]

## 조건

- 두 리스트 노드 개수: [0, 50]
- -100 <= Node.val <= 100
- 두 리스트 모두 오름차순 정렬
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
    print(to_list(mergeTwoLists(from_list([1,2,4]), from_list([1,3,4]))))   # [1,1,2,3,4,4]
    print(to_list(mergeTwoLists(from_list([]), from_list([]))))               # []
    print(to_list(mergeTwoLists(from_list([]), from_list([0]))))              # [0]
