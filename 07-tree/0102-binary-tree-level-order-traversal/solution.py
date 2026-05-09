"""
[0102] Binary Tree Level Order Traversal (Medium)
링크: https://leetcode.com/problems/binary-tree-level-order-traversal/

## 문제

이진 트리의 root → 레벨 순회 결과를 list of lists로 반환.
(레벨별로 묶어서, 왼쪽에서 오른쪽 순)

## 예시

Example 1: [3,9,20,null,null,15,7] → [[3], [9,20], [15,7]]
Example 2: [1]                      → [[1]]
Example 3: []                       → []

## 조건

- 노드 개수: [0, 2000]
- -1000 <= Node.val <= 1000

---

핵심 아이디어 (BFS의 정석):
    deque에 root 넣고 시작.
    매 레벨마다 "현재 큐 길이"를 미리 저장 → 그만큼만 처리해서 한 레벨 완성.
    각 노드의 자식을 다음 레벨용으로 큐에 추가.

자료구조 / 패턴:
    - BFS (collections.deque)
    - "레벨별 처리" 패턴: for _ in range(len(q))

시간복잡도: O(n) — 모든 노드 한 번씩
공간복잡도: O(w) — 큐 최대 크기, w는 트리의 최대 너비

영어 멘트 (면접용):
    "I'll use BFS with a queue. For each level, I capture the current queue size
     and process exactly that many nodes — they form the level. Each node's children
     are appended to the queue for the next level."

엣지 케이스:
    - 빈 트리: []
    - 노드 하나: [[val]]
    - skewed 트리: 각 레벨에 1개씩

## 손 추적 (Hand Trace)
# 트리:        3
#            /   \
#           9    20
#               /  \
#              15   7
#
# 초기:  q = [3]                    result = []
#
# 레벨 1: len(q)=1, 1번 처리
#   pop 3 → level=[3], q에 9, 20 추가
#   q = [9, 20]                    result = [[3]]
#
# 레벨 2: len(q)=2, 2번 처리
#   pop 9  → level=[9],   자식 없음
#   pop 20 → level=[9,20], q에 15, 7 추가
#   q = [15, 7]                    result = [[3], [9,20]]
#
# 레벨 3: len(q)=2, 2번 처리
#   pop 15 → level=[15],   자식 없음
#   pop 7  → level=[15,7], 자식 없음
#   q = []                         result = [[3], [9,20], [15,7]]
#
# q 비어서 종료 → return [[3], [9,20], [15,7]] ✓
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):       # 현재 레벨 크기만큼만 처리
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)

    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(levelOrder(root))         # [[3], [9,20], [15,7]]
    print(levelOrder(TreeNode(1)))  # [[1]]
    print(levelOrder(None))         # []
