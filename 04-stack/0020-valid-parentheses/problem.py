"""
[0020] Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

## 문제

'(', ')', '{', '}', '[', ']'로 이루어진 문자열 `s`가 주어진다.
문자열이 유효하면 `true`, 아니면 `false`를 반환하라.

유효한 조건:
  - 여는 괄호는 같은 종류의 괄호로 닫혀야 한다.
  - 괄호는 올바른 순서로 닫혀야 한다.
  - 모든 닫는 괄호에 대응하는 여는 괄호가 존재해야 한다.

## 예시

Example 1:
    Input:  s = "()"
    Output: true

Example 2:
    Input:  s = "()[]{}"
    Output: true

Example 3:
    Input:  s = "(]"
    Output: false

Example 4:
    Input:  s = "([)]"
    Output: false

Example 5:
    Input:  s = "{[]}"
    Output: true

## 조건 (Constraints)

- 1 <= s.length <= 10^4
- s는 '(', ')', '{', '}', '[', ']'로만 구성된다.
"""


def isValid(s: str) -> bool:
    is_valid = {')':'(', '}': '{', ']': '['}
    s_stack = []
    for c in s:
        if c in '({[':
            s_stack.append(c)
        else:
            if len(s_stack)==0 or s_stack.pop() != is_valid[c]:
                return False
    if len(s_stack)==0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isValid("()[]{}"))    # Expected: True
    print(isValid("(]"))        # Expected: False
    print(isValid("([{}])"))    # Expected: True
    print(isValid("([)]"))      # Expected: False
    print(isValid("{[]"))       # Expected: False
