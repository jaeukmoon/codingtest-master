"""
[0121] Best Time to Buy and Sell Stock (Easy)
링크: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## 문제

`prices[i]`는 i번째 날의 주가이다.
주식을 하루 사고 다른 날 팔 때 얻을 수 있는 최대 이익을 반환하라.
이익을 얻을 수 없으면 0을 반환하라.

## 예시

Example 1:
    Input:  prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Day 2(가격 1)에 사서 Day 5(가격 6)에 팔면 이익 = 5

Example 2:
    Input:  prices = [7,6,4,3,1]
    Output: 0

## 조건

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

---

핵심 아이디어:
    한 번 순회하면서 "지금까지 최저가"와 "현재에 팔 때 이익"을 동시에 추적.
    사는 날은 항상 파는 날보다 앞이어야 하므로, 최저가를 먼저 업데이트.

자료구조 / 패턴:
    - Sliding Window / 단일 패스 그리디

시간복잡도: O(n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I track the minimum price seen so far and the maximum profit achievable.
     For each price, I first check if it's a new minimum, then check if selling here
     beats the current max profit. One pass, O(n) time, O(1) space."

엣지 케이스:
    - 계속 하락: [7,6,5,4,3] → 0
    - 단조 상승: [1,2,3,4,5] → 4
    - 원소 1개: 0
"""


## 손 추적 (Hand Trace)
# prices = [7, 1, 5, 3, 6, 4]
#
#  price | min_price | profit(price-min) | max_profit
# -------|-----------|-------------------|----------
#    7   |     7     |        0          |     0
#    1   |     1     |        0          |     0     ← min 갱신
#    5   |     1     |        4          |     4
#    3   |     1     |        2          |     4
#    6   |     1     |        5          |     5
#    4   |     1     |        3          |     5
# → return 5


def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))   # 5 (1에 사서 6에 팔기)
    print(maxProfit([7, 6, 4, 3, 1]))      # 0 (이익 없음)
    print(maxProfit([1, 2]))               # 1
