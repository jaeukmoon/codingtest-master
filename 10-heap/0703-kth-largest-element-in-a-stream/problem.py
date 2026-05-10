"""
[0703] Kth Largest Element in a Stream (Easy)
https://leetcode.com/problems/kth-largest-element-in-a-stream/

## 문제

`KthLargest` 클래스를 구현:
- `KthLargest(int k, int[] nums)`: 정수 k와 초기 스트림으로 초기화
- `int add(int val)`: val을 스트림에 추가하고, 현재 스트림에서 k번째 큰 값을 반환

## 예시

Example 1:
    Input:
        ["KthLargest","add","add","add","add","add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output:
        [null, 4, 5, 5, 8, 8]
    Explanation:
        KthLargest kth = new KthLargest(3, [4,5,8,2]);
        kth.add(3);  → 4  (스트림: [4,5,8,2,3], 3번째 큰 값 = 4)
        kth.add(5);  → 5  (스트림: [4,5,8,2,3,5], 3번째 큰 값 = 5)
        kth.add(10); → 5
        kth.add(9);  → 8
        kth.add(4);  → 8

## 조건

- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- 호출 시 스트림에는 항상 적어도 k개 원소
- add는 최대 10^4번 호출
"""
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))    # 4
    print(kth.add(5))    # 5
    print(kth.add(10))   # 5
    print(kth.add(9))    # 8
    print(kth.add(4))    # 8
