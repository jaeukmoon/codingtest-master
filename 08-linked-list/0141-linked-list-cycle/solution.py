"""
[0141] Linked List Cycle (Easy)
링크: https://leetcode.com/problems/linked-list-cycle/

## 문제

연결 리스트에 사이클이 있으면 True, 없으면 False.

## 예시

Example 1:
    [3,2,0,-4], pos=1   →   True
Example 2:
    [1,2], pos=0        →   True
Example 3:
    [1], pos=-1         →   False

## 조건

- 노드 개수: [0, 10^4]
- Follow-up: O(1) 공간

---

핵심 아이디어 (Floyd's Cycle Detection — 거북이/토끼):
    slow는 1칸/턴, fast는 2칸/턴 같은 head에서 출발.
    - 사이클 없음: fast가 None에 먼저 닿아 종료 → False
    - 사이클 있음: 사이클 안에서 둘 사이 거리가 매 턴 1씩 줄어 결국 만남 → True

    while 조건은 fast and fast.next:
      fast가 2칸 가야 하므로 두 칸 앞까지 노드가 있어야 안전.

자료구조 / 패턴:
    - Two pointers (slow / fast)
    - 객체 동일성 비교 (`is`) — 값이 아니라 같은 노드인지

시간복잡도: O(n)
    - 사이클 없음: fast가 끝까지 — n/2 턴
    - 사이클 있음: 사이클 진입 후 최대 사이클 길이 L 만큼 → O(n + L) = O(n)
공간복잡도: O(1) — 포인터 2개

영어 멘트 (면접용):
    "I'll use Floyd's tortoise and hare. Slow moves one step, fast moves two.
     If there's no cycle, fast hits null and we return false.
     If there is one, fast catches up to slow inside the loop — relative speed
     is 1, so they meet within L steps where L is cycle length.
     O(n) time, O(1) space."

엣지 케이스:
    - 빈 리스트 (head=None): while 조건 즉시 False → return False
    - 노드 1개 + 사이클 없음: fast.next=None → 즉시 False
    - 노드 1개 + 자기 자신 사이클: 1턴 후 만남 → True
    - 두 노드 사이클: 2~3턴 안에 만남

## 손 추적 (Hand Trace)

# 케이스 A: [3,2,0,-4], tail이 index 1로 연결
#
# 구조:   [3] → [2] → [0] → [-4]
#                ↑___________|
#
# 초기:   slow=fast=[3]
# [1턴]   slow=[2],   fast=[0]                        slow ≠ fast
# [2턴]   slow=[0],   fast=[2]   (-4 → 2)             slow ≠ fast
# [3턴]   slow=[-4],  fast=[-4]  (2 → 0 → -4)         slow == fast → True ✓
#
# 케이스 B: [1,2], 사이클 없음
#
# 초기:   slow=fast=[1]
# [1턴]   slow=[2],   fast=[1].next.next = None
# while 재검사: fast=None → 탈출 → False ✓
#
# 케이스 C: 빈 리스트
#
# slow=fast=None → while 조건 False → False ✓
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# Hash Set 버전 (O(n) 공간, 더 직관적)
# def hasCycle(head):
#     seen = set()
#     while head:
#         if head in seen:
#             return True
#         seen.add(head)
#         head = head.next
#     return False


# 사이클 시작 지점 찾기 (LeetCode 142, 보너스)
# def detectCycle(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow is fast:
#             slow = head
#             while slow is not fast:
#                 slow = slow.next
#                 fast = fast.next
#             return slow
#     return None


# --- 테스트 헬퍼 ---
def build_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    print(hasCycle(build_with_cycle([3, 2, 0, -4], 1)))   # True
    print(hasCycle(build_with_cycle([1, 2], 0)))           # True
    print(hasCycle(build_with_cycle([1], -1)))             # False
    print(hasCycle(build_with_cycle([], -1)))              # False
    print(hasCycle(build_with_cycle([1, 2, 3, 4, 5], -1))) # False
