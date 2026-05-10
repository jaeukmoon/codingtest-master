"""
[0021] Merge Two Sorted Lists (Easy)
링크: https://leetcode.com/problems/merge-two-sorted-lists/

## 문제

두 정렬된 연결 리스트를 하나로 합쳐 정렬된 리스트 반환. 노드 재사용.

## 예시

Example 1: list1=[1,2,4], list2=[1,3,4] → [1,1,2,3,4,4]

## 조건

- 노드 개수: [0, 50], -100 <= val <= 100
- 두 리스트 모두 오름차순 정렬

---

핵심 아이디어:
    Dummy 노드 + tail 포인터.
    list1, list2 비교해서 작은 쪽을 tail.next에 연결, 그 리스트의 포인터 한 칸 전진.
    한쪽 끝나면 남은 쪽을 그대로 이어붙임.
    dummy.next 반환.

자료구조 / 패턴:
    - Linked List + Dummy node (head 케이스 단순화)

시간복잡도: O(n + m)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I use a dummy node to simplify head handling. I maintain a tail pointer and
     compare the heads of both lists, attaching the smaller one. When one list is
     exhausted, I attach the remainder of the other. O(n+m) time, O(1) space."

엣지 케이스:
    - 한쪽이 빈 리스트: 다른 쪽 그대로
    - 둘 다 빈 리스트: None
    - 같은 값일 때 어느 쪽 먼저든 OK

## 손 추적 (Hand Trace)
# list1 = 1 → 2 → 4
# list2 = 1 → 3 → 4
#
# 초기:  dummy → ?, tail = dummy
#
#  step | l1   | l2   | 비교       | tail.next 연결 | tail 전진
# ------|------|------|-----------|---------------|----------
#   1   | 1    | 1    | 1 <= 1    | tail → l1(1)  | tail = 1, l1 = 2
#   2   | 2    | 1    | 2 > 1     | tail → l2(1)  | tail = 1, l2 = 3
#   3   | 2    | 3    | 2 <= 3    | tail → l1(2)  | tail = 2, l1 = 4
#   4   | 4    | 3    | 4 > 3     | tail → l2(3)  | tail = 3, l2 = 4
#   5   | 4    | 4    | 4 <= 4    | tail → l1(4)  | tail = 4, l1 = None
#   루프 종료. l2 남음 → tail.next = l2 (4 → None)
#
# return dummy.next = 1 → 1 → 2 → 3 → 4 → 4
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # 남은 쪽 그대로 이어붙임
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


def to_list(head):
    r = []
    while head:
        r.append(head.val)
        head = head.next
    return r


def from_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(mergeTwoLists(from_list([1,2,4]), from_list([1,3,4]))))   # [1,1,2,3,4,4]
    print(to_list(mergeTwoLists(from_list([]), from_list([]))))               # []
    print(to_list(mergeTwoLists(from_list([]), from_list([0]))))              # [0]
