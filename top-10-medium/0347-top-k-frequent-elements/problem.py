"""
[0347] Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

## 문제

정수 배열 `nums`와 정수 `k`가 주어진다.
가장 많이 등장하는 상위 `k`개 원소를 반환하라. 순서는 무관.

## 예시

Example 1:
    Input:  nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

## 조건 (Constraints)

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k는 항상 유효 (1 <= k <= 고유 원소 개수)
- 답은 유일하다고 가정

## Follow-up

O(n log n)보다 빠른 풀이가 가능한가?
"""
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    pass


if __name__ == "__main__":
    print(sorted(topKFrequent([1,1,1,2,2,3], 2)))   # Expected: [1, 2]
    print(topKFrequent([1], 1))                       # Expected: [1]
