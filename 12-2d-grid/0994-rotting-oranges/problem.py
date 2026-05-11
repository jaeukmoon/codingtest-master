"""
[0994] Rotting Oranges (Medium)
https://leetcode.com/problems/rotting-oranges/

## 문제

m × n grid의 각 칸은:
- 0: 빈 칸
- 1: 신선한 오렌지
- 2: 썩은 오렌지

매 분마다 썩은 오렌지에 인접한(상하좌우) 신선한 오렌지가 함께 썩는다.
**모든 신선한 오렌지가 썩는 데 걸리는 최소 시간(분)**을 반환하라.
불가능하면 -1.

## 예시

Example 1:
    Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: (2,0) 위치 신선한 오렌지가 영영 안 썩음.

Example 3:
    Input:  grid = [[0,2]]
    Output: 0
    Explanation: 신선한 오렌지가 없으니 0.

## 조건

- m == grid.length, n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j]는 0, 1, 2 중 하나
"""
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))   # 4
    print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))   # -1
    print(orangesRotting([[0,2]]))                       # 0
