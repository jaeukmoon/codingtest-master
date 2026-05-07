"""
[0349] Intersection of Two Arrays (Easy)
https://leetcode.com/problems/intersection-of-two-arrays/

## 문제

두 정수 배열 `nums1`과 `nums2`가 주어진다.
두 배열의 교집합을 반환하라.
결과에 중복이 없어야 하며, 순서는 무관하다.

## 예시

Example 1:
    Input:  nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] also accepted.

## 조건 (Constraints)

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    answer_set = set()
    set_1 = set(nums1)

    for num2 in nums2:
        if num2 in set_1:
            answer_set.add(num2)
    return list(answer_set)


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))          # Expected: [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))    # Expected: [9,4] (순서 무관)
    print(intersection([1, 2, 3], [4, 5, 6]))           # Expected: []
