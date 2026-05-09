"""
[0001] Two Sum (Easy)
링크: https://leetcode.com/problems/two-sum/

## 문제

정수 배열 `nums`와 정수 `target`이 주어진다.
합이 `target`이 되는 두 수의 인덱스를 반환하라.
같은 원소를 두 번 사용할 수 없으며, 정확히 하나의 답이 존재한다.

## 예시

Example 1:
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]

Example 2:
    Input:  nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input:  nums = [3,3], target = 6
    Output: [0,1]

## 조건

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- 정확히 하나의 유효한 답이 존재한다.

---

핵심 아이디어:
    dict에 "이미 본 값 → 인덱스" 저장.
    새 값이 들어올 때마다 complement(target - 현재값)이 dict에 있는지 확인.

자료구조 / 패턴:
    - dict (Hash Map)

시간복잡도: O(n)
공간복잡도: O(n)

영어 멘트 (면접용):
    "I'll use a hash map to store values I've seen along with their indices.
     For each number, I check if its complement (target - num) is already in the map.
     This gives O(n) time and O(n) space."

엣지 케이스:
    - 중복 값: [3, 3], target=6 → [0, 1]
    - 음수: [-1, -2], target=-3 → [0, 1]
    - 두 수가 붙어있지 않을 때
"""


## 손 추적 (Hand Trace)
# nums = [2, 7, 11, 15], target = 9
#
#  i | num | complement | seen (before add) | 결과
# ---|-----|------------|-------------------|------------------
#  0 |  2  |     7      | {}                | 없음 → seen[2]=0
#  1 |  7  |     2      | {2:0}             | 발견! → return [0,1]


def twoSum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(twoSum([3, 2, 4], 6))         # [1, 2]
    print(twoSum([3, 3], 6))            # [0, 1]
