"""
[0121] Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## 문제

`prices[i]`는 i번째 날의 주가이다.
주식을 하루 사고 다른 날 팔 때 얻을 수 있는 최대 이익을 반환하라.
이익을 얻을 수 없으면 0을 반환하라.

## 예시

Example 1:
    Input:  prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Day 2(가격 1)에 사서 Day 5(가격 6)에 팔면 이익 = 6 - 1 = 5

Example 2:
    Input:  prices = [7,6,4,3,1]
    Output: 0
    Explanation: 이익이 나는 경우가 없으므로 0

## 조건 (Constraints)

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))   # Expected: 5
    print(maxProfit([7, 6, 4, 3, 1]))      # Expected: 0
    print(maxProfit([1, 2]))               # Expected: 1
