"""
[0104] Maximum Depth of Binary Tree (Easy)
https://leetcode.com/problems/maximum-depth-of-binary-tree/

## 문제

이진 트리의 root가 주어진다.
트리의 최대 깊이(루트에서 가장 먼 leaf까지 노드 수)를 반환하라.

## 예시

Example 1:
    Input:  root = [3,9,20,null,null,15,7]
            (트리:        3
                        /   \
                       9    20
                           /  \
                          15   7  )
    Output: 3

Example 2:
    Input:  root = [1,null,2]
    Output: 2

## 조건 (Constraints)

- 노드 개수: [0, 10^4]
- -100 <= Node.val <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    pass


if __name__ == "__main__":
    # 트리: [3,9,20,null,null,15,7]
    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maxDepth(root))           # Expected: 3

    print(maxDepth(TreeNode(1, None, TreeNode(2))))   # Expected: 2
    print(maxDepth(None))           # Expected: 0
