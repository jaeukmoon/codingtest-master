"""
[0278] First Bad Version (Easy)
https://leetcode.com/problems/first-bad-version/

## 문제

n개의 버전 [1, 2, ..., n]이 있다. 어느 시점부터 이후 버전은 모두 불량이다.
`isBadVersion(version)` API로 특정 버전이 불량인지 확인할 수 있다.
API 호출 횟수를 최소화하면서 최초 불량 버전을 찾아 반환하라.

## 예시

Example 1:
    Input:  n = 5, bad = 4
    Output: 4
    Explanation:
        isBadVersion(3) → false
        isBadVersion(5) → true
        isBadVersion(4) → true
        → first bad version is 4

Example 2:
    Input:  n = 1, bad = 1
    Output: 1

## 조건 (Constraints)

- 1 <= bad <= n <= 2^31 - 1

## 힌트

- 이진 탐색의 핵심: "정답 자체"가 아니라 "정답의 경계"를 찾는다.
- isBadVersion(mid)가 True이면 → 답은 mid 이하 (right = mid)
- isBadVersion(mid)가 False이면 → 답은 mid 초과 (left = mid + 1)
- 704번과 종료 조건 비교: while left < right vs left <= right
"""


def solution(isBadVersion):
    def firstBadVersion(n: int) -> int:
        pass
    return firstBadVersion


if __name__ == "__main__":
    def make_checker(bad):
        def isBadVersion(v): return v >= bad
        return isBadVersion

    fn = solution(make_checker(4))
    print(fn(5))    # Expected: 4

    fn = solution(make_checker(1))
    print(fn(1))    # Expected: 1

    fn = solution(make_checker(1))
    print(fn(2126753390))   # Expected: 1
