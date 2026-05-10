"""
[0046] Permutations (Medium)
https://leetcode.com/problems/permutations/

## 문제

서로 다른 정수로 이루어진 배열 `nums`가 주어진다.
**모든 순열**을 반환하라. 순서는 무관.

## 예시

Example 1:
    Input:  nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input:  nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input:  nums = [1]
    Output: [[1]]

## 조건

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- 모든 원소 유일
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    print(permute([1,2,3]))   # 6개 순열 (3!)
    print(permute([0,1]))     # [[0,1],[1,0]]
    print(permute([1]))       # [[1]]
