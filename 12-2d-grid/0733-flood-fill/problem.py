"""
[0733] Flood Fill (Easy)
https://leetcode.com/problems/flood-fill/

## 문제

2D 이미지 `image`(각 칸은 픽셀 색), 시작 좌표 `sr, sc`, 새 색 `color`가 주어진다.
시작 픽셀과 **4방향으로 연결되고 같은 원래 색**을 가진 모든 픽셀을 새 색으로 칠한다.
바뀐 이미지를 반환하라.

## 예시

Example 1:
    Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: (1,1)에서 시작. 원래 색 1과 연결된 모든 1을 2로 칠함.
                 (2,2)의 1은 연결 안 됨 (대각선) → 그대로.

Example 2:
    Input:  image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: 새 색이 원래 색과 같음 → 변화 없음 (무한 루프 주의).

## 조건

- m == image.length, n == image[i].length
- 1 <= m, n <= 50
- 0 <= image[i][j], color < 2^16
- 0 <= sr < m, 0 <= sc < n
"""
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    pass


if __name__ == "__main__":
    print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))   # [[2,2,2],[2,2,0],[2,0,1]]
    print(floodFill([[0,0,0],[0,0,0]], 0, 0, 0))            # [[0,0,0],[0,0,0]]
    print(floodFill([[0,0,0],[0,1,0]], 1, 1, 2))            # [[0,0,0],[0,2,0]]
