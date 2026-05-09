"""
[0217] Contains Duplicate (Easy)
링크: https://leetcode.com/problems/contains-duplicate/

## 문제

정수 배열 `nums`가 주어진다.
배열에 두 번 이상 등장하는 원소가 있으면 `true`, 모두 다르면 `false`를 반환하라.

## 예시

Example 1:
    Input:  nums = [1,2,3,1]
    Output: true

Example 2:
    Input:  nums = [1,2,3,4]
    Output: false

Example 3:
    Input:  nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

## 조건

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

---

핵심 아이디어:
    set에 원소를 하나씩 추가하면서 이미 있으면 True 반환.
    "이미 봤나" 체크는 set의 O(1) lookup으로.

자료구조 / 패턴:
    - set

시간복잡도: O(n)
공간복잡도: O(n)

영어 멘트 (면접용):
    "I'll use a set for O(1) duplicate detection. As I iterate, I check if each
     element is already in the set. If so, return True. Otherwise add it and continue."

엣지 케이스:
    - 원소 1개: False
    - 모두 같은 값: True
    - 빈 배열: False
"""


## 손 추적 (Hand Trace)
# nums = [1, 2, 3, 1]
#
#  num | seen (before)  | 결과
# -----|----------------|----------------------
#   1  | {}             | 없음 → add(1)
#   2  | {1}            | 없음 → add(2)
#   3  | {1,2}          | 없음 → add(3)
#   1  | {1,2,3}        | 있음! → return True


def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Pythonic 한 줄 버전 (면접 후 언급용)
# return len(set(nums)) != len(nums)


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))   # True
    print(containsDuplicate([1, 2, 3, 4]))   # False
    print(containsDuplicate([1]))             # False
