"""
[0098] Validate Binary Search Tree — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **중복 값 허용?**
  → 문제 정의는 strictly less / strictly greater. 즉, **중복 금지**.
  (실무 BST는 중복 허용 변종도 있으니 확인 필요)
- **빈 트리는 valid?**
  → 보통 True. 제약조건상 노드 1개 이상이라 무관할 수도.
- **값 범위**: int32 전 범위 — sentinel로 ±inf 쓰는 게 안전 (sys.maxsize 대신 float('inf'))

## 2. 흔한 함정 (이 문제의 핵심)

가장 흔한 오답: "각 노드에서 left.val < node.val < right.val만 체크".
→ 이건 **로컬 조건**만 보는 것. BST는 **서브트리 전체**가 조건을 만족해야 함.

반례:
        10
       /  \
      5    15
          /  \
         6    20
- 15의 왼쪽 6 < 15 ✓, but 6은 root=10의 오른쪽 서브트리에 있으므로 6 > 10이어야 함.
- 로컬 체크만 하면 통과시켜 버림 → 오답.

## 3. 엣지 케이스

- 단일 노드 → True
- 왼쪽으로 길게 늘어진 트리 (degenerate)
- 깊이 큰 트리 (재귀 스택 한계) — 10^4까지면 Python 기본 재귀 한계(약 1000) 초과 가능
  → sys.setrecursionlimit 또는 iterative로 처리 검토
- 값이 INT_MIN/INT_MAX인 노드

## 4. 알고리즘 선택

### 방법 A: 재귀 + (lo, hi) 범위 전달 ← 채택
각 노드를 valid 범위 (lo, hi)와 함께 검사. 왼쪽으로 내려가면 hi를 현재 값으로,
오른쪽으로 내려가면 lo를 현재 값으로 좁힌다.

- 깔끔하고 직관적.
- 시간 O(n), 공간 O(h) — h=트리 높이.

### 방법 B: Inorder 순회 → 단조 증가 체크
BST의 inorder는 strictly increasing이어야 함. iterative inorder로 prev 값만 들고
다니면서 비교 → O(n) 시간, O(h) 공간. 큰 트리에서 stack overflow 회피용으로 좋음.

면접에서는 A로 풀고, "재귀 깊이가 걱정되면 B(iterative inorder)로 바꿀 수 있다"고 언급.

## 5. 복잡도

- 시간: O(n) — 각 노드 한 번 방문
- 공간: O(h) — 재귀 스택
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    # 예시 트리:
    #       5
    #      / \
    #     1   4       ← 4는 5의 오른쪽인데 4 < 5 → invalid!
    #        / \
    #       3   6

    def validate(node: Optional[TreeNode], lo: float, hi: float) -> bool:
        if node is None:
            return True
        if not (lo < node.val < hi):
            return False
        return (validate(node.left, lo, node.val)
                and validate(node.right, node.val, hi))

    # 호출 흐름 (위 트리 기준):
    # validate(5, -inf, inf) → -inf < 5 < inf ✓
    #   validate(1, -inf, 5) → -inf < 1 < 5 ✓
    #     validate(None, ...) → True (좌)
    #     validate(None, ...) → True (우)
    #   → True
    #   validate(4, 5, inf) → 5 < 4 < inf? → 5 < 4 ✗ → False!
    # → False (전체 invalid)
    #
    # 핵심: 오른쪽으로 내려갈 때 lo=5로 좁힘
    #       → 오른쪽 서브트리의 모든 값은 5보다 커야 함

    return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(isValidBST(t1))   # True

    t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(isValidBST(t2))   # False — 핵심 함정 케이스

    # 단일 노드
    print(isValidBST(TreeNode(1)))   # True

    # 중복 값 — strictly less/greater이므로 False여야 함
    t3 = TreeNode(1, TreeNode(1))
    print(isValidBST(t3))   # False
