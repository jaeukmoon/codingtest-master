"""
[0349] Intersection of Two Arrays (Easy)
링크: https://leetcode.com/problems/intersection-of-two-arrays/

문제:
    두 배열의 교집합을 중복 없이 반환.

핵심 아이디어:
    nums1을 set으로 변환 후, nums2를 순회하면서 set1에 있으면 result에 추가.
    result도 set으로 관리해서 중복 자동 제거.

자료구조 / 패턴:
    - set (교집합)

시간복잡도: O(n + m)
공간복잡도: O(n)

영어 멘트 (면접용):
    "I'll convert nums1 to a set for O(1) lookups. Then iterate nums2 and collect
     elements that appear in the set. I use a result set to avoid duplicates.
     Alternatively, Python's set intersection operator & handles this in one line."

엣지 케이스:
    - 교집합 없음: []
    - 한쪽이 빈 배열: []
    - 한쪽에 중복 많은 경우 → set이 자동 처리
"""


def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)


# set 연산자 버전 (면접 후 언급용)
# return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))            # [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))      # [9, 4] (순서 무관)
    print(intersection([1, 2, 3], [4, 5, 6]))             # []
