"""
[0242] Valid Anagram (Easy)
링크: https://leetcode.com/problems/valid-anagram/

문제:
    두 문자열 s, t가 anagram인지 확인 (같은 글자로 구성).

핵심 아이디어:
    각 문자의 빈도를 세서 비교.
    s로 카운트 올리고, t로 카운트 내리면서 0 미만 나오면 False.

자료구조 / 패턴:
    - dict (카운팅)

시간복잡도: O(n)
공간복잡도: O(1) — 알파벳 26개 고정 크기

영어 멘트 (면접용):
    "I'll count character frequencies for s, then decrement for each char in t.
     If any count goes below zero, t has a character s doesn't — not an anagram.
     I can also do this with Counter, but I'll walk through it manually first."

엣지 케이스:
    - 길이 다르면 즉시 False
    - 같은 문자 다른 빈도: "aab" vs "abb" → False
    - 대소문자 구분 (문제 기본 설정: lowercase only)
"""
from collections import defaultdict


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    for c in t:
        if counts[c] == 0:
            return False
        counts[c] -= 1

    return True


# Counter 한 줄 버전 (면접 후 언급용)
# from collections import Counter
# return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))   # True
    print(isAnagram("rat", "car"))           # False
    print(isAnagram("listen", "silent"))     # True
