"""
[0198] House Robber (Medium)
링크: https://leetcode.com/problems/house-robber/

## 문제

집들의 돈 배열 nums. 인접한 두 집 동시에 못 텀. 최대 금액.

## 예시

Example 1: [1,2,3,1] → 4 (집 0+2)
Example 2: [2,7,9,3,1] → 12 (집 0+2+4)

## 조건

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

---

핵심 아이디어 (1D DP):
    상태: dp[i] = i번째 집까지 고려했을 때 털 수 있는 최대 금액
    점화식: dp[i] = max(dp[i-1],          # i번째 집 안 털기
                       dp[i-2] + nums[i])  # i번째 집 털기 (i-1은 못 텀)
    base: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])

자료구조 / 패턴:
    - 1D DP

시간복잡도: O(n)
공간복잡도: O(1)  ← 이전 두 값만 필요

영어 멘트 (면접용):
    "1D DP. dp[i] is the max money robbing houses up to index i.
     At house i, I either skip it (dp[i-1]) or rob it (dp[i-2] + nums[i]) — since
     robbing i means I can't rob i-1. I only need the last two values, so O(1) space."

엣지 케이스:
    - 집 1개: nums[0]
    - 집 2개: max(nums[0], nums[1])
    - 0이 섞인 경우

## DP 4단계
# 1. 상태: dp[i] = i까지 고려한 최대 금액
# 2. 점화식: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#    - 안 털기: 이전까지 최대(dp[i-1]) 그대로
#    - 털기: i-2까지 최대(dp[i-2]) + 현재 집(nums[i])  (i-1은 인접이라 제외)
# 3. base: dp[0]=nums[0], dp[1]=max(nums[0],nums[1])
# 4. 순서: 작은 i부터 (bottom-up)

## 손 추적 (Hand Trace)
# nums = [2, 7, 9, 3, 1]
#
#  i | nums[i] | dp[i-1] | dp[i-2]+nums[i] | dp[i] = max(둘)
# ---|---------|---------|-----------------|-----------------
#  0 |    2    |    -    |        -        |  2   (base)
#  1 |    7    |    -    |        -        |  7   (max(2,7))
#  2 |    9    |   7     |    2 + 9 = 11   |  11
#  3 |    3    |  11     |    7 + 3 = 10   |  11
#  4 |    1    |  11     |   11 + 1 = 12   |  12
#
# return 12
#
# 공간 최적화 추적 (prev2, prev1만):
#  num | prev2 | prev1 | new_prev1 = max(prev1, prev2 + num)
# -----|-------|-------|------------------------------------
#   2  |   0   |   0   | max(0, 0+2) = 2     → prev2=0, prev1=2
#   7  |   0   |   2   | max(2, 0+7) = 7     → prev2=2, prev1=7
#   9  |   2   |   7   | max(7, 2+9) = 11    → prev2=7, prev1=11
#   3  |   7   |  11   | max(11, 7+3) = 11   → prev2=11, prev1=11
#   1  |  11   |  11   | max(11, 11+1) = 12  → prev2=11, prev1=12
# return prev1 = 12
"""
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        skip_i = dp[i - 1]
        rob_i = dp[i - 2] + nums[i]
        dp[i] = max(skip_i, rob_i)

    return dp[-1]


# 공간 최적화 버전 (대안 — 면접 후 언급용)
# def rob(nums):
#     prev2 = 0
#     prev1 = 0
#     for num in nums:
#         new_prev1 = max(prev1, prev2 + num)
#         prev2 = prev1
#         prev1 = new_prev1
#     return prev1


if __name__ == "__main__":
    print(rob([1,2,3,1]))     # 4
    print(rob([2,7,9,3,1]))   # 12
    print(rob([2,1,1,2]))     # 4
    print(rob([5]))           # 5
