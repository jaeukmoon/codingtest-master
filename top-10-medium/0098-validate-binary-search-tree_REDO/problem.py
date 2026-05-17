"""
[0098] Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

## 문제

이진 트리의 root가 주어진다. 유효한 BST인지 확인하라.

유효한 BST의 정의:
- 노드의 왼쪽 서브트리는 그 노드의 값보다 **작은** 값만 포함
- 노드의 오른쪽 서브트리는 그 노드의 값보다 **큰** 값만 포함
- 양쪽 서브트리도 모두 BST여야 한다

## 예시

Example 1:
    Input:  root = [2,1,3]
            (트리:    2
                     / \
                    1   3 )
    Output: true

Example 2:
    Input:  root = [5,1,4,null,null,3,6]
            (트리:        5
                        /   \
                       1     4
                            / \
                           3   6 )
    Output: false
    Explanation: 4 is right child of 5, but its left child 3 < 5 — invalid.

## 조건 (Constraints)

- 노드 개수: [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def isValidBST(root: Optional[TreeNode]) -> bool:
#     if root is None:
#         return True
#     if root.left:
#         if root.left.val>=root.val:
#             return False
#         else:
#             isValidBST(root.left)
#     if root.right:
#         if root.right.val<=root.val:
#             return False
#         else:
#             isValidBST(root.right)
#     return True

def isValidBST(root: Optional[TreeNode],lo = float('-inf'), hi = float('inf')) -> bool:
     # 1) None은 빈 트리 — 유효 (재귀의 종료 조건)
    if root is None:
        return True
    if root.val <= lo or root.val>=hi:
        return False
    
    if not isValidBST(root.left,lo,root.val):
        return False
    if not isValidBST(root.right, root.val, hi):
        return False
    return True

if __name__ == "__main__":
    # [2,1,3]
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(isValidBST(t1))   # Expected: True

    # [5,1,4,null,null,3,6]
    t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(isValidBST(t2))   # Expected: False
