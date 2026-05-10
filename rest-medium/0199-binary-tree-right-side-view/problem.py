"""
[0199] Binary Tree Right Side View (Medium)
https://leetcode.com/problems/binary-tree-right-side-view/

## 문제

이진 트리의 root가 주어진다.
오른쪽에서 봤을 때 보이는 노드 값들을 위→아래 순서로 반환하라.

## 예시

Example 1:
    Input:  root = [1,2,3,null,5,null,4]
            (트리:    1
                     / \
                    2   3
                     \   \
                      5   4 )
    Output: [1,3,4]

Example 2:
    Input:  root = [1,null,3]
    Output: [1,3]

Example 3:
    Input:  root = []
    Output: []

## 조건 (Constraints)

- 노드 개수: [0, 100]
- -100 <= Node.val <= 100
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    pass


if __name__ == "__main__":
    t1 = TreeNode(1,
                  TreeNode(2, None, TreeNode(5)),
                  TreeNode(3, None, TreeNode(4)))
    print(rightSideView(t1))   # [1,3,4]
    print(rightSideView(TreeNode(1, None, TreeNode(3))))   # [1,3]
    print(rightSideView(None))                              # []
