"""
[0078] Subsets (Medium)
링크: https://leetcode.com/problems/subsets/

## 문제

[1,2,3]의 모든 부분집합 (power set) 반환.

## 예시

Example 1: [1,2,3] → [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]] (총 2^3 = 8개)

## 조건

- 1 <= nums.length <= 10
- 모든 원소 유일

---

핵심 아이디어 (Backtracking):
    각 원소에 대해 "포함 / 미포함" 두 갈래로 재귀.
    매 호출마다 현재까지 만든 path를 부분집합으로 결과에 추가.
    포함하기로 했으면 path에 push → 재귀 → pop (상태 복원).

자료구조 / 패턴:
    - Backtracking (DFS + 상태 복원)

시간복잡도: O(n * 2^n) — 부분집합 2^n개, 각각 길이 평균 n/2 복사
공간복잡도: O(n) 재귀 스택 + 결과 저장 별도

영어 멘트 (면접용):
    "I use backtracking. At each index, I have two choices: include the element or not.
     I maintain a current path, append a copy to results at each call, and recurse.
     The append/pop pattern restores state after exploring each branch."

엣지 케이스:
    - 빈 배열: [[]]
    - 1개 원소: [[], [원소]]

## 손 추적 (Hand Trace) — nums = [1, 2, 3]
# 호출 트리 (들여쓰기 = 깊이):
#
# bt(start=0, path=[])              → result = [[]]
#   include 1: path=[1]
#     bt(start=1, path=[1])         → result = [[], [1]]
#       include 2: path=[1,2]
#         bt(start=2, path=[1,2])   → result = [..., [1,2]]
#           include 3: path=[1,2,3]
#             bt(start=3, path=[1,2,3]) → result = [..., [1,2,3]]
#           pop 3
#         (start=3 > len-1 → return)
#       pop 2
#       include 3: path=[1,3]
#         bt(start=3, path=[1,3])   → result = [..., [1,3]]
#       pop 3
#     pop 1
#   include 2: path=[2]
#     bt(start=2, path=[2])         → result = [..., [2]]
#       include 3: path=[2,3]
#         bt(start=3, path=[2,3])   → result = [..., [2,3]]
#       pop 3
#     pop 2
#   include 3: path=[3]
#     bt(start=3, path=[3])         → result = [..., [3]]
#     pop 3
#
# 최종: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    path = []

    def backtrack(start: int):
        result.append(path[:])    # 현재 path를 부분집합으로 추가 (복사 중요)
        for i in range(start, len(nums)):
            path.append(nums[i])     # 선택
            backtrack(i + 1)         # 재귀
            path.pop()                # 선택 취소 (상태 복원)

    backtrack(0)
    return result


# 비트 마스크 버전 (대안 — 면접 후 언급용)
# def subsets(nums):
#     n = len(nums)
#     result = []
#     for mask in range(1 << n):
#         subset = [nums[i] for i in range(n) if mask & (1 << i)]
#         result.append(subset)
#     return result


if __name__ == "__main__":
    print(subsets([1,2,3]))
    # [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    print(subsets([0]))
    # [[], [0]]
