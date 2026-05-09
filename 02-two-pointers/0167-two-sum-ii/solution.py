"""
[0167] Two Sum II - Input Array Is Sorted (Medium)
링크: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## 문제

1-indexed 정렬된 배열 `numbers`가 주어진다.
합이 `target`이 되는 두 수의 인덱스를 [index1, index2] 형태로 반환하라.
O(1) 공간만 사용해야 한다.

## 예시

Example 1:
    Input:  numbers = [2,7,11,15], target = 9
    Output: [1,2]

Example 2:
    Input:  numbers = [2,3,4], target = 6
    Output: [1,3]

Example 3:
    Input:  numbers = [-1,0], target = -1
    Output: [1,2]

## 조건

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers는 오름차순으로 정렬되어 있다.
- 정확히 하나의 유효한 답이 존재한다.

---

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

Two Sum I vs Two Sum II:
    | 조건          | Two Sum I (1번)   | Two Sum II (167번)     |
    |---------------|-------------------|------------------------|
    | 입력          | 정렬 안 됨        | 정렬됨                 |
    | 최적 풀이     | dict (Hash Map)   | Two Pointers           |
    | 공간복잡도    | O(n)              | O(1)                   |

    167번에서 dict 쓰면 동작은 하지만 정렬 조건을 전혀 활용 안 한 것.
    면접에서 "왜 Two Pointers 쓰냐?" → "정렬이 보장되므로 O(1) space로 풀 수 있다."
"""


## 손 추적 (Hand Trace)
# numbers = [2, 7, 11, 15], target = 9
#
#  left | right | numbers[L] | numbers[R] | sum | 판단
# ------|-------|------------|------------|-----|------------------
#   0   |   3   |     2      |     15     |  17 | 17>9 → right--
#   0   |   2   |     2      |     11     |  13 | 13>9 → right--
#   0   |   1   |     2      |      7     |   9 | 9==9 → [1,2] ✓


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
