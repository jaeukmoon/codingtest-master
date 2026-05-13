"""
[1046] Last Stone Weight (Easy)
링크: https://leetcode.com/problems/last-stone-weight/

## 문제

매 턴 가장 무거운 돌 둘(x ≤ y)을 꺼냄. x==y면 둘 다 파괴, x<y면 y-x를 다시 넣음.
한 개 이하 남을 때까지 반복. 남은 무게(없으면 0) 반환.

## 예시

Example 1: [2,7,4,1,8,1] → 1
Example 2: [2,2] → 0

## 조건

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

---

핵심 아이디어 (Max-Heap):
    "가장 무거운 돌 두 개"를 반복해서 꺼내야 함 → Max-Heap이 정석.
    Python heapq는 min-heap만 제공 → **음수로 부호 뒤집어** max-heap 흉내.
    push: -stone, pop: -heappop() 로 부호 복원.
    매 턴: 가장 큰 두 개(y, x) pop → y > x면 y-x를 다시 push.
    힙 크기 ≤ 1 되면 종료.

자료구조 / 패턴:
    - Heap (max-heap을 min-heap + 음수 트릭으로)

시간복잡도: O(n log n) — 각 돌이 최대 log n번 heap 연산에 참여
공간복잡도: O(n) — heap

영어 멘트 (면접용):
    "I use a max-heap by negating values. Each turn I pop the two heaviest stones.
     If equal, both are destroyed. Otherwise, push back the difference. Stop when
     one or zero stones remain. O(n log n) time, O(n) space."

엣지 케이스:
    - 돌 1개: 그 무게 그대로
    - 둘 다 같음: 0
    - 단조 감소 / 단조 증가 입력

## 손 추적 (Hand Trace) — stones = [2,7,4,1,8,1]
# heapify (음수): heap = [-8,-7,-4,-1,-2,-1]
#   (실제 heap은 부분 정렬 구조지만 max로 보면 8,7,4,2,1,1)
#
#  turn | y=-pop | x=-pop | 결과       | heap (max로 본 값)
# ------|--------|--------|------------|-------------------
#   1   |   8    |   7    | 8-7=1 push | [4, 2, 1, 1, 1]
#   2   |   4    |   2    | 4-2=2 push | [2, 1, 1, 1]
#   3   |   2    |   1    | 2-1=1 push | [1, 1, 1]
#   4   |   1    |   1    | 둘 다 파괴  | [1]
#
# heap 크기 1 → 종료. return -heap[0] = 1
#
# 만약 heap이 비면 (둘 다 같은 무게로 끝): return 0
"""
from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    # 음수로 변환해서 max-heap 흉내
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        y = -heapq.heappop(heap)    # 가장 큰 돌 (부호 복원)
        x = -heapq.heappop(heap)    # 두 번째로 큰 돌
        if y > x:
            heapq.heappush(heap, -(y - x))    # 차이를 다시 음수로 push
        # y == x: 둘 다 파괴됨, push 안 함

    if len(heap) == 0:
        return 0
    return -heap[0]


if __name__ == "__main__":
    print(lastStoneWeight([2,7,4,1,8,1]))   # 1
    print(lastStoneWeight([1]))              # 1
    print(lastStoneWeight([2,2]))            # 0
    print(lastStoneWeight([10,4,2,10]))      # 2
