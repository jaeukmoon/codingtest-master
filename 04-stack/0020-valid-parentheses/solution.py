"""
[0020] Valid Parentheses (Easy)
링크: https://leetcode.com/problems/valid-parentheses/

문제:
    괄호 문자열 s가 유효한지 확인.
    ('(', ')', '{', '}', '[', ']'만 포함)

핵심 아이디어:
    여는 괄호 → push. 닫는 괄호 → pop해서 매칭 확인.
    모든 글자 처리 후 stack이 비어야 유효.

자료구조 / 패턴:
    - Stack (LIFO)

시간복잡도: O(n)
공간복잡도: O(n)

영어 멘트 (면접용):
    "I use a stack. Opening brackets are pushed; for each closing bracket, I pop from
     the stack and check if it matches the expected opener using a hash map.
     If the stack is empty at any mismatch, or non-empty at the end, return False."

엣지 케이스:
    - 닫는 괄호로 시작: ']' → stack 비어서 False
    - 열기만 하고 안 닫힘: '(' → 마지막에 stack 비지 않아서 False
    - 빈 문자열: True
    - 다른 종류 섞임: '([)]' → False, '([{}])' → True
"""


def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or stack.pop() != pairs[c]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(isValid("()[]{}"))    # True
    print(isValid("(]"))        # False
    print(isValid("([{}])"))    # True
    print(isValid("([)]"))      # False
    print(isValid("{[]"))       # False
