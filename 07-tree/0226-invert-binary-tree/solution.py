"""
[0226] Invert Binary Tree (Easy)
링크: https://leetcode.com/problems/invert-binary-tree/

## 문제

이진 트리의 root → 좌우 반전된 트리의 root 반환.

## 예시

Example 1: [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
Example 2: [2,1,3]         → [2,3,1]
Example 3: []              → []

## 조건

- 노드 개수: [0, 100]
- -100 <= Node.val <= 100

---

핵심 아이디어 (DFS 재귀):
    각 노드에서 left와 right를 swap.
    그 후 양쪽 서브트리에 대해 재귀.
    base case: None → 그대로 None 반환.

자료구조 / 패턴:
    - DFS 재귀 (Tree)
    - "각 노드에 같은 연산 적용" 패턴

시간복잡도: O(n) — 모든 노드 한 번씩 방문
공간복잡도: O(h) — 재귀 스택, h는 트리 높이

영어 멘트 (면접용):
    "I recursively swap each node's left and right children. The base case is a null
     node, which I return as-is. Each node is visited once, giving O(n) time and
     O(h) space for the recursion stack. BFS with a queue also works in O(n) time
     and O(w) space — useful when trees are very deep."

엣지 케이스:
    - 빈 트리: None 그대로
    - 노드 한 개: 그대로 (자식 없음)
    - 한쪽으로만 뻗은 트리: 반대쪽으로 뻗어진 트리

## 손 추적 (Hand Trace)
# 트리:        4
#            /   \
#           2     7
#          / \   / \
#         1   3 6   9
#
# 재귀 호출 (postorder 시각):
#   invertTree(4):
#     invertTree(2):
#       invertTree(1) → 1 (자식 없음, swap 무의미)
#       invertTree(3) → 3
#       2.left, 2.right = 3, 1                  # swap
#       return 2
#     invertTree(7):
#       invertTree(6) → 6
#       invertTree(9) → 9
#       7.left, 7.right = 9, 6                  # swap
#       return 7
#     4.left, 4.right = 7, 2                    # swap
#     return 4
#
# 결과 트리:    4
#             /   \
#            7     2
#           / \   / \
#          9   6 3   1
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


# BFS 버전 (대안 — 재귀 한도 회피용)
# def invertTree(root):
#     if not root:
#         return None
#     q = deque([root])
#     while q:
#         node = q.popleft()
#         node.left, node.right = node.right, node.left
#         if node.left:  q.append(node.left)
#         if node.right: q.append(node.right)
#     return root


def to_level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    print(to_level_order(invertTree(root)))    # [4, 7, 2, 9, 6, 3, 1]

    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(to_level_order(invertTree(root2)))   # [2, 3, 1]

    print(to_level_order(invertTree(None)))    # []
