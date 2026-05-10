"""
[0046] Permutations (Medium)
링크: https://leetcode.com/problems/permutations/

## 문제

[1,2,3]의 모든 순열 반환.

## 예시

Example 1: [1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] (3! = 6개)

## 조건

- 1 <= nums.length <= 6
- 모든 원소 유일

---

핵심 아이디어 (Backtracking + 사용 여부 추적):
    매 자리에 "아직 안 쓴 모든 원소"를 후보로 시도.
    used 집합으로 어떤 원소를 이미 path에 넣었는지 추적.
    path가 길이 n에 도달하면 결과에 추가.
    Subsets와 차이: 순서가 의미 있음 (start 인덱스 안 씀 → 모든 원소를 매번 후보로).

자료구조 / 패턴:
    - Backtracking + Set (used)

시간복잡도: O(n * n!) — 순열 n!개, 각각 길이 n
공간복잡도: O(n) 재귀 + used set

영어 멘트 (면접용):
    "Backtracking with a `used` set. At each level, I try every unused element,
     mark it used, recurse, then unmark. When the path length equals n, I record
     it as a permutation. Because order matters, I revisit all elements at every
     level — unlike subsets which uses a start index."

엣지 케이스:
    - 한 원소: [[원소]]
    - 빈 배열: [[]]

## 손 추적 (Hand Trace) — nums = [1, 2, 3]
# 호출 트리:
#
# bt(path=[], used={})
# ├─ try 1: used={1}, path=[1]
# │   ├─ try 2: used={1,2}, path=[1,2]
# │   │   └─ try 3: used={1,2,3}, path=[1,2,3] → result.append [1,2,3]
# │   └─ try 3: used={1,3}, path=[1,3]
# │       └─ try 2: path=[1,3,2] → [1,3,2]
# ├─ try 2: path=[2]
# │   ├─ try 1: path=[2,1]
# │   │   └─ try 3: path=[2,1,3] → [2,1,3]
# │   └─ try 3: path=[2,3]
# │       └─ try 1: path=[2,3,1] → [2,3,1]
# └─ try 3: path=[3]
#     ├─ try 1: path=[3,1]
#     │   └─ try 2: path=[3,1,2] → [3,1,2]
#     └─ try 2: path=[3,2]
#         └─ try 1: path=[3,2,1] → [3,2,1]
#
# 최종 6개

## Subsets vs Permutations 차이

#               | Subsets (78)        | Permutations (46)
# --------------|---------------------|---------------------
# 순서 의미     | 없음 ({1,2}={2,1})   | 있음 ([1,2]≠[2,1])
# 인덱스        | start 인덱스 사용    | used 집합 사용 (모두 후보)
# 결과 개수     | 2^n                  | n!
# 결과 추가 시점| 모든 호출마다        | path 길이 == n 일 때만
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    path = []
    used = set()

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])    # 복사
            return

        for num in nums:
            if num in used:
                continue
            used.add(num)
            path.append(num)
            backtrack()
            path.pop()                 # 상태 복원
            used.remove(num)

    backtrack()
    return result


if __name__ == "__main__":
    print(permute([1,2,3]))
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute([0,1]))     # [[0,1],[1,0]]
    print(permute([1]))       # [[1]]
