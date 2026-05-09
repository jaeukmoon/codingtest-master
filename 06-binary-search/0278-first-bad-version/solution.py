"""
[0278] First Bad Version (Easy)
https://leetcode.com/problems/first-bad-version/

## 문제

n개의 버전 [1, 2, ..., n]이 있다. 어느 시점부터 이후 버전은 모두 불량이다.
`isBadVersion(v)` API로 특정 버전이 불량인지 확인할 수 있다.
API 호출 횟수를 최소화하면서 최초 불량 버전을 반환하라.

## 예시

Example 1:
    Input:  n = 5, bad = 4
    Output: 4

Example 2:
    Input:  n = 1, bad = 1
    Output: 1

## 조건

- 1 <= bad <= n <= 2^31 - 1

---

핵심 아이디어:
    경계 이진 탐색. isBadVersion(mid)가 True면 right = mid (mid가 답일 수 있음).
    False면 left = mid + 1. left == right일 때 첫 불량 버전.
    704번과 차이: right = mid - 1이 아니라 right = mid.

자료구조 / 패턴:
    - Binary Search (경계 탐색)

시간복잡도: O(log n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I use binary search to find the boundary between good and bad versions.
     If mid is bad, the first bad version is at mid or earlier, so right = mid.
     If mid is good, it must be after mid, so left = mid + 1.
     The loop ends when left == right, which is the answer."

엣지 케이스:
    - bad = 1: 첫 번째부터 불량
    - bad = n: 마지막만 불량
    - n이 2^31 - 1에 가까울 때: mid = left + (right - left) // 2 로 overflow 방지
"""


## 손 추적 (Hand Trace)
# n=5, bad=4 (버전 4부터 불량)
#
#  left | right | mid | isBadVersion(mid) | 판단
# ------|-------|-----|-------------------|------------------
#   1   |   5   |  3  |      False        | left=4
#   4   |   5   |  4  |      True         | right=4
#   4   |   4   |  -  |      -            | left==right → return 4 ✓
#
# 704번과 비교:
#  - 704: while left <= right, right = mid-1  (정확한 값 탐색)
#  - 278: while left < right,  right = mid    (경계 탐색, mid가 답일 수 있음)


def solution(isBadVersion):
    def firstBadVersion(n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2   # overflow 방지
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

    return firstBadVersion


if __name__ == "__main__":
    def make_checker(bad):
        def isBadVersion(v): return v >= bad
        return isBadVersion

    fn = solution(make_checker(4))
    print(fn(5))              # 4

    fn = solution(make_checker(1))
    print(fn(1))              # 1

    fn = solution(make_checker(1))
    print(fn(2126753390))     # 1
