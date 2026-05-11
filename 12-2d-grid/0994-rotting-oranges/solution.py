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

핵심 아이디어 (Multi-source BFS, 거리를 노드에 동봉):
    "최단 시간" + "동시 확산" → BFS. 시작점이 여러 개 (모든 썩은 오렌지).
    1) 처음에 모든 썩은 오렌지를 (r, c, 0) 형태로 큐에 넣음. 신선 오렌지 개수 카운트.
    2) BFS: 각 노드가 자기 시각(minutes)을 들고 다님. 인접 신선 오렌지를 썩히며
       (nr, nc, minutes+1)을 큐에 추가, fresh -= 1.
    3) 마지막 신선 오렌지가 썩는 순간 그 시각을 즉시 반환 (조기 종료).
    4) BFS 끝났는데 fresh가 남았으면 -1.

    레벨 트릭(`len(q)`) 대신 거리를 튜플에 담는 방식. 최단 거리류 BFS에서 흔하고,
    "마지막 fresh 썩는 순간 return"이 깔끔.

자료구조 / 패턴:
    - Multi-source BFS (deque, 거리를 노드에 동봉)

시간복잡도: O(m * n) — 각 칸 한 번
공간복잡도: O(m * n) — 큐

영어 멘트 (면접용):
    "Multi-source BFS. I seed the queue with all rotten oranges, each carrying a
     timestamp of 0, and count the fresh ones. Each node propagates its time + 1 to
     fresh neighbors. The moment the last fresh orange rots, I return that timestamp.
     If BFS finishes with fresh oranges left, return -1."

엣지 케이스:
    - 신선 오렌지 0개: 0분 (BFS 안 돌아도 됨)
    - 고립된 신선 오렌지 (썩은 거랑 연결 안 됨): -1
    - 처음부터 다 썩어있음: 0

## 손 추적 (Hand Trace)
# grid = [[2,1,1],
#         [1,1,0],
#         [0,1,1]]
#
# 초기: 큐 = [(0,0,0)]  (썩은 오렌지 + 시각 0), fresh = 6
#
#  pop          | 인접 신선 → 썩힘 (큐 추가)         | fresh | 큐 상태
# --------------|------------------------------------|-------|--------------------------
#  (0,0,0)      | (0,1)→(0,1,1), (1,0)→(1,0,1)       |  4    | [(0,1,1),(1,0,1)]
#  (0,1,1)      | (0,2)→(0,2,2), (1,1)→(1,1,2)       |  2    | [(1,0,1),(0,2,2),(1,1,2)]
#  (1,0,1)      | (1,1) 이미 썩음, 나머지 0/범위밖    |  2    | [(0,2,2),(1,1,2)]
#  (0,2,2)      | (1,2)=0 빈칸                        |  2    | [(1,1,2)]
#  (1,1,2)      | (2,1)→(2,1,3)                       |  1    | [(2,1,3)]
#  (2,1,3)      | (2,2)→(2,2,4)  fresh==0 → return 4 |  0    | -
#
# 마지막 fresh가 시각 4에 썩음 → return 4
"""
from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # 1) 초기 썩은 오렌지 큐에 (시각 0) + 신선 오렌지 카운트
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 2) BFS — 각 노드가 자기 시각을 들고 다님
    while queue:
        r, c, minutes = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2          # 썩힘
                fresh -= 1
                if fresh == 0:            # 마지막 fresh 썩는 순간 즉시 반환
                    return minutes + 1
                queue.append((nr, nc, minutes + 1))

    # 3) 큐 다 비웠는데 fresh가 남음 → 도달 불가
    return -1


if __name__ == "__main__":
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))   # 4
    print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))   # -1
    print(orangesRotting([[0,2]]))                       # 0
