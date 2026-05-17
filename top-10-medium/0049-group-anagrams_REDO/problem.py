"""
[0049] Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/

## 문제

문자열 배열 `strs`가 주어진다.
서로 anagram인 문자열들을 같은 그룹으로 묶어 반환하라.
(anagram = 같은 문자들을 재배열한 문자열)

그룹 순서, 그룹 내 원소 순서는 무관.

## 예시

Example 1:
    Input:  strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input:  strs = [""]
    Output: [[""]]

Example 3:
    Input:  strs = ["a"]
    Output: [["a"]]

## 조건 (Constraints)

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i]는 소문자 영어 알파벳으로만 구성
"""
from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    seen = defaultdict(list)
    for s in strs:
        count_dict = [0]*26
        for c in s:
            count_dict[ord(c)-ord('a')] += 1
        seen[tuple(count_dict)].append(s)
    return list(seen.values())

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     seen = defaultdict(list)
#     for s in strs:
#         key = ''.join(sorted(s))
#         seen[key].append(s)
#         # print(seen)
#     return list(seen.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected: [["eat","tea","ate"],["tan","nat"],["bat"]] (순서 무관)
    print(groupAnagrams([""]))                  # Expected: [[""]]
    print(groupAnagrams(["a"]))                 # Expected: [["a"]]
    print(groupAnagrams(["ab", "aab", "ba"]))   # Expected: [["ab","ba"],["aab"]]
