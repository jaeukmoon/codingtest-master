"""
[0002] Add Two Numbers (Medium)
https://leetcode.com/problems/add-two-numbers/

## 문제

두 개의 비어있지 않은 연결 리스트가 주어진다. 각 리스트는 음이 아닌 정수를 **역순**으로 저장.
두 수를 더해 같은 형식의 연결 리스트로 반환하라.

## 예시

Example 1:
    Input:  l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

Example 2:
    Input:  l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input:  l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

## 조건 (Constraints)

- 두 리스트 노드 개수: [1, 100]
- 0 <= Node.val <= 9
- 선행 0 없음 (0 자체 제외)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
    print(to_list(addTwoNumbers(from_list([2,4,3]), from_list([5,6,4]))))         # [7,0,8]
    print(to_list(addTwoNumbers(from_list([0]), from_list([0]))))                  # [0]
    print(to_list(addTwoNumbers(from_list([9,9,9,9,9,9,9]), from_list([9,9,9,9]))))  # [8,9,9,9,0,0,0,1]
