"""
[0102] Binary Tree Level Order Traversal (Medium)
https://leetcode.com/problems/binary-tree-level-order-traversal/

## 문제

이진 트리의 root가 주어진다.
레벨 순회(level order) 결과를 반환하라.
(왼쪽에서 오른쪽으로, 레벨별로 묶어서 list of lists)

## 예시

Example 1:
    Input:  root = [3,9,20,null,null,15,7]
            (트리:       3
                       /   \
                      9    20
                          /  \
                         15   7  )
    Output: [[3], [9,20], [15,7]]

Example 2:
    Input:  root = [1]
    Output: [[1]]

Example 3:
    Input:  root = []
    Output: []

## 조건 (Constraints)

- 노드 개수: [0, 2000]
- -1000 <= Node.val <= 1000
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(levelOrder(root))         # Expected: [[3], [9,20], [15,7]]

    print(levelOrder(TreeNode(1)))  # Expected: [[1]]
    print(levelOrder(None))         # Expected: []
