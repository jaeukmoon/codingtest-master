"""
[0226] Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

## 문제

이진 트리의 root가 주어진다.
트리를 뒤집어서(좌우 반전) 새 root를 반환하라.

## 예시

Example 1:
    Input:  root = [4,2,7,1,3,6,9]
            (트리:        4               4
                        /   \           /   \
                       2     7  →      7     2
                      / \   / \       / \   / \
                     1   3 6   9     9   6 3   1  )
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input:  root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input:  root = []
    Output: []

## 조건 (Constraints)

- 노드 개수: [0, 100]
- -100 <= Node.val <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    pass


def to_level_order(root):
    """트리 → 레벨 순회 리스트 (None 포함)"""
    if not root:
        return []
    from collections import deque
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
    # Example 1: [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    print(to_level_order(invertTree(root)))    # Expected: [4, 7, 2, 9, 6, 3, 1]

    # Example 2: [2,1,3] → [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(to_level_order(invertTree(root2)))   # Expected: [2, 3, 1]

    # Example 3: 빈 트리
    print(to_level_order(invertTree(None)))    # Expected: []
