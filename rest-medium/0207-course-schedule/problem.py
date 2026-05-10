"""
[0207] Course Schedule (Medium)
https://leetcode.com/problems/course-schedule/

## 문제

`numCourses`개 강의 (0번 ~ numCourses-1번).
선수 과목 배열 `prerequisites[i] = [a_i, b_i]`: a_i를 들으려면 b_i를 먼저 들어야 함.
모든 강의를 들을 수 있으면 true, 아니면 false 반환.

## 예시

Example 1:
    Input:  numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: 0 들으면 1 들을 수 있음.

Example 2:
    Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: 순환.

## 조건 (Constraints)

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= a_i, b_i < numCourses
- 모든 prerequisites pairs는 유일
"""
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))           # True
    print(canFinish(2, [[1,0],[0,1]]))     # False
    print(canFinish(4, [[1,0],[2,1],[3,2]]))   # True
    print(canFinish(3, [[0,1],[1,2],[2,0]]))   # False (cycle)
