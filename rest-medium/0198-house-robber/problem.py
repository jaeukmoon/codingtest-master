"""
[0198] House Robber (Medium)
https://leetcode.com/problems/house-robber/

## 문제

각 집의 돈 액수가 담긴 배열 `nums`. 인접한 두 집을 동시에 털면 경보 작동.
경보 없이 털 수 있는 **최대 금액**을 반환하라.

## 예시

Example 1:
    Input:  nums = [1,2,3,1]
    Output: 4
    Explanation: 1 + 3 = 4 (집 0과 집 2)

Example 2:
    Input:  nums = [2,7,9,3,1]
    Output: 12
    Explanation: 2 + 9 + 1 = 12

## 조건 (Constraints)

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""
from typing import List


def rob(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(rob([1,2,3,1]))     # 4
    print(rob([2,7,9,3,1]))   # 12
    print(rob([2,1,1,2]))     # 4
