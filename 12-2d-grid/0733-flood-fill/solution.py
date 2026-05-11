"""
[0733] Flood Fill (Easy)
링크: https://leetcode.com/problems/flood-fill/

## 문제

(sr, sc)에서 시작, 같은 원래 색으로 연결된 영역을 새 색으로 칠하기.

## 예시

Example 1: [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2 → [[2,2,2],[2,2,0],[2,0,1]]
Example 2: 새 색 == 원래 색 → 변화 없음 (무한 루프 주의)

## 조건

- 1 <= m, n <= 50

---

핵심 아이디어 (DFS):
    시작 픽셀의 원래 색을 기억. (sr, sc)에서 4방향 DFS.
    "원래 색과 같은 칸"만 새 색으로 바꾸고 재귀.
    **함정: 새 색 == 원래 색이면 아무것도 안 바뀌고 무한 루프** → 같으면 즉시 반환.

자료구조 / 패턴:
    - 2D Grid DFS (재귀)
    - visited 표시 = 새 색으로 칠하는 것 자체

시간복잡도: O(m * n) — 각 칸 최대 한 번
공간복잡도: O(m * n) 최악 (재귀 스택)

영어 멘트 (면접용):
    "I record the original color of the start pixel, then DFS in 4 directions,
     recoloring cells that match the original color. Important edge case: if the
     new color equals the original, I return immediately to avoid infinite recursion."

엣지 케이스:
    - 새 색 == 원래 색: 변화 없이 반환
    - 시작 픽셀이 고립 (주변 다른 색): 그 픽셀만 칠함
    - 그리드 가장자리에서 시작

## 손 추적 (Hand Trace)
# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]
# sr=1, sc=1, color=2.  원래 색 = image[1][1] = 1
#
# dfs(1,1): image[1][1]=1==원래색 → 2로 칠함. image[1][1]=2
#   상 dfs(0,1): 1==1 → 2로. image[0][1]=2
#     상 dfs(-1,1): 범위 밖
#     하 dfs(1,1): 이미 2 ≠ 1 → return
#     좌 dfs(0,0): 1==1 → 2로. image[0][0]=2
#       (상/좌 범위 밖, 하 dfs(1,0): 1==1 → 2로. image[1][0]=2 → 주변 다 2거나 0)
#     우 dfs(0,2): 1==1 → 2로. image[0][2]=2 → 하 dfs(1,2)=0 ≠ 1 → return
#   하 dfs(2,1): image[2][1]=0 ≠ 1 → return
#   좌 dfs(1,0): 이미 2 → return
#   우 dfs(1,2): 0 ≠ 1 → return
#
# 결과: [[2,2,2],
#        [2,2,0],
#        [2,0,1]]   ← (2,2)의 1은 대각선이라 연결 안 됨, 그대로
"""
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    original = image[sr][sc]
    if original == color:           # 무한 루프 방지
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original:
            return
        image[r][c] = color         # 칠하기 = visited 표시
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))   # [[2,2,2],[2,2,0],[2,0,1]]
    print(floodFill([[0,0,0],[0,0,0]], 0, 0, 0))            # [[0,0,0],[0,0,0]]
    print(floodFill([[0,0,0],[0,1,0]], 1, 1, 2))            # [[0,0,0],[0,2,0]]
