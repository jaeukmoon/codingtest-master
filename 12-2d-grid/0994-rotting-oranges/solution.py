"""
[0994] Rotting Oranges (Medium)
링크: https://leetcode.com/problems/rotting-oranges/

## 문제

grid: 0(빈칸), 1(신선), 2(썩음). 매 분 썩은 오렌지가 인접 신선 오렌지를 썩힘.
모두 썩는 최소 분. 불가능하면 -1.

## 예시

Example 1: [[2,1,1],[1,1,0],[0,1,1]] → 4
Example 2: 고립된 신선 오렌지 → -1
Example 3: 신선 오렌지 없음 → 0

## 조건

- 1 <= m, n <= 10

---

핵심 아이디어 (Multi-source BFS):
    "최단 시간" + "동시 확산" → BFS. 단, 시작점이 여러 개 (모든 썩은 오렌지).
    1) 처음에 모든 썩은 오렌지를 큐에 넣고 시작. 신선 오렌지 개수 카운트.
    2) BFS 한 레벨 = 1분. 레벨 처리할 때마다 minutes += 1.
       (단, 새로 썩은 게 하나도 없으면 minutes 증가 안 함 — 마지막 레벨 처리 후 빈 확산 방지)
    3) BFS 끝나고 신선 오렌지가 남았으면 -1, 아니면 minutes.

자료구조 / 패턴:
    - Multi-source BFS (deque, `len(q)` 레벨 트릭)

시간복잡도: O(m * n) — 각 칸 한 번
공간복잡도: O(m * n) — 큐

영어 멘트 (면접용):
    "This is multi-source BFS. I start with ALL rotten oranges in the queue and
     count fresh ones. Each BFS level represents one minute. After BFS, if any fresh
     orange remains, return -1; otherwise return the minutes elapsed."

엣지 케이스:
    - 신선 오렌지 0개: 0분 (BFS 안 돌아도 됨)
    - 고립된 신선 오렌지 (썩은 거랑 연결 안 됨): -1
    - 처음부터 다 썩어있음: 0

## 손 추적 (Hand Trace)
# grid = [[2,1,1],
#         [1,1,0],
#         [0,1,1]]
#
# 초기: 큐 = [(0,0)]  (썩은 오렌지 위치), fresh = 6, minutes = 0
#
# 레벨 1 (minutes → 1): pop (0,0)
#   인접: (0,1)신선→썩힘 fresh=5 큐추가, (1,0)신선→썩힘 fresh=4 큐추가
#   큐 = [(0,1),(1,0)]
#
# 레벨 2 (minutes → 2): pop (0,1), (1,0)
#   (0,1)→ (0,2)신선→썩힘 fresh=3, (1,1)신선→썩힘 fresh=2
#   (1,0)→ (1,1)이미 처리됨
#   큐 = [(0,2),(1,1)]
#
# 레벨 3 (minutes → 3): pop (0,2), (1,1)
#   (0,2)→ 인접 (1,2)=0 빈칸, 끝
#   (1,1)→ (2,1)신선→썩힘 fresh=1
#   큐 = [(2,1)]
#
# 레벨 4 (minutes → 4): pop (2,1)
#   (2,1)→ (2,2)신선→썩힘 fresh=0
#   큐 = [(2,2)]
#
# 레벨 5: pop (2,2) → 인접에 신선 오렌지 없음 → 새로 썩은 거 없음 → minutes 증가 안 함
# 큐 빔, fresh == 0 → return 4
"""
from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # 1) 초기 썩은 오렌지 큐에 + 신선 오렌지 카운트
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 2) Multi-source BFS, 레벨 = 1분
    while q and fresh > 0:
        minutes += 1
        for _ in range(len(q)):           # 현재 레벨(이번 분) 처리
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2      # 썩힘
                    fresh -= 1
                    q.append((nr, nc))

    # 3) 신선 오렌지 남았으면 -1
    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))   # 4
    print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))   # -1
    print(orangesRotting([[0,2]]))                       # 0
