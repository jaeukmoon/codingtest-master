"""
[0141] Linked List Cycle (Easy)
https://leetcode.com/problems/linked-list-cycle/

## 문제

연결 리스트의 head가 주어진다.
리스트에 사이클이 있으면 true, 없으면 false 반환.
사이클 = 어떤 노드의 next가 이전 노드를 다시 가리키는 경우.

## 예시

Example 1:
    Input:  head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: tail이 두 번째 노드(2)에 연결됨.

Example 2:
    Input:  head = [1,2], pos = 0
    Output: true

Example 3:
    Input:  head = [1], pos = -1
    Output: false

## 조건

- 노드 개수: [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos = -1 또는 [0, n-1] (사이클 시작 인덱스)

## Follow-up

O(1) 메모리로 풀 수 있는가?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    pass


def make_cycle(values, pos):
    """pos가 -1이면 사이클 없음, 아니면 tail이 values[pos] 노드를 가리키게"""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    print(hasCycle(make_cycle([3,2,0,-4], 1)))   # True
    print(hasCycle(make_cycle([1,2], 0)))         # True
    print(hasCycle(make_cycle([1], -1)))          # False
    print(hasCycle(make_cycle([], -1)))           # False
