"""
[0033] Search in Rotated Sorted Array — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **중복 원소 있나요?**
  → 이 문제는 "모든 원소 유일". 중복이 있으면 [LC 81]이 되고 worst case O(n)으로 떨어짐.
- **회전 안 됐을 수도 있나요?**
  → 네 (피벗=0인 경우). 알고리즘이 그것도 자연스럽게 처리해야 함.
- **빈 배열 들어오나요?**
  → 제약조건상 1 이상이지만, 방어적으로 처리 가능.
- **O(log n) 강제** — 두 번 binary search 해도 되지만 한 번에 끝내는 게 깔끔.

## 2. 엣지 케이스

- nums=[1], target=1 → 0
- nums=[1], target=0 → -1
- nums=[3,1], target=1 → 1 (작은 배열에서 mid 처리 주의)
- 회전 안 한 배열 [1,2,3,4,5]
- target이 배열 양 끝값
- target이 피벗 직전/직후 (경계)

## 3. 알고리즘 선택

### 발상
정렬된 배열에 회전이 추가됐을 뿐. binary search는 "현재 구간이 정렬돼 있다"는 가정이 필요한데,
회전 배열도 **mid를 기준으로 자르면 한쪽은 반드시 정렬**되어 있다는 성질이 있음.

예: [4,5,6,7,0,1,2], mid=3(=7)
  - 왼쪽 [4,5,6,7] 정렬됨
  - 오른쪽 [0,1,2] 정렬됨
  → 둘 중 한쪽은 반드시 정렬됨.

### One-pass Binary Search ← 채택
- mid 계산
- **nums[left] <= nums[mid]** 이면 왼쪽 절반이 정렬됨
  - target이 그 정렬된 구간 안에 있는지 확인 → 안에 있으면 right=mid-1, 아니면 left=mid+1
- 그렇지 않으면 오른쪽 절반이 정렬됨
  - 같은 방식으로 분기

**`<=` vs `<` 주의**: 길이 1짜리(left==mid) 케이스에서 nums[left]==nums[mid]가 됨.
이걸 "왼쪽이 정렬됨"으로 처리해야 [3,1] target=1 같은 케이스가 풀린다.

## 4. 복잡도

- 시간: O(log n)
- 공간: O(1)
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    # 예시: nums = [4,5,6,7,0,1,2], target = 0
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # 왼쪽 [left..mid]가 정렬됨
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # 오른쪽 [mid..right]가 정렬됨
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        # 1회차: left=0, right=6, mid=3 → nums[3]=7 ≠ 0
        #   nums[0]=4 <= nums[3]=7 → 왼쪽 [4,5,6,7] 정렬됨
        #   target=0이 4~7 사이? → NO → left = 4
        #
        # 2회차: left=4, right=6, mid=5 → nums[5]=1 ≠ 0
        #   nums[4]=0 <= nums[5]=1 → 왼쪽 [0,1] 정렬됨
        #   target=0이 0~1 사이? → 0 <= 0 < 1 → YES → right = 4
        #
        # 3회차: left=4, right=4, mid=4 → nums[4]=0 == target → return 4

    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))   # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))   # -1
    print(search([1], 0))                       # -1
    print(search([1], 1))                       # 0
    print(search([3, 1], 1))                    # 1 — 작은 배열 경계 케이스
    print(search([5, 1, 3], 3))                 # 2
    print(search([1, 2, 3, 4, 5], 3))           # 2 — 회전 없는 경우
