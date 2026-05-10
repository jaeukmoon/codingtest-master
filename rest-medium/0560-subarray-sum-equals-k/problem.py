"""
[0560] Subarray Sum Equals K (Medium)
https://leetcode.com/problems/subarray-sum-equals-k/

## 문제

정수 배열 `nums`와 정수 `k`가 주어진다.
합이 `k`인 **연속 부분 배열의 개수**를 반환하라.

## 예시

Example 1:
    Input:  nums = [1,1,1], k = 2
    Output: 2
    Explanation: [1,1] 두 개 (인덱스 0~1, 1~2)

Example 2:
    Input:  nums = [1,2,3], k = 3
    Output: 2
    Explanation: [1,2], [3]

## 조건 (Constraints)

- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    pass


if __name__ == "__main__":
    print(subarraySum([1,1,1], 2))   # 2
    print(subarraySum([1,2,3], 3))   # 2
    print(subarraySum([1,-1,0], 0))  # 3
