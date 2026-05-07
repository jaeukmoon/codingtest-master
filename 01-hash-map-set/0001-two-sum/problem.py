"""
[0001] Two Sum (Easy)
https://leetcode.com/problems/two-sum/

## 문제

정수 배열 `nums`와 정수 `target`이 주어진다.
합이 `target`이 되는 두 수의 인덱스를 반환하라.
같은 원소를 두 번 사용할 수 없으며, 정확히 하나의 답이 존재한다.

## 예시

Example 1:
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9

Example 2:
    Input:  nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input:  nums = [3,3], target = 6
    Output: [0,1]

## 조건 (Constraints)

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- 정확히 하나의 유효한 답이 존재한다.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    pass


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print(twoSum([3, 2, 4], 6))         # Expected: [1, 2]
    print(twoSum([3, 3], 6))            # Expected: [0, 1]
