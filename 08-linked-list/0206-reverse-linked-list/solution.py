"""
[0206] Reverse Linked List (Easy)
링크: https://leetcode.com/problems/reverse-linked-list/

## 문제

단일 연결 리스트의 head가 주어진다. 리스트를 뒤집어 새 head를 반환하라.

## 예시

Example 1:
    Input:  [1,2,3,4,5]   →   Output: [5,4,3,2,1]
Example 2:
    Input:  [1,2]         →   Output: [2,1]
Example 3:
    Input:  []            →   Output: []

## 조건

- 노드 개수: [0, 5000]
- -5000 <= Node.val <= 5000

---

핵심 아이디어 (포인터 뒤집기, prev/cur/nxt 3총사):
    각 노드의 next를 "이전 노드"로 다시 꽂는다.
    단, 끊기 전에 원래 다음 노드를 nxt에 임시 저장해야 잃어버리지 않는다.

    while cur:
        nxt = cur.next      # 1. 다음 노드 백업
        cur.next = prev     # 2. 화살표 뒤집기
        prev = cur          # 3. prev 한 칸 전진
        cur = nxt           # 4. cur 한 칸 전진

자료구조 / 패턴:
    - 연결 리스트 포인터 조작
    - "prev / cur / nxt" 3 포인터 패턴 (뒤집기의 정석)

시간복잡도: O(n) — 노드 한 번씩 방문
공간복잡도: O(1) — 포인터 3개만 사용 (재귀가 아닌 반복)

영어 멘트 (면접용):
    "I'll iterate with three pointers: prev, cur, and a temp for cur.next.
     Each step I save next, flip cur.next to prev, then advance both.
     When cur becomes null, prev is the new head. O(n) time, O(1) space."

엣지 케이스:
    - 빈 리스트: head=None → 루프 진입 안 함 → prev=None 그대로 반환
    - 노드 1개: 첫 턴에서 cur.next=None 됨, prev=노드 그대로 반환

## 손 추적 (Hand Trace) — [1,2,3]

# 초기:  prev=None,  cur=1→2→3→None
#
# 1턴:   nxt = 2→3→None
#        cur.next = prev   →   1→None
#        prev = 1→None
#        cur  = 2→3→None
#
# 2턴:   nxt = 3→None
#        cur.next = prev   →   2→1→None
#        prev = 2→1→None
#        cur  = 3→None
#
# 3턴:   nxt = None
#        cur.next = prev   →   3→2→1→None
#        prev = 3→2→1→None
#        cur  = None       ← 종료
#
# return prev = 3→2→1→None  ✓
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


# 재귀 버전 (대안)
# def reverseList(head):
#     if not head or not head.next:
#         return head
#     new_head = reverseList(head.next)
#     head.next.next = head    # 뒤 노드의 next를 자기 자신으로
#     head.next = None         # 자기 next 끊기 (사이클 방지)
#     return new_head


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
    print(to_list(reverseList(build([1, 2, 3, 4, 5]))))   # [5,4,3,2,1]
    print(to_list(reverseList(build([1, 2]))))             # [2,1]
    print(to_list(reverseList(build([]))))                 # []
    print(to_list(reverseList(build([7]))))                # [7]
