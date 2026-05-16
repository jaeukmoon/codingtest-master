"""
[0200] Number of Islands — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **대각선도 인접인가요?**
  → 아니요, 상하좌우 4방향만. (8방향이면 변종 문제)
- **입력 grid 수정해도 되나요?**
  → 보통 OK. visited 셋 대신 grid를 직접 '0'으로 덮어쓰면 공간 절약.
  → "수정 안 됨"이라고 하면 visited set이나 별도 배열 필요.
- **값 타입**: '1'/'0' 문자(string)? 정수? — 문제는 문자열.
- **grid가 비어있을 수도?** 제약상 1×1 이상.

## 2. 엣지 케이스

- 전부 물 → 0
- 전부 육지 → 1
- 1×1 그리드 ([[0]] 또는 [[1]])
- 대각선으로만 닿는 두 1 → 두 개 island
- 매우 큰 그리드 300×300 — DFS 깊이가 9만까지 갈 수 있음 → **재귀 한계 위험!**
  → BFS(큐) 또는 iterative DFS(스택)가 더 안전.

## 3. 알고리즘 선택

### Connected components 문제 → 3가지 표준 풀이
1. **DFS** (재귀 or 스택)
2. **BFS** (큐)
3. **Union-Find**

### 트레이드오프
- DFS 재귀: 코드 짧지만 큰 그리드에서 stack overflow.
- BFS: deque 사용, 안전. 채택.
- Union-Find: 동적으로 grid가 변하는 변종(LC 305)에 적합. 정적 문제엔 과함.

### 채택: BFS + grid in-place 마킹
- 칸 (r,c)가 '1'이면 카운트++ 하고 거기서 BFS 시작.
- BFS 시작점에서 출발해 닿는 모든 '1'을 '0'으로 덮어 "방문" 표시.
- 다음 칸으로 진행.

방문 표시를 grid 자체에 하면 visited set 없이 O(1) 추가 공간.
"입력 수정 안 됨"이 제약이면 visited 셋으로 변경.

## 4. 복잡도

- 시간: O(m * n) — 각 칸 최대 한 번 방문
- 공간: O(min(m, n)) — BFS 큐 최대 크기 (그리드 한 변)
"""
from typing import List
from collections import deque


def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 예시 grid:
    #   1 1 0 0
    #   1 0 0 0
    #   0 0 1 1
    #
    # (0,0)='1' → count=1, BFS 시작
    #   큐: [(0,0)] → grid[0][0]='0'
    #   pop (0,0) → 이웃 (0,1)='1' → grid[0][1]='0', 큐에 추가
    #             → 이웃 (1,0)='1' → grid[1][0]='0', 큐에 추가
    #   pop (0,1) → 이웃 중 '1' 없음
    #   pop (1,0) → 이웃 중 '1' 없음
    #   → 첫 번째 섬 완료, 방문한 칸은 전부 '0'으로 변경됨
    #
    # (0,1)~(1,1) → 이미 '0'이라 skip
    # (2,2)='1' → count=2, BFS로 (2,2),(2,3) 처리 → 두 번째 섬
    # 최종 count = 2

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '1':
                continue

            count += 1
            queue = deque([(r, c)])
            grid[r][c] = '0'

            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

    return count


if __name__ == "__main__":
    g1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(numIslands(g1))   # 1

    g2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(numIslands(g2))   # 3

    print(numIslands([["0"]]))   # 0
    print(numIslands([["1"]]))   # 1
