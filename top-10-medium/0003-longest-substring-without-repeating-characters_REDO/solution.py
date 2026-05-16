"""
[0003] Longest Substring Without Repeating Characters — Solution

================================================================
면접에서 처음 문제를 봤을 때 어떻게 접근할까
================================================================

## 1. 면접관에게 먼저 확인할 것 (Clarifying Questions)

"몇 가지 먼저 여쭤봐도 될까요?"

- **문자 집합**: ASCII만 가정해도 되나요, 아니면 유니코드(이모지 등)도 들어오나요?
  → 답에 따라 카운터 자료구조 크기/구현이 달라짐. ASCII면 길이 128짜리 배열도 가능.
- **부분 문자열(substring) vs 부분 수열(subsequence)**: 연속이어야 한다는 거 맞죠?
  → 문제는 "substring"이므로 **연속**. (subsequence였다면 알고리즘이 완전 달라짐)
- **반환값**: 길이만 반환하면 되나요, 문자열 자체도 필요한가요?
  → 길이만. (필요하면 (start, length)를 추적해서 잘라내면 됨)
- **대소문자 구분**: "Aa"는 길이 2인가요 1인가요?
  → 보통은 구분 (서로 다른 문자). 명시적으로 확인.

## 2. 엣지 케이스

- 빈 문자열 ""   → 0
- 길이 1 " "    → 1 (공백도 문자)
- 모두 같은 문자 "bbbb" → 1
- 모두 다른 문자 "abcdef" → len(s)
- 매우 긴 입력(5*10^4) → O(n²)는 위험, O(n) 목표.

## 3. 알고리즘 선택 — 왜 슬라이딩 윈도우인가

### Brute force (O(n²) ~ O(n³))
모든 부분 문자열을 만들어 중복 체크 → 시간 초과 가능.

### Sliding Window + Hash (O(n)) ← 채택
- 윈도우 [left, right]를 유지하면서 right를 한 칸씩 늘려간다.
- 새로 들어오는 문자가 이미 윈도우 안에 있으면, **그 문자가 마지막으로 나타난 위치+1**까지 left를 점프시킨다.
- "마지막 위치"를 O(1)에 알기 위해 `dict[char] = last_index` 해시맵 사용.

핵심 통찰: left는 절대 뒤로 가지 않는다 → 양 포인터가 각각 최대 n번씩 이동 → O(n).

### 흔히 하는 실수
- `left = last_seen[c] + 1`로 무조건 갱신하면 안 됨.
  이미 left가 그 위치를 지나갔을 수도 있음(과거의 중복).
  → `left = max(left, last_seen[c] + 1)`로 단조 증가 보장해야 함.

## 4. 복잡도

- 시간: O(n)
- 공간: O(min(n, σ)) — σ는 문자 집합 크기

## 5. 두 가지 슬라이딩 윈도우 스타일 비교

| 항목 | 방식 A: set + while (left 한 칸씩) | 방식 B: dict + 점프 (채택) |
|---|---|---|
| 자료구조 | `set[char]` | `dict[char, last_index]` |
| 중복 처리 | while로 왼쪽에서 한 칸씩 빼며 축소 | 중복 문자 직후로 left를 **점프** |
| 시간복잡도 | O(n) (amortized — 각 문자 최대 1번 add/remove) | O(n) |
| 직관성 | "윈도우를 좁힌다"는 의미가 코드에 그대로 | 인덱스 계산 한 줄로 끝나 간결 |
| 실수 포인트 | 적음 (while 조건만 맞으면 됨) | `last_seen[c] >= left` 가드 필수 (안 그러면 left가 뒤로 감) |

→ 면접에선 **B를 메인으로, A를 "더 직관적인 변형"** 으로 언급하면 좋음.
"""


