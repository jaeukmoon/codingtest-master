"""
[0200] Number of Islands (Medium)
링크: https://leetcode.com/problems/number-of-islands/

## 문제

2D grid에서 '1'로 연결된 영역(island)의 개수.

## 예시

Example 1: 한 덩어리 → 1
Example 2: 세 덩어리 → 3

## 조건

- 1 <= m, n <= 300

---

핵심 아이디어 (DFS):
    모든 칸을 순회. '1'을 만나면 island 카운트 +1, DFS로 그 island에 연결된 모든 '1'을
    '0'으로 침몰시킴 (visited 표시). 이미 침몰된 '1'은 다시 안 셈.

자료구조 / 패턴:
    - 2D Grid DFS (또는 BFS)
    - in-place visited ('1' → '0')

시간복잡도: O(m * n) — 각 칸 한 번
공간복잡도: O(m * n) 최악 (재귀 스택, 한 island가 전체일 때)

영어 멘트 (면접용):
    "I scan every cell. When I hit a '1', I increment the island count and run DFS
     to sink the entire connected component to '0', marking it visited.
     Each cell is processed once, so O(m*n) time."

엣지 케이스:
    - 모두 물 ('0'): 0
    - 모두 육지 ('1'): 1
    - 대각선으로만 닿은 '1'들: 별개의 island (4방향만 연결)

## 손 추적 (Hand Trace)
# grid = [["1","1","0"],
#         ["0","1","0"],
#         ["0","0","1"]]
#
# 순회:
#  (0,0)='1' → count=1, DFS:
#    sink (0,0)→'0'
#    하 (1,0)='0' → return
#    우 (0,1)='1' → sink→'0'
#      하 (1,1)='1' → sink→'0'  (주변 다 '0'이거나 범위 밖)
#      우 (0,2)='0' → return
#  → island 1 침몰 완료. grid 왼쪽 위 영역 다 '0'.
#
#  (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1) 모두 '0' → skip
#  (2,2)='1' → count=2, DFS: sink (2,2)→'0' (주변 다 '0')
#
# return 2
"""
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def sink(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '0'        # visited 표시 (침몰)
        sink(r - 1, c)
        sink(r + 1, c)
        sink(r, c - 1)
        sink(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                sink(r, c)

    return count


# BFS 버전 (대안 — 재귀 한도 회피용)
# from collections import deque
# def numIslands(grid):
#     if not grid: return 0
#     rows, cols = len(grid), len(grid[0])
#     count = 0
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == '1':
#                 count += 1
#                 q = deque([(r, c)])
#                 grid[r][c] = '0'
#                 while q:
#                     cr, cc = q.popleft()
#                     for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
#                         nr, nc = cr+dr, cc+dc
#                         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
#                             grid[nr][nc] = '0'
#                             q.append((nr, nc))
#     return count


if __name__ == "__main__":
    g1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(g1))   # 1

    g2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(g2))   # 3
