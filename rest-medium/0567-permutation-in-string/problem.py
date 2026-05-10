"""
[0567] Permutation in String (Medium)
https://leetcode.com/problems/permutation-in-string/

## 문제

두 문자열 `s1`, `s2`가 주어진다.
`s2`가 `s1`의 **순열 중 하나를 substring으로 포함**하면 true 반환.

## 예시

Example 1:
    Input:  s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2가 "ba" (s1의 순열) 포함.

Example 2:
    Input:  s1 = "ab", s2 = "eidboaoo"
    Output: false

## 조건 (Constraints)

- 1 <= s1.length, s2.length <= 10^4
- s1, s2는 소문자 영문자만
"""


def checkInclusion(s1: str, s2: str) -> bool:
    pass


if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))   # True
    print(checkInclusion("ab", "eidboaoo"))   # False
    print(checkInclusion("hello", "ooolleoooleh"))   # False