# ─────────────────────────────────────────────────────────────
# 방식 A: set + while (left를 한 칸씩 미는 직관적 버전)
# ─────────────────────────────────────────────────────────────
def lengthOfLongestSubstring_set(s: str) -> int:
    window: set[str] = set()
    left = 0
    best = 0

    # 예시: s = "dvdf"
    for right, c in enumerate(s):
        # 새로 들어올 c가 이미 윈도우에 있으면, 그 c가 사라질 때까지 왼쪽 축소
        while c in window:
            window.remove(s[left])
            left += 1
        window.add(c)
        best = max(best, right - left + 1)

        # right=0, c='d' → window={d},   [0,0] "d",  best=1
        # right=1, c='v' → window={d,v}, [0,1] "dv", best=2
        # right=2, c='d' → 'd' in window → s[0]='d' 제거, left=1
        #                  → window={v,d}, [1,2] "vd", best=2
        # right=3, c='f' → window={v,d,f}, [1,3] "vdf", best=3

    # ─────────────────────────────────────────────────────────────
    # 그림으로 이해하기 — s = "dvdf"
    # ─────────────────────────────────────────────────────────────
    #
    # 핵심 개념:
    #   window = 현재 윈도우 안에 있는 문자들의 집합 (set)
    #   left   = 윈도우 왼쪽 끝
    #   right  = 윈도우 오른쪽 끝
    #
    # ⚠️ B와 다른 점: window는 "현재 윈도우"만 담는다.
    #    윈도우에서 빠지면 set에서도 제거됨 → "옛날 기록" 자체가 없음
    #    → 그래서 가드(`>= left`) 같은 게 필요 없다!
    #
    # ─── Step 1) right=0, 'd' ───
    #   index:  0   1   2   3
    #   char:   d   v   d   f
    #           ↑
    #          L,R
    #   window: {d}, best=1
    #
    # ─── Step 2) right=1, 'v' ───
    #   index:  0   1   2   3
    #   char:   d   v   d   f
    #           ↑   ↑
    #           L   R
    #   window: {d, v}, best=2
    #
    # ─── Step 3) right=2, 'd' ← 중복! while 루프 시작 ───
    #   'd' in window → True → 한 칸씩 빼면서 좁힘:
    #
    #   [while 1회차]  s[left]=s[0]='d' 제거, left=1
    #     index:  0   1   2   3
    #     char:   d   v   d   f
    #                 ↑   ↑
    #                 L   R
    #     window: {v}        ← 'd'가 빠졌으니 while 종료
    #
    #   이제 'd' 추가:
    #     window: {v, d}, best=2
    #
    # ─── Step 4) right=3, 'f' ───
    #   index:  0   1   2   3
    #   char:   d   v   d   f
    #               ↑       ↑
    #               L       R
    #   window: {v, d, f}, best=3 ✅
    #
    # ─────────────────────────────────────────────────────────────
    # 좀 더 극적인 예: s = "abba" (가드 없이도 잘 되는지 확인)
    # ─────────────────────────────────────────────────────────────
    #
    # right=2, 'b' (현재 윈도우 {a,b}):
    #   [while 1회차]  s[0]='a' 제거, left=1
    #     window: {b}        ← 아직 'b' 있음, 계속
    #   [while 2회차]  s[1]='b' 제거, left=2
    #     window: {}         ← 'b' 빠졌으니 while 종료
    #   추가:
    #     index:  0   1   2   3
    #     char:   a   b   b   a
    #                     ↑
    #                    L,R
    #     window: {b}
    #
    # right=3, 'a':
    #   'a' in window? → window={b}이므로 ❌ NO
    #   바로 추가:
    #     index:  0   1   2   3
    #     char:   a   b   b   a
    #                     ↑   ↑
    #                     L   R
    #     window: {b, a}, best=2 ✅
    #
    # → B에서 골치 아팠던 "옛날 'a'" 문제가 A에선 자동으로 해결됨!
    #   set에서 이미 빠졌기 때문에 `'a' in window`가 False라서
    #   그냥 추가만 하면 끝.
    #
    # ─────────────────────────────────────────────────────────────
    # A vs B 한눈에
    # ─────────────────────────────────────────────────────────────
    #
    # 방식 A: "윈도우를 한 칸씩 좁힌다"
    #         ┌──────────┐         ┌──────┐
    #         │ a b b a  │  →→→    │  b a │
    #         └──────────┘         └──────┘
    #         while로 점진적 축소     (set이 자동 정리됨)
    #
    # 방식 B: "한 번에 점프"
    #         ┌──────────┐         ┌──────┐
    #         │ a b b a  │  ─jump→ │  b a │
    #         └──────────┘         └──────┘
    #         last_seen[b]+1 로 워프  (dict에 옛날 기록 남아있어서 가드 필요)

    return best


