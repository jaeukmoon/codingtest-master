"""
[0049] Group Anagrams — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **문자 집합**: 소문자 영어 알파벳뿐인가요? (제약조건상 그렇긴 함)
  → 답에 따라 카운트 키 생성 방식이 달라짐 (길이 26 튜플 vs 정렬 문자열).
- **빈 문자열도 그룹의 멤버가 되나요?**
  → 네 — [""]는 [[""]].
- **출력 순서**: 그룹 순서, 그룹 내 원소 순서 둘 다 무관 맞나요?
- **유니코드/대소문자 혼재** 가능성? — 제약조건상 없지만 확장성 측면에서 언급할 수 있음.

## 2. 엣지 케이스

- 빈 입력 [] → []
- 단일 원소 ["a"] → [["a"]]
- 빈 문자열 [""] → [[""]]
- 모두 같은 그룹 ["abc","bca","cab"] → 하나의 그룹
- 모두 다른 그룹 ["a","b","c"]
- 같은 문자가 반복 ["aab", "aba", "baa"] — 단순 set 비교는 틀림! ("ab" vs "aab" 구분 못함)

## 3. 알고리즘 선택

### 잘못된 접근: set(str) 사용
원래 코드 시도가 이거였는데, set은 중복을 잃음. "aab"와 "ab"가 같은 그룹으로 묶임 → 오답.
**문자 개수까지 정확히 같아야 anagram.**

### 방법 A: 정렬한 문자열을 키로 ← 직관적
- key = "".join(sorted(s))
- 시간: O(N * K log K), K = 평균 문자열 길이

### 방법 B: 26개 카운트 튜플을 키로 ← 점근적으로 더 빠름 (채택)
- 각 문자열의 알파벳별 개수를 26차원 튜플로
- 시간: O(N * K)
- 소문자만 들어온다는 제약을 활용한 최적화

면접에서는 B를 제시하면서 "정렬 방식은 더 일반적이지만, 소문자라는 제약이 있으니
26개 카운트가 K log K 인자를 떼낼 수 있다"고 트레이드오프 설명하면 좋다.

## 4. 복잡도

- 시간: O(N * K), N=문자열 개수, K=평균 길이
- 공간: O(N * K) — 해시맵에 모든 문자열 보관
"""
from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    # 예시: strs = ["eat", "tea", "tan"]
    for s in strs:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        # s="eat" → counts[0]=1(a), counts[4]=1(e), counts[19]=1(t) → 나머지 0
        # key = (1,0,0,0,1,0,...,1,...,0)  ← 26자리 튜플
        # groups = {(1,0,0,0,1,...,1,...,0): ["eat"]}
        #
        # s="tea" → 같은 알파벳 구성 → 같은 key 생성!
        # groups = {(1,0,0,0,1,...,1,...,0): ["eat", "tea"]}
        #
        # s="tan" → counts[0]=1(a), counts[13]=1(n), counts[19]=1(t)
        # 다른 key → 새 그룹 생성
        # groups = {(1,0,0,0,1,...,1,...,0): ["eat", "tea"],
        #           (1,0,...,1,...,1,...,0):  ["tan"]}
        groups[tuple(counts)].append(s)

    # groups.values() = [["eat", "tea"], ["tan"]]
    return list(groups.values())


# ================================================================
# 방법 B: sorted 문자열을 키로 (더 직관적, 코드 짧음)
# ================================================================
def groupAnagrams_sorted(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    # 예시: strs = ["eat", "tea", "tan"]
    for s in strs:
        key = "".join(sorted(s))
        # s="eat" → sorted("eat") = ['a','e','t'] → key = "aet"
        # s="tea" → sorted("tea") = ['a','e','t'] → key = "aet"  ← 같은 키!
        # s="tan" → sorted("tan") = ['a','n','t'] → key = "ant"  ← 다른 키
        groups[key].append(s)

    # groups = {"aet": ["eat", "tea"], "ant": ["tan"]}
    return list(groups.values())


# ================================================================
# 시간 복잡도 비교 (N = 문자열 개수, K = 평균 문자열 길이)
# ================================================================
# 방법 A (카운트 튜플):  O(N * K)      — 각 문자열을 한번 순회
# 방법 B (sorted 키):    O(N * K logK) — 각 문자열을 정렬
#
# K가 작으면 (대부분 코테) 차이 미미. 둘 다 통과함.
# K가 크면 방법 A가 유리. 단, 소문자 알파벳만이라는 제약 필요.
# 면접에서는 B 먼저 제시 → "소문자 제약 활용하면 A로 최적화 가능" 흐름이 이상적.
# ================================================================


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(groupAnagrams([""]))    # [[""]]
    print(groupAnagrams(["a"]))   # [["a"]]
    print(groupAnagrams(["ab", "aab", "ba"]))   # [["ab","ba"],["aab"]] — set 함정 테스트


# ─────────────────────────────────────────────────────────────────
# 내 풀이: 카운트 튜플 (defaultdict + 26자리 카운트)
# ─────────────────────────────────────────────────────────────────
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     groups = defaultdict(list)
#     for s in strs:
#         counts = [0] * 26
#         for c in s:
#             counts[ord(c)-ord('a')] += 1
#         groups[tuple(counts)].append(s)
#     return list(groups.values)
