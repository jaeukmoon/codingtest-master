"""
[0125] Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/

## 문제

문자열 `s`에서 영숫자(알파벳 + 숫자)만 남기고 대소문자를 무시했을 때,
앞뒤가 같은 팰린드롬이면 `true`, 아니면 `false`를 반환하라.

## 예시

Example 1:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input:  s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input:  s = " "
    Output: true
    Explanation: s is an empty string after removing non-alphanumeric chars.
                 An empty string reads the same forward and backward.

## 조건 (Constraints)

- 1 <= s.length <= 2 * 10^5
- s는 출력 가능한 ASCII 문자로만 구성된다.
"""


def isPalindrome(s: str) -> bool:
    def is_alnum(c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))
    if len(s) == 0:
        return True
    for i in range(len(s)):
        ord(s[i])
    left, right = 0, len(s)-1
    while left<right:
        while left<right and not is_alnum(s[left]):
            left += 1
        while left<right and not is_alnum(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(isPalindrome("race a car"))                      # Expected: False
    print(isPalindrome(" "))                               # Expected: True
