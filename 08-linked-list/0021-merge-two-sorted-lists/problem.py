"""
[0021] Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

## 문제

오름차순으로 정렬된 두 연결 리스트 list1, list2가 주어진다.
두 리스트를 합쳐서 정렬된 하나의 연결 리스트로 만들고 head를 반환하라.
(노드를 새로 만들지 말고 기존 노드를 재배치할 것)

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

## 조건 (Constraints)

- 두 리스트의 노드 개수: [0, 50]
- -100 <= Node.val <= 100
- list1, list2는 각각 비내림차순(non-decreasing)으로 정렬됨
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode],
                  list2: Optional[ListNode]) -> Optional[ListNode]:
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
    print(to_list(mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))   # [1,1,2,3,4,4]
    print(to_list(mergeTwoLists(build([]), build([]))))                  # []
    print(to_list(mergeTwoLists(build([]), build([0]))))                 # [0]
