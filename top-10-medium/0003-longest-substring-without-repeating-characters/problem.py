"""
[0003] Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 문제

문자열 `s`가 주어진다.
중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환하라.

## 예시

Example 1:
    Input:  s = "abcabcbb"
    Output: 3
    Explanation: "abc"

Example 2:
    Input:  s = "bbbbb"
    Output: 1
    Explanation: "b"

Example 3:
    Input:  s = "pwwkew"
    Output: 3
    Explanation: "wke" (subsequence "pwke"가 아님 — 연속이어야 함)

## 조건 (Constraints)

- 0 <= s.length <= 5 * 10^4
- s는 영어 알파벳, 숫자, 기호, 공백으로 구성
"""


def lengthOfLongestSubstring(s: str) -> int:
    pass


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))   # Expected: 3
    print(lengthOfLongestSubstring("bbbbb"))      # Expected: 1
    print(lengthOfLongestSubstring("pwwkew"))     # Expected: 3
    print(lengthOfLongestSubstring(""))            # Expected: 0
    print(lengthOfLongestSubstring(" "))           # Expected: 1