# ─────────────────────────────────────────────────────────────
# 방식 B: dict + 점프 (인덱스로 한 번에 건너뛰는 버전) ← 메인
# ─────────────────────────────────────────────────────────────
def lengthOfLongestSubstring(s: str) -> int:
    # last_seen[c] = 문자 c가 마지막으로 등장한 인덱스
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    # 예시: s = "abcab"
    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1

        last_seen[c] = right
        best = max(best, right - left + 1)

        # right=0, c='a' → last_seen={a:0}, 윈도우=[0,0] "a",  best=1
        # right=1, c='b' → last_seen={a:0,b:1}, 윈도우=[0,1] "ab", best=2
        # right=2, c='c' → last_seen={a:0,b:1,c:2}, 윈도우=[0,2] "abc", best=3
        # right=3, c='a' → 'a'가 last_seen에 있고 위치0 >= left(0)
        #                  → left = 0+1 = 1  (중복 'a' 다음으로 점프!)
        #                  → last_seen={a:3,b:1,c:2}, 윈도우=[1,3] "bca", best=3
        # right=4, c='b' → 'b'가 last_seen에 있고 위치1 >= left(1)
        #                  → left = 1+1 = 2
        #                  → last_seen={a:3,b:4,c:2}, 윈도우=[2,4] "cab", best=3

    # ─────────────────────────────────────────────────────────────
    # `last_seen[c] >= left` 가드가 왜 필요한가? — s = "abba" 로 풀이
    # ─────────────────────────────────────────────────────────────
    #
    # 핵심 개념:
    #   last_seen[c] = 문자 c를 "마지막으로 본" 인덱스 (영원히 기록됨, 지워지지 않음)
    #   left         = 현재 윈도우 왼쪽 끝
    #   right        = 현재 윈도우 오른쪽 끝
    #
    # ⚠️ last_seen은 윈도우가 움직여도 지워지지 않는다.
    #    그래서 "옛날 기록"이 남아있을 수 있음 → 가드가 필요한 이유.
    #
    # ─── Step 1) right=0, 'a' ───
    #   index:  0   1   2   3
    #   char:   a   b   b   a
    #           ↑
    #          L,R
    #   윈도우: [a]
    #   last_seen = {a:0}
    #
    # ─── Step 2) right=1, 'b' ───
    #   index:  0   1   2   3
    #   char:   a   b   b   a
    #           ↑   ↑
    #           L   R
    #   윈도우: [a, b]
    #   last_seen = {a:0, b:1}
    #
    # ─── Step 3) right=2, 'b' ← 중복 발생! ───
    #   index:  0   1   2   3
    #   char:   a   b   b   a
    #           ↑   ↑   ↑
    #           L  (옛b) R
    #
    #   last_seen[b]=1, left=0
    #   체크: 1 >= 0 ? ✅ YES → 윈도우 안에 진짜 중복!
    #   → left = 1 + 1 = 2 로 점프
    #
    #   점프 후:
    #   index:  0   1   2   3
    #   char:   a   b   b   a
    #                   ↑
    #                  L,R
    #   윈도우: [b]
    #   last_seen = {a:0, b:2}
    #
    # ─── Step 4) right=3, 'a' ← 여기가 포인트! ───
    #   index:  0   1   2   3
    #   char:   a   b   b   a
    #           ↑       ↑   ↑
    #         (옛a)     L   R
    #
    #   last_seen[a]=0, left=2
    #   체크: 0 >= 2 ? ❌ NO → 옛날 'a'는 이미 윈도우 밖!
    #   → left 그대로 둠 (점프 안 함)
    #
    # ─── 만약 `>= left` 가드가 없었다면? 😱 ───
    #   index:  0   1   2   3
    #   char:   a   b   b   a
    #           ↑           ↑
    #           L           R    ← left이 0+1=1 로 되돌아가버림!
    #   잘못된 윈도우: [b, b, a]  ← 'b'가 두 개! 망함
    #
    # ─── 한 줄 요약 ───
    #   last_seen[c]가 "옛날 위치"일 수도 있다.
    #     • 현재 윈도우 안(>= left)이면 → 진짜 중복 → 점프
    #     • 현재 윈도우 밖(<  left)이면 → 옛날 흔적 → 무시
    #   즉 `>= left`는 "이 중복이 지금도 유효한가?"를 검사하는 필터.

    return best


if __name__ == "__main__":
    tests = ["abcabcbb", "bbbbb", "pwwkew", "", " ", "dvdf", "abba"]
    expected = [3, 1, 3, 0, 1, 3, 2]
    for s, exp in zip(tests, expected):
        a = lengthOfLongestSubstring_set(s)
        b = lengthOfLongestSubstring(s)
        print(f"{s!r:12} set={a} dict={b} (expected {exp})")


# ─────────────────────────────────────────────────────────────
# 내 풀이: 시도 1 (작성 중 — 두 포인터 + set, 미완성)
# ─────────────────────────────────────────────────────────────
# def lengthOfLongestSubstring(s: str) -> int:
#     seen = set()
#     if len(s) == 0:
#         return 0
#     if len(s) == 1:
#         return 1
#     max_len = 0
#     first = 0
#     second = 1
#     if s[first] == s[second]:
#         return 1
#     seen.add(s[first],s[second])
#     for i,c in enumerate(s):
#         if s[second] in seen:
#             pass
#         second += 1


# ─────────────────────────────────────────────────────────────
# 내 풀이: 시도 2 (set 리셋 방식 — 일부 케이스에서 틀림)
# ─────────────────────────────────────────────────────────────
# def lengthOfLongestSubstring(s: str) -> int:
#     max_len = 0
#     tmp_set = set()
#     tmp_len = 0
#     for i,c in enumerate(s):
#         if c in tmp_set:
#             tmp_set = set()
#             tmp_len = 0
#         tmp_set.add(c)
#         tmp_len += 1
#         max_len = max(max_len, tmp_len)
#     return max_len
#
# """
#     c  tmp_set. tmp_len.  max_len.
# 0.  a    (a).      1         1
# 1   b.    (a,b)    2         2
# 2.  a.     (a).    1         2
# """
