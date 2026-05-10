"""
[0021] Merge Two Sorted Lists (Easy)
링크: https://leetcode.com/problems/merge-two-sorted-lists/

## 문제

정렬된 두 연결 리스트를 하나로 합쳐서 정렬된 리스트의 head를 반환하라.
(노드를 새로 만들지 말고 기존 노드의 next만 재배치)

## 예시

Example 1:
    Input:  list1=[1,2,4], list2=[1,3,4]   →   Output: [1,1,2,3,4,4]
Example 2:
    Input:  [], []                          →   Output: []
Example 3:
    Input:  [], [0]                         →   Output: [0]

## 조건

- 노드 개수: 각 [0, 50]
- -100 <= Node.val <= 100
- 두 리스트는 비내림차순 정렬됨

---

핵심 아이디어 (Dummy Node + Two Pointers):
    결과의 head가 list1의 첫 노드일지 list2의 첫 노드일지 처음엔 모른다.
    → 가짜 dummy를 앞에 두고, tail을 한 칸씩 전진시키며 더 작은 노드를 붙인다.
    → 한쪽이 끝나면 남은 쪽을 통째로 tail.next에 이어 붙인다 (이미 정렬돼 있으므로).
    → 진짜 head는 dummy.next.

자료구조 / 패턴:
    - Dummy node (head 분기 제거용)
    - Two pointers (정렬 머지)
    - 노드 재사용 (in-place)

시간복잡도: O(n + m) — 두 리스트 길이 합만큼 비교
공간복잡도: O(1) — 새 노드 0개, 포인터만

영어 멘트 (면접용):
    "I'll use a dummy head and a tail pointer. While both lists have nodes,
     I attach the smaller one to tail and advance. When one list ends,
     I splice the remaining list onto tail.next. Return dummy.next.
     O(n+m) time, O(1) space — no new nodes."

엣지 케이스:
    - 한쪽 또는 양쪽이 빈 리스트: while 루프 진입 안 함, tail.next = l1 or l2가 처리
    - 한쪽이 다른 쪽보다 훨씬 김: 끝난 후 남은 거 통째 연결
    - 동점 (l1.val == l2.val): <= 로 비교했으므로 stable, l1을 먼저 붙임

## 손 추적 (Hand Trace) — list1=[1,2,4], list2=[1,3,4]

# 초기:  dummy→None,  tail=dummy
#        l1=1→2→4,  l2=1→3→4
#
# [1턴]  l1.val=1, l2.val=1  →  1 <= 1 이므로 l1 붙임
#        tail.next = l1   →   dummy→1(l1)→2→4
#        l1 = 2→4
#        tail = 1(l1)
#
# [2턴]  l1.val=2, l2.val=1  →  l2 붙임
#        tail.next = l2   →   dummy→1→1(l2)→3→4
#        l2 = 3→4
#        tail = 1(l2)
#
# [3턴]  l1.val=2, l2.val=3  →  l1
#        tail.next = l1   →   dummy→1→1→2→4
#        l1 = 4
#        tail = 2
#
# [4턴]  l1.val=4, l2.val=3  →  l2
#        tail.next = l2   →   dummy→1→1→2→3→4
#        l2 = 4
#        tail = 3
#
# [5턴]  l1.val=4, l2.val=4  →  l2 (<=)
#        tail.next = l2   →   dummy→1→1→2→3→4(l2)
#        l2 = None
#        tail = 4(l2)
#
# while 종료 (l2 == None).
# 남은 부분 연결:  tail.next = l1 or l2 = l1 = 4(l1)→None
#                  →  dummy→1→1→2→3→4→4→None
#
# return dummy.next = 1→1→2→3→4→4  ✓
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode],
                  list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next


# 재귀 버전 (대안)
# def mergeTwoLists(l1, l2):
#     if not l1: return l2
#     if not l2: return l1
#     if l1.val <= l2.val:
#         l1.next = mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = mergeTwoLists(l1, l2.next)
#         return l2


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
    print(to_list(mergeTwoLists(build([1, 5, 9]), build([2]))))          # [1,2,5,9]
