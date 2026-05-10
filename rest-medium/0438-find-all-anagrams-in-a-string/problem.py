"""
[0438] Find All Anagrams in a String (Medium)
https://leetcode.com/problems/find-all-anagrams-in-a-string/

## 문제

문자열 `s`와 `p`가 주어진다.
`s` 안에서 `p`의 **애너그램이 시작되는 모든 인덱스**를 반환하라. (순서 무관)

## 예시

Example 1:
    Input:  s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation: s[0:3] = "cba" (abc 애너그램), s[6:9] = "bac" (abc 애너그램)

Example 2:
    Input:  s = "abab", p = "ab"
    Output: [0,1,2]

## 조건 (Constraints)

- 1 <= s.length, p.length <= 3 * 10^4
- s, p는 소문자 영문자만
"""
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    pass


if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))   # [0,6]
    print(findAnagrams("abab", "ab"))           # [0,1,2]
