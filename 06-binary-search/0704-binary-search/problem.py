"""
[0704] Binary Search (Easy)
https://leetcode.com/problems/binary-search/

## 문제

오름차순 정렬된 정수 배열 `nums`와 정수 `target`이 주어진다.
`target`이 존재하면 인덱스를 반환, 없으면 -1을 반환하라.

## 예시

Example 1:
    Input:  nums = [-1,0,3,5,9,12], target = 9
    Output: 4

Example 2:
    Input:  nums = [-1,0,3,5,9,12], target = 2
    Output: -1

## 조건 (Constraints)

- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- nums의 모든 원소는 유일하다.
- nums는 오름차순으로 정렬되어 있다.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
  
    while left<=right:
        mid = (left+right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid+1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))    # Expected: 4
    print(search([-1, 0, 3, 5, 9, 12], 2))    # Expected: -1
    print(search([5], 5))                      # Expected: 0
