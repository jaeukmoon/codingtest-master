"""
[0034] Find First and Last Position of Element in Sorted Array (Medium)
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## 문제

오름차순 정렬된 정수 배열 `nums`와 정수 `target`이 주어진다.
`target`이 처음 나타나는 위치와 마지막 나타나는 위치를 반환하라.
없으면 [-1, -1].
**반드시 O(log n)으로 풀어야 한다.**

## 예시

Example 1:
    Input:  nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input:  nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:
    Input:  nums = [], target = 0
    Output: [-1,-1]

## 조건 (Constraints)

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums는 오름차순 정렬
- -10^9 <= target <= 10^9
"""
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    pass


if __name__ == "__main__":
    print(searchRange([5,7,7,8,8,10], 8))   # Expected: [3,4]
    print(searchRange([5,7,7,8,8,10], 6))   # Expected: [-1,-1]
    print(searchRange([], 0))                # Expected: [-1,-1]
    print(searchRange([1], 1))               # Expected: [0,0]
