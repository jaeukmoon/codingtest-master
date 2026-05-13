"""
[0695] Max Area of Island (Medium)
링크: https://leetcode.com/problems/max-area-of-island/

## 문제

2D grid에서 가장 큰 island의 면적 반환.

## 예시

Example 1: 위 8x13 grid → 6
Example 2: 모두 0 → 0

## 조건

- 1 <= m, n <= 50

---

핵심 아이디어 (DFS):
    각 1 칸에서 시작해 4방향 DFS로 연결된 1을 모두 탐색.
    탐색하면서 면적 카운트, visited 표시 (in-place로 0 만들면 메모리 절약).
    모든 칸을 한 번씩 보면서 최대 면적 갱신.

자료구조 / 패턴:
    - 2D Grid DFS (재귀)
    - in-place visited 표시 (1을 0으로 변경)

시간복잡도: O(m * n) — 각 칸 한 번씩
공간복잡도: O(m * n) 최악 (재귀 스택, 한 island가 그리드 전체일 때)

영어 멘트 (면접용):
    "I scan every cell. When I find a '1', I run DFS to count all connected land,
     marking visited cells as '0' to avoid revisiting. I keep track of the max area.
     O(m*n) time and O(m*n) worst case space for recursion."

엣지 케이스:
    - 모두 물 (0): 0
    - 모두 육지 (1): m * n
    - 그리드 가장자리에 island

## 손 추적 (Hand Trace)
# 작은 예: grid = [[1,1,0],
#                  [1,0,1]]
#
# 칸 (0,0) = 1 → DFS 시작
#   visit (0,0), area=1, mark 0
#     상: 범위 밖
#     하: (1,0) = 1 → DFS
#       visit (1,0), area=2, mark 0
#         상: (0,0) 이미 0
#         하: 범위 밖
#         좌: 범위 밖
#         우: (1,1) = 0
#     좌: 범위 밖
#     우: (0,1) = 1 → DFS
#       visit (0,1), area=3, mark 0
#         (다 0이거나 범위 밖) → return
# island 1: area = 3, max_area = 3
#
# 칸 (1,2) = 1 → DFS → area = 1
# island 2: area = 1, max_area = 3
#
# return 3
"""
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        # 경계 + 물 체크
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] == 0:
            return 0

        grid[r][c] = 0   # visited 표시 (in-place)
        area = 1
        area += dfs(r - 1, c)
        area += dfs(r + 1, c)
        area += dfs(r, c - 1)
        area += dfs(r, c + 1)
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = dfs(r, c)
                if area > max_area:
                    max_area = area

    return max_area


if __name__ == "__main__":
    g1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print(maxAreaOfIsland(g1))   # 6
    print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))   # 0
    print(maxAreaOfIsland([[1]]))                   # 1
