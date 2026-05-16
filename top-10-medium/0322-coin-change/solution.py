"""
[0322] Coin Change — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **같은 동전 무한히 사용 가능?**
  → 네. (이게 unbounded knapsack 변종임을 알리는 신호)
- **amount=0이면?**
  → 0개. (방어적으로 base case 처리)
- **coins에 음수/0 있나요?**
  → 양수만 (1 이상).
- **답이 없으면?**
  → -1 반환.
- **그리디 가능한가?**
  → 일반적으로 **불가**. 예: coins=[1,3,4], amount=6 → 그리디(4+1+1=3개) vs 최적(3+3=2개).
  미국 화폐(1,5,10,25)처럼 "canonical" 시스템에서만 그리디 성립. 면접에서 명시적으로
  "그리디는 일반적으로 안 됨"이라고 짚고 가는 게 좋음.

## 2. 엣지 케이스

- amount=0 → 0
- 어떤 동전으로도 못 만듦 (coins=[2], amount=3) → -1
- coins에 1이 있으면 항상 해 존재
- coins[i]가 매우 큼 (2^31-1) — 비교 시 overflow 없음(파이썬). 다른 언어면 주의.
- amount가 동전보다 작음 → 해당 동전 skip

## 3. 알고리즘 선택

### 왜 DP인가
"최소 개수"를 찾는 문제이고, 부분 문제 `dp[x] = x를 만드는 최소 동전 수`로 분해 가능.
점화식: `dp[x] = min(dp[x - c] + 1)  for c in coins  if x - c >= 0`.
중복 부분 문제 + 최적 부분 구조 → DP 적격.

### Bottom-up DP ← 채택
- dp 배열 길이 amount+1, 초기값 amount+1 (도달 불가능 sentinel; INT_MAX 쓰면 +1에서 overflow).
- dp[0] = 0.
- 1..amount 순회하며 각 동전으로 갱신.
- 마지막에 dp[amount]가 sentinel이면 -1.

### Top-down (memoization)도 가능
재귀 + memo. 코드 직관적이지만 재귀 호출 오버헤드가 있음. 면접에서는 bottom-up 선호.

### BFS 시각으로도 풀 수 있음
각 amount를 노드, "동전 c 추가"가 엣지 → 최소 step. 최단경로니까 BFS = O(amount * len(coins)).
같은 복잡도지만 코드는 DP가 더 짧음.

## 4. 복잡도

- 시간: O(amount * len(coins))
- 공간: O(amount)
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # 예시: coins = [1, 3, 4], amount = 6
    INF = amount + 1    # 7 (절대 불가능한 값)
    dp = [INF] * (amount + 1)
    # dp = [7, 7, 7, 7, 7, 7, 7]
    dp[0] = 0
    # dp = [0, 7, 7, 7, 7, 7, 7]

    for x in range(1, amount + 1):
        for c in coins:
            if c <= x and dp[x - c] + 1 < dp[x]:
                dp[x] = dp[x - c] + 1

    # x=1: c=1 → dp[0]+1=1 < 7 → dp[1]=1
    #       c=3 → 3>1 skip, c=4 → 4>1 skip
    # dp = [0, 1, 7, 7, 7, 7, 7]
    #
    # x=2: c=1 → dp[1]+1=2  → dp[2]=2
    # dp = [0, 1, 2, 7, 7, 7, 7]
    #
    # x=3: c=1 → dp[2]+1=3, c=3 → dp[0]+1=1 → dp[3]=1  ← 동전 3 하나!
    # dp = [0, 1, 2, 1, 7, 7, 7]
    #
    # x=4: c=1 → dp[3]+1=2, c=3 → dp[1]+1=2, c=4 → dp[0]+1=1 → dp[4]=1
    # dp = [0, 1, 2, 1, 1, 7, 7]
    #
    # x=5: c=1 → dp[4]+1=2, c=3 → dp[2]+1=3, c=4 → dp[1]+1=2 → dp[5]=2
    # dp = [0, 1, 2, 1, 1, 2, 7]
    #
    # x=6: c=1 → dp[5]+1=3, c=3 → dp[3]+1=2, c=4 → dp[2]+1=3 → dp[6]=2
    # dp = [0, 1, 2, 1, 1, 2, 2]
    # → 답: 2 (동전 3+3)
    # (그리디였으면 4+1+1=3개 → 오답!)

    return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))    # 3 (5+5+1)
    print(coinChange([2], 3))            # -1
    print(coinChange([1], 0))            # 0
    print(coinChange([1, 2, 5], 100))    # 20
    print(coinChange([1, 3, 4], 6))      # 2 — 그리디 실패 케이스 (그리디는 3 답)
    print(coinChange([186, 419, 83, 408], 6249))   # 20
