"""
[0019] Remove Nth Node From End of List (Medium)
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## 문제

연결 리스트의 head와 정수 n이 주어진다.
끝에서 n번째 노드를 제거하고 head를 반환하라.

## 예시

Example 1:
    Input:  head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input:  head = [1], n = 1
    Output: []

Example 3:
    Input:  head = [1,2], n = 1
    Output: [1]

## 조건 (Constraints)

- 노드 개수: sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Follow-up

한 번의 순회(one pass)로 풀 수 있는가?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(removeNthFromEnd(from_list([1,2,3,4,5]), 2)))   # [1,2,3,5]
    print(to_list(removeNthFromEnd(from_list([1]), 1)))            # []
    print(to_list(removeNthFromEnd(from_list([1,2]), 1)))          # [1]
