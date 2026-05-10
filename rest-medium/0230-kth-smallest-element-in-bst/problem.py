"""
[0230] Kth Smallest Element in a BST (Medium)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## 문제

BST의 root와 정수 k가 주어진다.
**k번째로 작은** 값을 반환하라 (1-indexed).

## 예시

Example 1:
    Input:  root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:
    Input:  root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

## 조건 (Constraints)

- 노드 개수 == n
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

## Follow-up

BST가 자주 수정되고 k번째 작은 값을 자주 찾아야 한다면 어떻게 최적화할까?
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    pass


if __name__ == "__main__":
    # [3,1,4,null,2]
    t1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(kthSmallest(t1, 1))   # 1

    # [5,3,6,2,4,null,null,1]
    t2 = TreeNode(5,
                  TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                  TreeNode(6))
    print(kthSmallest(t2, 3))   # 3
