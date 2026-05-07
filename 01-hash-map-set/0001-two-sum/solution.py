"""
[0001] Two Sum (Easy)
링크: https://leetcode.com/problems/two-sum/

문제:
    정수 배열 nums와 target이 주어질 때, 합이 target이 되는 두 수의 인덱스를 반환.

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
