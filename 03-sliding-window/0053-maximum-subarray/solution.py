"""
[0053] Maximum Subarray (Medium)
링크: https://leetcode.com/problems/maximum-subarray/

문제:
    정수 배열에서 합이 가장 큰 연속 부분 배열의 합 반환.

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
