"""
[0033] Search in Rotated Sorted Array (Medium)
https://leetcode.com/problems/search-in-rotated-sorted-array/

## 문제

오름차순 정렬된 배열이 어떤 인덱스에서 회전(rotate)되어 주어진다.
예: [0,1,2,4,5,6,7] → [4,5,6,7,0,1,2]
정수 `target`이 존재하면 인덱스 반환, 없으면 -1.
**반드시 O(log n) 시간복잡도로 풀어야 한다.**

## 예시

Example 1:
    Input:  nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input:  nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input:  nums = [1], target = 0
    Output: -1

## 조건 (Constraints)

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums의 모든 원소는 유일
- nums는 회전되었거나 회전되지 않은 정렬 배열
- -10^4 <= target <= 10^4
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    pass


if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))   # Expected: 4
    print(search([4,5,6,7,0,1,2], 3))   # Expected: -1
    print(search([1], 0))                # Expected: -1
    print(search([1], 1))                # Expected: 0
    print(search([3,1], 1))              # Expected: 1
