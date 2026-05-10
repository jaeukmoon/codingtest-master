"""
[0703] Kth Largest Element in a Stream (Easy)
링크: https://leetcode.com/problems/kth-largest-element-in-a-stream/

## 문제

KthLargest 클래스: add 호출 시 현재 스트림에서 k번째 큰 값을 반환.

## 예시

Example 1: k=3, [4,5,8,2] → add(3)→4, add(5)→5, add(10)→5, add(9)→8, add(4)→8

## 조건

- 1 <= k <= 10^4
- add는 최대 10^4번 호출

---

핵심 아이디어 (min-heap 크기 k 유지):
    크기 k짜리 min-heap을 유지하면 heap[0]이 항상 k번째 큰 값.
    add 시: push하고 heap이 k 초과면 pop. 그러면 항상 상위 k개만 남음.
    이때 heap[0]이 k번째 큰 값 (k개 중 가장 작은 값).

자료구조 / 패턴:
    - Min-Heap, 크기 k 유지

시간복잡도: __init__ O(n log k), add O(log k)
공간복잡도: O(k)

영어 멘트 (면접용):
    "I maintain a min-heap of size k. The root (smallest in heap) is always the
     kth largest in the stream. On each add, I push the value and pop if size > k.
     This gives O(log k) per add."

엣지 케이스:
    - 초기 nums 길이 < k: heap에 일단 다 넣음
    - val이 heap[0]보다 작으면 push 후 자기 자신이 pop됨 (k번째 큰 값 변화 없음)

## 손 추적 (Hand Trace)
# k = 3, nums = [4, 5, 8, 2]
#
# __init__: nums 차례로 push, 크기 > k면 pop
#   push 4 → heap=[4]
#   push 5 → heap=[4,5]
#   push 8 → heap=[4,5,8]
#   push 2 → heap=[2,4,5,8] → 크기 4 > 3 → pop → heap=[4,5,8]
#   heap[0] = 4
#
# add(3):  push 3 → heap=[3,5,8,4] → pop → heap=[4,5,8] → heap[0]=4
# add(5):  push 5 → heap=[4,5,8,5] → pop → heap=[5,5,8] → heap[0]=5
# add(10): push 10 → heap=[5,5,8,10] → pop → heap=[5,8,10] → heap[0]=5
# add(9):  push 9 → heap=[5,8,10,9] → pop → heap=[8,9,10] → heap[0]=8
# add(4):  push 4 → heap=[4,8,10,9] → pop → heap=[8,9,10] → heap[0]=8
"""
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))    # 4
    print(kth.add(5))    # 5
    print(kth.add(10))   # 5
    print(kth.add(9))    # 8
    print(kth.add(4))    # 8
