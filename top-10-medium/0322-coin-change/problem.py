"""
[0322] Coin Change (Medium)
https://leetcode.com/problems/coin-change/

## 문제

서로 다른 액면의 동전 배열 `coins`와 목표 금액 `amount`가 주어진다.
amount를 만들기 위한 **최소 동전 개수**를 반환하라.
조합 불가능하면 -1.
같은 동전을 여러 번 사용 가능.

## 예시

Example 1:
    Input:  coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input:  coins = [2], amount = 3
    Output: -1

Example 3:
    Input:  coins = [1], amount = 0
    Output: 0

## 조건 (Constraints)

- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    pass


if __name__ == "__main__":
    print(coinChange([1,2,5], 11))   # Expected: 3
    print(coinChange([2], 3))         # Expected: -1
    print(coinChange([1], 0))         # Expected: 0
    print(coinChange([1,2,5], 100))   # Expected: 20
