"""
[0141] Linked List Cycle (Easy)
링크: https://leetcode.com/problems/linked-list-cycle/

## 문제

연결 리스트에 사이클이 있으면 true, 없으면 false. O(1) 메모리.

## 예시

Example 1: head = [3,2,0,-4], pos = 1 → true (tail이 인덱스 1로 연결)

## 조건

- 노드 개수: [0, 10^4], -10^5 <= val <= 10^5

---

핵심 아이디어 (Floyd's Tortoise and Hare):
    포인터 두 개. slow는 1칸씩, fast는 2칸씩 전진.
    사이클 있으면 fast가 결국 slow를 따라잡음 (만남).
    사이클 없으면 fast가 None에 도달 → 종료.

자료구조 / 패턴:
    - Two Pointers (fast/slow)

시간복잡도: O(n)
공간복잡도: O(1)  ← Hash Set 쓰면 O(n)

영어 멘트 (면접용):
    "I'll use Floyd's tortoise and hare. Slow moves one step, fast moves two.
     If there's a cycle, fast eventually catches up to slow inside the loop.
     If no cycle, fast reaches None and we return False. O(n) time, O(1) space."

엣지 케이스:
    - 빈 리스트: False
    - 노드 1개 (자기 참조 없음): False
    - 노드 1개 자기 사이클: True (그러나 문제에서는 보통 pos 사용)

## 손 추적 (Hand Trace)
# 사이클 있는 케이스: [3,2,0,-4], pos=1 (-4의 next가 2)
#
# 그래프:    3 → 2 → 0 → -4
#                ↑________|
#
#  step | slow | fast       | 만남?
# ------|------|------------|------
#   0   |  3   |  3         | -
#   1   |  2   |  0         | NO
#   2   |  0   |  2         | NO
#   3   | -4   | -4         | YES → return True
#
# 사이클 없는 케이스: [1, 2, 3]
#  step | slow | fast       |
# ------|------|------------|
#   0   |  1   |  1         |
#   1   |  2   |  3         |
#   2   |  3   |  None      | fast가 None → return False
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# Hash Set 버전 (대안 — O(n) 메모리)
# def hasCycle(head):
#     visited = set()
#     while head:
#         if head in visited: return True
#         visited.add(head)
#         head = head.next
#     return False


def make_cycle(values, pos):
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
