"""
[0078] Subsets (Medium)
https://leetcode.com/problems/subsets/

## 문제

서로 다른 원소들로 구성된 정수 배열 `nums`가 주어진다.
**모든 부분집합 (power set)** 을 반환하라. 결과에 중복 부분집합 없어야 함.
순서는 무관.

## 예시

Example 1:
    Input:  nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input:  nums = [0]
    Output: [[],[0]]

## 조건

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- nums의 모든 원소는 유일
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    print(subsets([1,2,3]))   # 8개 부분집합
    print(subsets([0]))       # [[],[0]]
