"""
[0704] Binary Search (Easy)
https://leetcode.com/problems/binary-search/

문제:
    오름차순 정렬된 배열에서 target의 인덱스 반환. 없으면 -1.

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
