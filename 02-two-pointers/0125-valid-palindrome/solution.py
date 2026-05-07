"""
[0125] Valid Palindrome (Easy)
링크: https://leetcode.com/problems/valid-palindrome/

문제:
    문자열이 팰린드롬인지 확인 (영숫자만 고려, 대소문자 무시).

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
