"""
[0053] Maximum Subarray (Medium)
https://leetcode.com/problems/maximum-subarray/

## 문제

정수 배열 `nums`가 주어진다.
합이 가장 큰 연속 부분 배열(subarray)을 찾고, 그 합을 반환하라.
(부분 배열은 최소 1개 원소를 포함해야 한다)

## 예시

Example 1:
    Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6

Example 2:
    Input:  nums = [1]
    Output: 1

Example 3:
    Input:  nums = [5,4,-1,7,8]
    Output: 23

## 조건 (Constraints)

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Follow-up

O(n log n) 풀이(분할 정복)도 가능하다. 생각해보자.
"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # Expected: 6
    print(maxSubArray([1]))                                  # Expected: 1
    print(maxSubArray([-2, -1]))                             # Expected: -1
