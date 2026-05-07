"""
[0217] Contains Duplicate (Easy)
링크: https://leetcode.com/problems/contains-duplicate/

문제:
    배열에 중복 원소가 하나라도 있으면 True, 없으면 False 반환.

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
