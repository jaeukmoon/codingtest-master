"""
[0424] Longest Repeating Character Replacement (Medium)
https://leetcode.com/problems/longest-repeating-character-replacement/

## 문제

문자열 `s`와 정수 `k`가 주어진다.
임의의 글자를 다른 영문 대문자로 **최대 k번** 바꿀 수 있다.
이렇게 해서 만들 수 있는, **같은 글자로만 구성된 가장 긴 substring**의 길이를 반환하라.

## 예시

Example 1:
    Input:  s = "ABAB", k = 2
    Output: 4
    Explanation: 두 'A'를 'B'로 바꾸거나 그 반대.

Example 2:
    Input:  s = "AABABBA", k = 1
    Output: 4
    Explanation: 가운데 'A'를 'B'로 → "AABBBBA" → "BBBB" 길이 4.

## 조건 (Constraints)

- 1 <= s.length <= 10^5
- s는 영문 대문자만
- 0 <= k <= s.length
"""


def characterReplacement(s: str, k: int) -> int:
    pass


if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))     # 4
    print(characterReplacement("AABABBA", 1))  # 4
    print(characterReplacement("ABCDE", 1))    # 2
