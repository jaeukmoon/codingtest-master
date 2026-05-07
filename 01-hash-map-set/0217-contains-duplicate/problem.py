"""
[0217] Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

## 문제

정수 배열 `nums`가 주어진다.
배열에 두 번 이상 등장하는 원소가 있으면 `true`, 모두 다르면 `false`를 반환하라.

## 예시

Example 1:
    Input:  nums = [1,2,3,1]
    Output: true

Example 2:
    Input:  nums = [1,2,3,4]
    Output: false

Example 3:
    Input:  nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

## 조건 (Constraints)

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""
from typing import List
from collections import defaultdict

def containsDuplicate(nums: List[int]) -> bool:
    num_map = defaultdict(int)
    for num in nums:
        num_map[num] += 1
        if num_map[num]>=2:
            return True
    return False



if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))          # Expected: True
    print(containsDuplicate([1, 2, 3, 4]))          # Expected: False
    print(containsDuplicate([1, 1, 1, 3, 3, 4]))   # Expected: True
