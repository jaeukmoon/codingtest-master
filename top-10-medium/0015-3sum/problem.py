"""
[0015] 3Sum (Medium)
https://leetcode.com/problems/3sum/

## 문제

정수 배열 `nums`가 주어진다.
i, j, k가 모두 다르고 nums[i] + nums[j] + nums[k] == 0인 모든 triplet을 반환하라.
**중복된 triplet은 결과에 포함되지 말아야 한다.**

## 예시

Example 1:
    Input:  nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
        nums[0] + nums[1] + nums[2] = -1+0+1 = 0
        nums[1] + nums[2] + nums[4] = 0+1+(-1) = 0
        nums[0] + nums[3] + nums[4] = -1+2+(-1) = 0
        중복 [-1,0,1]은 한 번만.

Example 2:
    Input:  nums = [0,1,1]
    Output: []

Example 3:
    Input:  nums = [0,0,0]
    Output: [[0,0,0]]

## 조건 (Constraints)

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))   # Expected: [[-1,-1,2],[-1,0,1]]
    print(threeSum([0,1,1]))             # Expected: []
    print(threeSum([0,0,0]))             # Expected: [[0,0,0]]
