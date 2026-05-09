"""
[0104] Maximum Depth of Binary Tree (Easy)
링크: https://leetcode.com/problems/maximum-depth-of-binary-tree/

## 문제

이진 트리의 root가 주어진다.
트리의 최대 깊이(루트에서 가장 먼 leaf까지 노드 수)를 반환하라.

## 예시

Example 1:
    Input:  [3,9,20,null,null,15,7]   →   Output: 3
Example 2:
    Input:  [1,null,2]                →   Output: 2

## 조건

- 노드 개수: [0, 10^4]
- -100 <= Node.val <= 100

---

핵심 아이디어 (DFS 재귀):
    노드의 깊이 = 1 + max(왼쪽 서브트리 깊이, 오른쪽 서브트리 깊이)
    base case: None → 0

자료구조 / 패턴:
    - DFS (재귀)
    - Tree 재귀 사고의 정석

시간복잡도: O(n) — 모든 노드 한 번씩 방문
공간복잡도: O(h) — 재귀 스택, h는 트리 높이 (최악 O(n))

영어 멘트 (면접용):
    "I'll use recursion. The depth of a node is 1 plus the max depth of its children.
     Base case: a null node has depth 0. This visits each node once, O(n) time."

엣지 케이스:
    - 빈 트리: 0
    - 한쪽으로만 뻗은 트리(skewed): 깊이 = 노드 수
    - 균형 트리: 깊이 ≈ log₂(n)

## 손 추적 (Hand Trace)
# 트리:        3        ← maxDepth(3) = 1 + max(L, R)
#            /   \
#           9    20      ← maxDepth(9) = 1 + 0 = 1
#               /  \         maxDepth(20) = 1 + max(1, 1) = 2
#              15   7    ← maxDepth(15) = 1, maxDepth(7) = 1
#
# 호출 흐름 (재귀 트리):
#   maxDepth(3)
#   ├─ maxDepth(9)  = 1 + max(maxDepth(None), maxDepth(None)) = 1 + 0 = 1
#   └─ maxDepth(20) = 1 + max(maxDepth(15), maxDepth(7))      = 1 + 1 = 2
#                                                                       ↓
#   return 1 + max(1, 2) = 3
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# BFS 버전 (대안)
# from collections import deque
# def maxDepth(root):
#     if not root:
#         return 0
#     q = deque([root])
#     depth = 0
#     while q:
#         depth += 1
#         for _ in range(len(q)):
#             node = q.popleft()
#             if node.left:  q.append(node.left)
#             if node.right: q.append(node.right)
#     return depth


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maxDepth(root))                              # 3
    print(maxDepth(TreeNode(1, None, TreeNode(2))))    # 2
    print(maxDepth(None))                              # 0
