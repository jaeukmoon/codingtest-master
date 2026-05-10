"""
[0011] Container With Most Water (Medium)
https://leetcode.com/problems/container-with-most-water/

## 문제

길이 n의 정수 배열 `height`가 주어진다.
n개의 수직선이 있고, i번째 선의 양 끝점은 (i, 0)과 (i, height[i]).
두 선과 x축이 만드는 컨테이너에 담을 수 있는 **물의 최대 양**을 반환하라.

## 예시

Example 1:
    Input:  height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: 인덱스 1과 8 (높이 8과 7) → min(8,7) * (8-1) = 49

Example 2:
    Input:  height = [1,1]
    Output: 1

## 조건 (Constraints)

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""
from typing import List


def maxArea(height: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))   # Expected: 49
    print(maxArea([1,1]))                   # Expected: 1
    print(maxArea([4,3,2,1,4]))             # Expected: 16
