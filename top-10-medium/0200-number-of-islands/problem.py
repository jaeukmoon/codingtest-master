"""
[0200] Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands/

## 문제

m × n 크기의 2D grid가 주어진다. 각 칸은 '1'(육지) 또는 '0'(물).
인접한(상하좌우) 육지끼리 연결된 영역을 하나의 "island"로 본다.
grid의 가장자리는 모두 물로 둘러싸여 있다고 가정.
island의 개수를 반환하라.

## 예시

Example 1:
    Input:
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
    Output: 1

Example 2:
    Input:
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    Output: 3

## 조건 (Constraints)

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j]는 '0' 또는 '1'
"""
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    pass


if __name__ == "__main__":
    g1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(g1))   # Expected: 1

    g2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(g2))   # Expected: 3
