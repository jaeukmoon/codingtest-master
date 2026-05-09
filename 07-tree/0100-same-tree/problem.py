"""
[0100] Same Tree (Easy)
https://leetcode.com/problems/same-tree/

## 문제

두 이진 트리의 root `p`와 `q`가 주어진다.
두 트리가 같으면 `true`, 다르면 `false`를 반환하라.
(같다 = 구조도 같고 모든 노드 값도 같다)

## 예시

Example 1:
    Input:  p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input:  p = [1,2], q = [1,null,2]
    Output: false
    Explanation: 같은 값이지만 구조가 다름.

Example 3:
    Input:  p = [1,2,1], q = [1,1,2]
    Output: false

## 조건 (Constraints)

- 두 트리의 노드 개수: [0, 100]
- -10^4 <= Node.val <= 10^4
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    pass


if __name__ == "__main__":
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(isSameTree(p1, q1))   # Expected: True

    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(isSameTree(p2, q2))   # Expected: False

    print(isSameTree(None, None))                # Expected: True
    print(isSameTree(TreeNode(1), None))         # Expected: False
