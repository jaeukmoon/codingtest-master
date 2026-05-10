"""
[0022] Generate Parentheses (Medium)
https://leetcode.com/problems/generate-parentheses/

## 문제

n쌍의 괄호로 만들 수 있는 **모든 유효한 조합**을 생성하라.

## 예시

Example 1:
    Input:  n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input:  n = 1
    Output: ["()"]

## 조건 (Constraints)

- 1 <= n <= 8
"""
from typing import List


def generateParenthesis(n: int) -> List[str]:
    pass


if __name__ == "__main__":
    print(sorted(generateParenthesis(3)))
    # Expected: ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(generateParenthesis(1))   # Expected: ["()"]
