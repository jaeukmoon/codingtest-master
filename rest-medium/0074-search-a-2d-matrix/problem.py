"""
[0074] Search a 2D Matrix (Medium)
https://leetcode.com/problems/search-a-2d-matrix/

## 문제

m x n 매트릭스가 다음을 만족:
- 각 행은 왼쪽→오른쪽으로 정렬됨
- 각 행의 첫 원소는 이전 행의 마지막 원소보다 큼

target이 매트릭스에 존재하는지 반환. **O(log(m*n))**.

## 예시

Example 1:
    Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

## 조건 (Constraints)

- m == matrix.length, n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    pass


if __name__ == "__main__":
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(m, 3))    # True
    print(searchMatrix(m, 13))   # False
    print(searchMatrix(m, 60))   # True
    print(searchMatrix([[1]], 1))  # True
