"""
[0100] Same Tree (Easy)
링크: https://leetcode.com/problems/same-tree/

## 문제

두 이진 트리 root p, q가 주어진다.
두 트리가 같으면 true, 다르면 false 반환.
(같다 = 구조도 같고 모든 노드 값도 같다)

## 예시

Example 1: p=[1,2,3], q=[1,2,3] → true
Example 2: p=[1,2],   q=[1,null,2] → false (구조 다름)

## 조건

- 노드 개수: [0, 100]
- -10^4 <= Node.val <= 10^4

---

핵심 아이디어 (DFS 재귀):
    1) 둘 다 None → True (같음)
    2) 한쪽만 None → False (구조 다름)
    3) 값 다름 → False
    4) 둘 다 있고 값 같음 → 왼쪽 서브트리끼리 + 오른쪽 서브트리끼리 재귀

자료구조 / 패턴:
    - DFS 재귀, 두 트리 동시 순회

시간복잡도: O(min(n, m)) — 더 작은 트리 노드 수만큼만 탐색
공간복잡도: O(min(h_p, h_q)) — 재귀 스택

영어 멘트 (면접용):
    "I'll recurse on both trees simultaneously. If both nodes are null, they're equal.
     If only one is null, they differ. If values differ, return False. Otherwise recurse
     on left and right children with logical AND."

엣지 케이스:
    - 둘 다 빈 트리: True
    - 한쪽만 빈 트리: False
    - 값 같지만 구조 다름: False (예: [1,2] vs [1,null,2])

## 손 추적 (Hand Trace)
# p = [1,2,3]      q = [1,2,3]
#       1                1
#      / \              / \
#     2   3            2   3
#
# isSameTree(1,1):
#   둘 다 None? NO. 한쪽만 None? NO. 값 비교: 1==1 ✓
#   ├─ isSameTree(2, 2): 값 같음 → 왼쪽(None,None)→True, 오른쪽(None,None)→True → True
#   └─ isSameTree(3, 3): 위와 동일 → True
#   return True AND True = True ✓
#
# 실패 케이스 p=[1,2], q=[1,null,2]:
#       1              1
#      /                \
#     2                  2
#
# isSameTree(1,1): 값 같음
#   ├─ isSameTree(2, None): 한쪽만 None → return False ← 즉시 종료
#   └─ (실행 안 함, AND 단락)
#   return False
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    if not isSameTree(p.left, q.left):
        return False
    if not isSameTree(p.right, q.right):
        return False
    return True


# 한 줄 버전 (Pythonic — 면접 후 언급용)
# return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(isSameTree(p1, q1))   # True

    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(isSameTree(p2, q2))   # False

    print(isSameTree(None, None))                # True
    print(isSameTree(TreeNode(1), None))         # False
