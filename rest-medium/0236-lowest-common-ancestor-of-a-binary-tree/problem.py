"""
[0236] Lowest Common Ancestor of a Binary Tree (Medium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## 문제

이진 트리의 root와 두 노드 p, q가 주어진다.
p와 q의 **lowest common ancestor (LCA)** 노드를 반환하라.
(노드는 자기 자신의 후손이 될 수 있다)

## 예시

Example 1:
    Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3

Example 2:
    Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5

Example 3:
    Input:  root = [1,2], p = 1, q = 2
    Output: 1

## 조건 (Constraints)

- 노드 개수: [2, 10^5]
- -10^9 <= Node.val <= 10^9
- 모든 노드 값 유일
- p, q는 트리에 존재하며 서로 다름
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass


if __name__ == "__main__":
    # [3,5,1,6,2,0,8,null,null,7,4]
    n7 = TreeNode(7); n4 = TreeNode(4)
    n2 = TreeNode(2, n7, n4)
    n6 = TreeNode(6); n0 = TreeNode(0); n8 = TreeNode(8)
    n5 = TreeNode(5, n6, n2); n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    print(lowestCommonAncestor(root, n5, n1).val)   # 3
    print(lowestCommonAncestor(root, n5, n4).val)   # 5
