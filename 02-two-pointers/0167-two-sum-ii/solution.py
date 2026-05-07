"""
[0167] Two Sum II - Input Array Is Sorted (Medium)
링크: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

문제:
    정렬된 배열에서 합이 target이 되는 두 수의 인덱스(1-indexed) 반환.
    O(1) 공간만 사용해야 함.

핵심 아이디어:
    배열이 정렬됨 → 양 끝 포인터. 합이 작으면 left++, 크면 right--.
    (정렬 안 된 Two Sum과 달리 dict 불필요 → O(1) space)

자료구조 / 패턴:
    - Two Pointers (정렬된 배열 + 양 끝)

시간복잡도: O(n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "Since the array is sorted, I can use two pointers at both ends.
     If the sum is too small, move left pointer right; if too large, move right pointer left.
     This is O(n) time and O(1) space — better than the hash map approach."

엣지 케이스:
    - 두 수가 인접하지 않을 때
    - 배열에 음수 포함
    - 정확히 한 쌍만 존재 (문제 보장)
"""


def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]   # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))    # [1, 2]
    print(twoSum([2, 3, 4], 6))         # [1, 3]
    print(twoSum([-1, 0], -1))          # [1, 2]
