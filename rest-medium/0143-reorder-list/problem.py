"""
[0143] Reorder List (Medium)
https://leetcode.com/problems/reorder-list/

## 문제

연결 리스트 head: L0 → L1 → ... → Ln-1 → Ln
다음 형태로 **in-place** 재배열:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

값을 바꾸지 말고 **노드 자체를 재배열**하라.

## 예시

Example 1:
    Input:  head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input:  head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

## 조건 (Constraints)

- 노드 개수: [1, 5 * 10^4]
- 1 <= Node.val <= 1000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    """in-place 재배열, 반환 없음"""
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
    h1 = from_list([1,2,3,4])
    reorderList(h1)
    print(to_list(h1))   # [1,4,2,3]

    h2 = from_list([1,2,3,4,5])
    reorderList(h2)
    print(to_list(h2))   # [1,5,2,4,3]
