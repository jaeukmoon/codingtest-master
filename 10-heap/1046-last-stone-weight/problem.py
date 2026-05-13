"""
[1046] Last Stone Weight (Easy)
https://leetcode.com/problems/last-stone-weight/

## 문제

돌 무게 배열 `stones`가 주어진다. 매 턴마다:
1. 가장 무거운 돌 두 개 x, y를 꺼낸다 (x <= y).
2. x == y이면 둘 다 파괴.
3. x < y이면 x 파괴, y는 `y - x`로 변함.
돌이 한 개 이하 남을 때까지 반복.
남은 돌의 무게 반환. 모두 파괴됐으면 0.

## 예시

Example 1:
    Input:  stones = [2,7,4,1,8,1]
    Output: 1
    Explanation:
        가장 큰 둘 8,7 → 1 남음. stones = [2,4,1,1,1]
        가장 큰 둘 4,2 → 2 남음. stones = [2,1,1,1]
        가장 큰 둘 2,1 → 1 남음. stones = [1,1,1]
        가장 큰 둘 1,1 → 둘 다 파괴. stones = [1]
        → 1

Example 2:
    Input:  stones = [1]
    Output: 1

## 조건

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000
"""
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(lastStoneWeight([2,7,4,1,8,1]))   # 1
    print(lastStoneWeight([1]))              # 1
    print(lastStoneWeight([2,2]))            # 0
    print(lastStoneWeight([10,4,2,10]))      # 2
