"""
[0739] Daily Temperatures (Medium)
https://leetcode.com/problems/daily-temperatures/

## 문제

각 날의 기온을 담은 배열 `temperatures`가 주어진다.
배열 `answer`를 반환하라. `answer[i]`는 i번째 날 이후, 기온이 더 높아지는 날까지의 일수.
그런 날이 없으면 0.

## 예시

Example 1:
    Input:  temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input:  temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Example 3:
    Input:  temperatures = [30,60,90]
    Output: [1,1,0]

## 조건 (Constraints)

- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    pass


if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))   # Expected: [1,1,4,2,1,1,0,0]
    print(dailyTemperatures([30,40,50,60]))                # Expected: [1,1,1,0]
    print(dailyTemperatures([30,60,90]))                   # Expected: [1,1,0]
