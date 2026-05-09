"""
[0125] Valid Palindrome (Easy)
링크: https://leetcode.com/problems/valid-palindrome/

## 문제

문자열 `s`에서 영숫자(알파벳 + 숫자)만 남기고 대소문자를 무시했을 때,
앞뒤가 같으면 `true`, 아니면 `false`를 반환하라.

## 예시

Example 1:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input:  s = "race a car"
    Output: false

Example 3:
    Input:  s = " "
    Output: true

## 조건

- 1 <= s.length <= 2 * 10^5
- s는 출력 가능한 ASCII 문자로만 구성된다.

---

핵심 아이디어:
    양 끝에서 포인터 두 개, 안쪽으로 좁혀가며 비교.
    영숫자 아닌 문자는 skip. 대소문자는 lower()로 통일.

자료구조 / 패턴:
    - Two Pointers (양 끝에서 안쪽으로)

시간복잡도: O(n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I'll use two pointers starting at both ends. I skip non-alphanumeric characters
     and compare the remaining characters case-insensitively. If they ever mismatch,
     return False. This runs in O(n) time and O(1) space."

엣지 케이스:
    - 빈 문자열: True
    - 공백/특수문자만: True (영숫자 없으면 팰린드롬)
    - 숫자 포함: "A1B...B1A" → True
"""


## 손 추적 (Hand Trace)
# s = "A man, a plan, a canal: Panama"
# (영숫자만 추출하면: "amanaplanacanalpanama")
#
#  left | right | s[L] | s[R] | 비교
# ------|-------|------|------|------
#    0  |  29   |  A   |  a   | a==a ✓ → L++, R--
#    1  |  28   | (공백)→skip→m | a  | m≠a → False? 아니, 공백skip 후...
#
# 실제 추적 (skip 포함):
#  L=0  R=29: skip공백→ 'A' vs 'a'  → lower: a==a ✓
#  L=1  R=27: skip','→  'm' vs 'm'  → m==m ✓
#  L=2  R=26: 'a' vs 'a'            → a==a ✓
#  ...중략...
#  L==R: 루프 종료 → return True


def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(isPalindrome("race a car"))                      # False
    print(isPalindrome(" "))                               # True
