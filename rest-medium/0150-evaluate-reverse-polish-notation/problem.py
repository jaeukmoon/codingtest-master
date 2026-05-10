"""
[0150] Evaluate Reverse Polish Notation (Medium)
https://leetcode.com/problems/evaluate-reverse-polish-notation/

## 문제

후위 표기법(Reverse Polish Notation)으로 된 산술식 토큰 배열 `tokens`가 주어진다.
연산자: '+', '-', '*', '/' (정수 나눗셈, 0으로 truncate).
계산 결과를 정수로 반환하라.

## 예시

Example 1:
    Input:  tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

Example 2:
    Input:  tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

Example 3:
    Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22

## 조건 (Constraints)

- 1 <= tokens.length <= 10^4
- tokens[i]는 연산자 또는 [-200, 200] 범위의 정수
"""
from typing import List


def evalRPN(tokens: List[str]) -> int:
    pass


if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))           # 9
    print(evalRPN(["4","13","5","/","+"]))          # 6
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
