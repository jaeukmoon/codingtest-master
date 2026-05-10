"""
[0300] Longest Increasing Subsequence (Medium)
https://leetcode.com/problems/longest-increasing-subsequence/

## 문제

정수 배열 `nums`가 주어진다.
가장 긴 **strictly increasing subsequence**의 길이를 반환하라.
subsequence: 원본 순서를 유지하면서 일부 원소를 (가능하면 0개) 삭제한 것.

## 예시

Example 1:
    Input:  nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: [2,3,7,101]

Example 2:
    Input:  nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input:  nums = [7,7,7,7,7,7,7]
    Output: 1

## 조건 (Constraints)

- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

## Follow-up

O(n log n)으로 풀 수 있는가?
"""
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))   # 4
    print(lengthOfLIS([0,1,0,3,2,3]))            # 4
    print(lengthOfLIS([7,7,7,7,7,7,7]))          # 1
