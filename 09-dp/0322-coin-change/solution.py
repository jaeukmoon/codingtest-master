"""
[0322] Coin Change (Medium)
링크: https://leetcode.com/problems/coin-change/

## 문제

coins와 amount → amount를 만드는 최소 동전 수. 불가능하면 -1.

## 예시

Example 1: coins=[1,2,5], amount=11 → 3 (5+5+1)
Example 2: coins=[2], amount=3 → -1
Example 3: coins=[1], amount=0 → 0

## 조건

- 1 <= coins.length <= 12
- 0 <= amount <= 10^4

---

핵심 아이디어 (1D DP, bottom-up):
    상태: dp[i] = i원을 만드는 최소 동전 수
    점화식: dp[i] = min(dp[i - c] + 1  for c in coins if c <= i)
            의미: i원 = (i-c)원 만든 다음 동전 c 하나 더 쓰기
    base: dp[0] = 0 (0원은 동전 0개)
    초기값: dp[i] = ∞ (아직 못 만듦)
    답: dp[amount]가 ∞면 -1, 아니면 dp[amount]

자료구조 / 패턴:
    - 1D DP (Unbounded Knapsack 류)

시간복잡도: O(amount * len(coins))
공간복잡도: O(amount)

영어 멘트 (면접용):
    "Bottom-up DP. dp[i] is the min coins to make amount i. For each amount i, I try
     every coin c <= i: dp[i] = min(dp[i-c] + 1). Base case dp[0] = 0. If dp[amount]
     stays infinity, it's unreachable, return -1."

엣지 케이스:
    - amount = 0: 0 (동전 안 씀)
    - 만들 수 없는 금액: -1 (예: coins=[2], amount=3)
    - 동전 1개로 딱 떨어지는 경우

## DP 4단계
# 1. 상태: dp[i] = i원 만드는 최소 동전 수
# 2. 점화식: dp[i] = min over coins c≤i of (dp[i-c] + 1)
# 3. base: dp[0] = 0, 나머지 dp[i] = ∞
# 4. 순서: i = 1부터 amount까지 (bottom-up)

## 손 추적 (Hand Trace)
# coins = [1, 2, 5], amount = 11
# dp 초기: [0, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]   (index 0~11)
#
#  i  | 시도 (c <= i)              | dp[i] = min(dp[i-c]+1)
# ----|----------------------------|------------------------
#  1  | c=1: dp[0]+1=1             | 1
#  2  | c=1: dp[1]+1=2, c=2: dp[0]+1=1 | 1
#  3  | c=1: dp[2]+1=2, c=2: dp[1]+1=2 | 2
#  4  | c=1: dp[3]+1=3, c=2: dp[2]+1=2 | 2
#  5  | c=1: dp[4]+1=3, c=2: dp[3]+1=3, c=5: dp[0]+1=1 | 1
#  6  | c=1: dp[5]+1=2, c=2: dp[4]+1=3, c=5: dp[1]+1=2 | 2
#  7  | c=1: dp[6]+1=3, c=2: dp[5]+1=2, c=5: dp[2]+1=2 | 2
#  8  | c=1: dp[7]+1=3, c=2: dp[6]+1=3, c=5: dp[3]+1=3 | 3
#  9  | c=1: dp[8]+1=4, c=2: dp[7]+1=3, c=5: dp[4]+1=3 | 3
# 10  | c=1: dp[9]+1=4, c=2: dp[8]+1=4, c=5: dp[5]+1=2 | 2   (5+5)
# 11  | c=1: dp[10]+1=3, c=2: dp[9]+1=4, c=5: dp[6]+1=3 | 3  (5+5+1 또는 5+2+2+2 → 3 vs 4 → 3)
#
# dp[11] = 3 ≠ ∞ → return 3
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                candidate = dp[i - c] + 1
                if candidate < dp[i]:
                    dp[i] = candidate

    if dp[amount] == INF:
        return -1
    return dp[amount]


if __name__ == "__main__":
    print(coinChange([1,2,5], 11))   # 3
    print(coinChange([2], 3))         # -1
    print(coinChange([1], 0))         # 0
    print(coinChange([1,2,5], 100))   # 20
