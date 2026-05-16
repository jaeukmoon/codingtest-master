"""
[0049] Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/

## 문제

문자열 배열 `strs`가 주어진다.
애너그램끼리 그룹지어 반환하라. 그룹의 순서, 그룹 내 원소 순서는 무관.

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
    pass



if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]] (순서 무관)
    print(groupAnagrams([""]))    # Expected: [[""]]
    print(groupAnagrams(["a"]))   # Expected: [["a"]]
