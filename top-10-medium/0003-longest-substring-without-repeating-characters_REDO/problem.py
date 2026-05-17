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
# dvdf
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    window = set()
    left = 0
    right = 0
    for right, c in enumerate(s):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(c)
        max_len = max(max_len,right-left+1)
    return max_len

"""
================================================================
손 디버깅 (whiteboard / Google Docs 용)
================================================================

전략:
  1. 어려운 케이스 하나만 골라서 추적 (예: "pwwkew" — 중복으로 left 이동 필요)
  2. 표 헤더에 "상태 변수 전부" 나열: r, c, left, window, max_len
  3. while 루프가 여러 번 도는 step은 한 행에 sub-step으로 들여쓰기
  4. max_len이 갱신되는 줄에 ★ 표시 → 검증할 때 빠르게 눈으로 확인

s = "pwwkew"
     0 1 2 3 4 5

step | r | c | action               | left | window    | max_len
-----+---+---+----------------------+------+-----------+---------
init |   |   |                      |  0   | {}        |   0
  1  | 0 | p | add p                |  0   | {p}       |   1  ★
  2  | 1 | w | add w                |  0   | {p,w}     |   2  ★
  3  | 2 | w | w∈win → rm s[0]=p    |  1   | {w}       |
     |   |   | w∈win → rm s[1]=w    |  2   | {}        |
     |   |   | add w                |  2   | {w}       |   2
  4  | 3 | k | add k                |  2   | {w,k}     |   2
  5  | 4 | e | add e                |  2   | {w,k,e}   |   3  ★
  6  | 5 | w | w∈win → rm s[2]=w    |  3   | {k,e}     |
     |   |   | add w                |  3   | {k,e,w}   |   3

return 3 ✓

면접 팁:
  - 표 그리기 전에 한 줄로 "invariant: window = s[left..right] 의 문자 집합,
    중복 없음" 명시하면 면접관이 의도 파악 쉬움
  - 엣지 케이스는 표 말고 한 줄로:  s=""→0,  s=" "→1,  s="bbb"→1
"""


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))   # Expected: 3
    print(lengthOfLongestSubstring("bbbbb"))      # Expected: 1
    print(lengthOfLongestSubstring("pwwkew"))     # Expected: 3
    print(lengthOfLongestSubstring(""))            # Expected: 0
    print(lengthOfLongestSubstring(" "))           # Expected: 1
