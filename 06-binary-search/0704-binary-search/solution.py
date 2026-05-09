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

## 조건

- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- nums의 모든 원소는 유일하며 오름차순 정렬되어 있다.

---

핵심 아이디어:
    left, right 포인터. mid = (left + right) // 2.
    nums[mid] < target → left = mid + 1
    nums[mid] > target → right = mid - 1
    종료 조건: left > right

자료구조 / 패턴:
    - Binary Search

시간복잡도: O(log n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I use two pointers, left and right, and repeatedly check the midpoint.
     If nums[mid] equals target, return mid. If less, search right half;
     if greater, search left half. This runs in O(log n)."

엣지 케이스:
    - 원소 1개: target과 같으면 0, 다르면 -1
    - target이 배열 범위 밖: -1
    - 짝수/홀수 길이 모두 동작해야 함
"""
from typing import List


## 손 추적 (Hand Trace)
# nums = [-1, 0, 3, 5, 9, 12], target = 9
# idx:    0   1  2  3  4   5
#
#  left | right | mid | nums[mid] | 판단
# ------|-------|-----|-----------|------------------
#   0   |   5   |  2  |     3     | 3 < 9 → left=3
#   3   |   5   |  4  |     9     | 9 == 9 → return 4 ✓
#
# 실패 케이스 target=2:
#  left | right | mid | nums[mid] | 판단
# ------|-------|-----|-----------|------------------
#   0   |   5   |  2  |     3     | 3 > 2 → right=1
#   0   |   1   |  0  |    -1     | -1 < 2 → left=1
#   1   |   1   |  1  |     0     | 0 < 2 → left=2
#   2   |   1   |  -  |     -     | left>right → return -1


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))    # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))    # -1
    print(search([5], 5))                      # 0
