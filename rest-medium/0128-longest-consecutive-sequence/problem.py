"""
[0128] Longest Consecutive Sequence (Medium)
https://leetcode.com/problems/longest-consecutive-sequence/

## 문제

정수 배열 `nums`가 주어진다.
가장 긴 연속된 정수 수열의 길이를 반환하라.
**O(n) 시간복잡도**로 풀어야 한다.

## 예시

Example 1:
    Input:  nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: 가장 긴 연속 수열은 [1,2,3,4]

Example 2:
    Input:  nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

## 조건 (Constraints)

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(longestConsecutive([100,4,200,1,3,2]))           # 4
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))       # 9
    print(longestConsecutive([]))                            # 0
