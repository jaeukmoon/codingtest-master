"""
[0015] 3Sum — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **중복 제거 기준**: triplet 값 기준인가요, 인덱스 기준인가요?
  → 값 기준. [-1,-1,2]가 인덱스 다른 두 가지로 만들어져도 결과엔 1번만.
- **반환 순서**: 정렬돼야 하나요?
  → 보통 무관. 다만 각 triplet 내부는 정렬된 형태가 깔끔.
- **음수/0/양수 분포**: 모두 양수면 답 없음이라는 거 알고 시작.

## 2. 엣지 케이스

- 길이 < 3 → []
- 모두 0 → [[0,0,0]] (단 한 개)
- 같은 값이 많이 중복 [-1,-1,-1,-1,2,2] → 중복 triplet 제거 필요
- 정답 없음 [1,2,3,4] → []
- 음수 큰 값 + 양수 작은 값들

## 3. 알고리즘 선택

### Brute force O(n³)
3중 루프 + set으로 중복 제거 → n=3000일 때 2.7*10^10, 시간 초과.

### Hashset 2sum O(n²) 평균
각 i 고정 후 나머지를 2sum으로. 가능하지만 중복 제거가 까다로움.

### Sort + Two pointers O(n²) ← 채택
1. 배열 정렬 O(n log n).
2. i를 0..n-3까지 고정.
3. nums[i] 이후 구간에서 two-pointer로 합이 -nums[i]인 쌍 찾기.
4. **중복 처리 핵심**:
   - i 단계: nums[i] == nums[i-1]이면 skip.
   - two pointer 매칭 후: left, right 양쪽도 같은 값 skip.
5. **조기 종료(early exit)**: 정렬했으므로 nums[i] > 0이면 더 볼 필요 없음
   (i 이후는 다 양수 → 합 > 0).

이게 가장 깔끔하고 면접에서 선호됨. 중복 제거가 정렬 덕분에 O(1)로 처리됨.

## 4. 복잡도

- 시간: O(n²) — 정렬 O(n log n) + 외부 i 루프 O(n) * 내부 two-pointer O(n)
- 공간: O(1) 추가 (출력 제외). 정렬을 in-place로 하면.
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # 예시: nums = [-1, 0, 1, 2, -1, -4]
    nums.sort()
    # 정렬 후: [-4, -1, -1, 0, 1, 2]
    n = len(nums)
    result: List[List[int]] = []

    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        target = -nums[i]

        # i=0: nums[i]=-4, target=4, left=1, right=5
        #   [-4, -1, -1, 0, 1, 2]  → -1+2=1 < 4 → left++ ... 합 4 불가능
        #
        # i=1: nums[i]=-1, target=1, left=2, right=5
        #   nums[2]+nums[5] = -1+2 = 1 == target → 찾음! [-1,-1,2]
        #   left=3, right=4 → nums[3]+nums[4] = 0+1 = 1 == target → [-1,0,1]
        #   left=4, right=3 → left >= right → 종료
        #
        # i=2: nums[2]=-1 == nums[1]=-1 → 중복 skip!
        # i=3: nums[3]=0 → target=0, left=4, right=5 → 1+2=3 > 0 → right-- → 종료
        # 결과: [[-1,-1,2], [-1,0,1]]

        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]
    print(threeSum([0, 1, 1]))                # []
    print(threeSum([0, 0, 0]))                # [[0,0,0]]
    print(threeSum([0, 0, 0, 0]))             # [[0,0,0]] (중복 제거 확인)
    print(threeSum([-2, 0, 1, 1, 2]))         # [[-2,0,2],[-2,1,1]]
