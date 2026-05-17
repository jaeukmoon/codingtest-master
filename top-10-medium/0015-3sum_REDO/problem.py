"""
[0015] 3Sum (Medium)
https://leetcode.com/problems/3sum/

## 문제

정수 배열 `nums`가 주어진다.
i, j, k가 모두 다르고 nums[i] + nums[j] + nums[k] == 0인 모든 triplet을 반환하라.
**중복된 triplet은 결과에 포함되지 말아야 한다.**

## 예시

Example 1:
    Input:  nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
        nums[0] + nums[1] + nums[2] = -1+0+1 = 0
        nums[1] + nums[2] + nums[4] = 0+1+(-1) = 0
        nums[0] + nums[3] + nums[4] = -1+2+(-1) = 0
        중복 [-1,0,1]은 한 번만.

Example 2:
    Input:  nums = [0,1,1]
    Output: []

Example 3:
    Input:  nums = [0,0,0]
    Output: [[0,0,0]]

## 조건 (Constraints)

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""
from typing import List

# 공간 복잡도가 O(n²)
# def twosum(target, nums_list):
#     seen = set()
#     pair = []
#     for num in nums_list:
#         counter = target-num
#         if counter in seen:
#             pair.append((counter,num))
#         seen.add(num)
#     return pair

# def threeSum(nums: List[int]) -> List[List[int]]:
#     result_set = set()
#     for i in range(len(nums)):
#         counter = -nums[i]
#         pair = twosum(counter,nums[i+1:])
#         for a,b in pair:
#             triplet = tuple(sorted([nums[i],a,b]))
#             result_set.add(triplet)
#     return [list(t) for t in result_set]

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort() # O(nlogn)
    n = len(nums)
    result = []

    for i in range(n-2):
        if nums[i]>0:
            break
        if i>0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1,n-1
        target = -nums[i]
        while left<right:
            s = nums[left] + nums[right]
            if s == target:
                result.append([nums[i],left,right])
                left += 1
                right -= 1
                while left<right and nums[left] == nums[left-1]:
                    left += 1
                while left<right and nums[right] == nums[right+1]:
                    right -= 1
            elif s<target:
                left += 1
            else:
                right -= 1
    return result
            


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))   # Expected: [[-1,-1,2],[-1,0,1]]
    print(threeSum([0,1,1]))             # Expected: []
    print(threeSum([0,0,0]))             # Expected: [[0,0,0]]
