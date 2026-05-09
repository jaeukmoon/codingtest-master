"""
[0167] Two Sum II - Input Array Is Sorted (Medium)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## 문제

1-indexed 정렬된 배열 `numbers`가 주어진다.
합이 `target`이 되는 두 수의 인덱스를 [index1, index2] 형태로 반환하라.
(1 <= index1 < index2 <= numbers.length)
O(1) 공간만 사용해야 한다.

## 예시

Example 1:
    Input:  numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: numbers[0] + numbers[1] == 9

Example 2:
    Input:  numbers = [2,3,4], target = 6
    Output: [1,3]

Example 3:
    Input:  numbers = [-1,0], target = -1
    Output: [1,2]

## 조건 (Constraints)

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers는 오름차순으로 정렬되어 있다.
- -1000 <= target <= 1000
- 정확히 하나의 유효한 답이 존재한다.
"""
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        cur_sum = numbers[left]+numbers[right]
        if cur_sum > target:
            right -= 1
        elif cur_sum == target:
            return [left+1, right+1]
        else:
            left += 1
    return []
    


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))   # Expected: [1, 2]
    print(twoSum([2, 3, 4], 6))        # Expected: [1, 3]
    print(twoSum([-1, 0], -1))         # Expected: [1, 2]
