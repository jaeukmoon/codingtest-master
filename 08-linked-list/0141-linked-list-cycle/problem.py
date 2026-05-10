"""
[0141] Linked List Cycle (Easy)
https://leetcode.com/problems/linked-list-cycle/

## 문제

연결 리스트의 head가 주어진다.
리스트에 사이클이 존재하면 True, 아니면 False를 반환하라.

(사이클 = 어떤 노드의 next를 따라가다 보면 다시 그 노드로 돌아오는 경우)

## 예시

Example 1:
    Input:  head = [3,2,0,-4], pos = 1   (tail이 index=1 노드와 연결)
    Output: True

Example 2:
    Input:  head = [1,2], pos = 0
    Output: True

Example 3:
    Input:  head = [1], pos = -1   (사이클 없음)
    Output: False

## 조건 (Constraints)

- 노드 개수: [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos는 -1 또는 [0, n-1]
- Follow-up: O(1) 메모리로 풀어보세요.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    pass


# --- 테스트 헬퍼 ---
def build_with_cycle(values, pos):
    """values로 리스트 만들고, pos != -1이면 tail.next를 values[pos] 노드로 연결."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    print(hasCycle(build_with_cycle([3, 2, 0, -4], 1)))   # Expected: True
    print(hasCycle(build_with_cycle([1, 2], 0)))           # Expected: True
    print(hasCycle(build_with_cycle([1], -1)))             # Expected: False
    print(hasCycle(build_with_cycle([], -1)))              # Expected: False
