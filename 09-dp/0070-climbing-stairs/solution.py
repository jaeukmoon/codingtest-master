"""
[0070] Climbing Stairs (Easy)
링크: https://leetcode.com/problems/climbing-stairs/

## 문제

n계단까지 1칸 또는 2칸씩 오를 때 방법 수.

## 예시

Example 1: n = 2 → 2 (1+1, 2)
Example 2: n = 3 → 3 (1+1+1, 1+2, 2+1)

## 조건

- 1 <= n <= 45

---

핵심 아이디어 (DP — Fibonacci):
    f(n) = f(n-1) + f(n-2)
    의미: n계단 도달 = (n-1에서 1칸) + (n-2에서 2칸) 합.
    base: f(1) = 1, f(2) = 2.

자료구조 / 패턴:
    - DP (1D, 점화식)

시간복잡도: O(n)
공간복잡도: O(1)  ← 이전 두 값만 추적

영어 멘트 (면접용):
    "This is a classic Fibonacci recurrence: f(n) = f(n-1) + f(n-2).
     Reaching step n means either taking one step from n-1 or two from n-2.
     I use two variables to track previous values for O(1) space."

엣지 케이스:
    - n = 1: 1 (1칸만)
    - n = 2: 2

## 손 추적 (Hand Trace)
# n = 5
#
#  i | prev2 | prev1 | curr (= prev2 + prev1)
# ---|-------|-------|-----------------------
#  3 |   1   |   2   |   3
#  4 |   2   |   3   |   5
#  5 |   3   |   5   |   8
#
# return 8

## 점화식 도출 과정 (DP 4단계)

# 1. 상태 정의: f(n) = n계단까지의 방법 수
# 2. 점화식: f(n) = f(n-1) + f(n-2)
#    (n계단 도달 = n-1에서 +1칸 OR n-2에서 +2칸)
# 3. base case: f(1)=1, f(2)=2
# 4. 순서: 작은 i부터 (bottom-up)
"""


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    prev2 = 1   # f(1)
    prev1 = 2   # f(2)

    for i in range(3, n + 1):
        curr = prev2 + prev1
        prev2 = prev1
        prev1 = curr

    return prev1


# DP 배열 버전 (대안 — 더 명시적)
# def climbStairs(n):
#     if n <= 2: return n
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n + 1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]


if __name__ == "__main__":
    print(climbStairs(2))    # 2
    print(climbStairs(3))    # 3
    print(climbStairs(5))    # 8
    print(climbStairs(10))   # 89
