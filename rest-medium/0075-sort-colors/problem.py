"""
[0075] Sort Colors (Medium)
https://leetcode.com/problems/sort-colors/

## 문제

배열 `nums`가 0(red), 1(white), 2(blue) 세 종류의 정수만 포함.
**in-place**로 정렬하라. 라이브러리 sort 사용 금지.

## 예시

Example 1:
    Input:  nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:
    Input:  nums = [2,0,1]
    Output: [0,1,2]

## 조건 (Constraints)

- n == nums.length
- 1 <= n <= 300
- nums[i]는 0, 1, 2 중 하나

## Follow-up

한 번의 순회로 O(1) 공간에서 가능한가? (Dutch National Flag)
"""
from typing import List


def sortColors(nums: List[int]) -> None:
    """in-place로 nums를 수정"""
    pass


if __name__ == "__main__":
    a = [2,0,2,1,1,0]
    sortColors(a)
    print(a)   # [0,0,1,1,2,2]

    b = [2,0,1]
    sortColors(b)
    print(b)   # [0,1,2]
