"""
[0053] Maximum Subarray (Medium)
링크: https://leetcode.com/problems/maximum-subarray/

## 문제

정수 배열 `nums`가 주어진다.
합이 가장 큰 연속 부분 배열(subarray)을 찾고, 그 합을 반환하라.
(부분 배열은 최소 1개 원소를 포함해야 한다)

## 예시

Example 1:
    Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6

Example 2:
    Input:  nums = [1]
    Output: 1

Example 3:
    Input:  nums = [5,4,-1,7,8]
    Output: 23

## 조건

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

---

핵심 아이디어 (Kadane's Algorithm):
    각 위치에서 "여기서 새로 시작" vs "이전부터 이어가기" 중 더 큰 쪽 선택.
    음수 누적합이면 버리고 현재값부터 새로 시작.

자료구조 / 패턴:
    - Sliding Window / DP (Kadane's Algorithm)

시간복잡도: O(n)
공간복잡도: O(1)

영어 멘트 (면접용):
    "I'll use Kadane's algorithm. At each position I decide: extend the current subarray,
     or start fresh from here. I keep track of the running sum and the global maximum.
     This is O(n) time and O(1) space."

엣지 케이스:
    - 모두 음수: [-3, -1, -2] → -1 (부분 배열은 최소 1개)
    - 원소 1개: 그 값 그대로
    - 0이 포함된 경우
"""


## 손 추적 (Hand Trace)
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
#  num | current_sum (max(num, prev+num)) | max_sum
# -----|----------------------------------|--------
#  -2  | -2          (초기값)             |  -2
#   1  | max(1, -2+1)  = max(1,-1)  =  1 |   1    ← 새로 시작
#  -3  | max(-3, 1-3)  = max(-3,-2) = -2 |   1
#   4  | max(4, -2+4)  = max(4,2)   =  4 |   4    ← 새로 시작
#  -1  | max(-1, 4-1)  = max(-1,3)  =  3 |   4
#   2  | max(2, 3+2)   = max(2,5)   =  5 |   5
#   1  | max(1, 5+1)   = max(1,6)   =  6 |   6
#  -5  | max(-5, 6-5)  = max(-5,1)  =  1 |   6
#   4  | max(4, 1+4)   = max(4,5)   =  5 |   6
# → return 6  ([4,-1,2,1])


def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)   # 새로 시작 vs 이어가기
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6 ([4,-1,2,1])
    print(maxSubArray([1]))                                  # 1
    print(maxSubArray([-2, -1]))                             # -1
