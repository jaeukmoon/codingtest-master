"""
[0242] Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

## 문제

문자열 `s`와 `t`가 주어진다.
`t`가 `s`의 애너그램이면 `true`, 아니면 `false`를 반환하라.
애너그램이란 같은 글자들로 구성된 단어를 말한다.

## 예시

Example 1:
    Input:  s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input:  s = "rat", t = "car"
    Output: false

## 조건 (Constraints)

- 1 <= s.length, t.length <= 5 * 10^4
- s와 t는 소문자 영어 알파벳으로만 구성된다.

## Follow-up

유니코드 문자가 포함된 경우에는 어떻게 처리할까?
"""


def isAnagram(s: str, t: str) -> bool:
    pass


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))   # Expected: True
    print(isAnagram("rat", "car"))           # Expected: False
    print(isAnagram("listen", "silent"))     # Expected: True
