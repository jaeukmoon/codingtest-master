"""
[0155] Min Stack (Medium)
https://leetcode.com/problems/min-stack/

## 문제

다음 연산을 모두 O(1)에 지원하는 스택을 설계하라:
  - push(val): 스택에 원소 추가
  - pop(): 스택에서 원소 제거
  - top(): 스택의 top 원소 반환
  - getMin(): 스택의 최솟값 반환

## 예시

Example 1:
    Input:
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
    Output:
        [null,null,null,null,-3,null,0,-2]
    Explanation:
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();  → -3
        minStack.pop();
        minStack.top();     → 0
        minStack.getMin();  → -2

## 조건 (Constraints)

- -2^31 <= val <= 2^31 - 1
- pop(), top(), getMin()은 항상 비어있지 않은 스택에서 호출된다.
- push, pop, top, getMin 각각 최대 3 * 10^4번 호출된다.
"""


class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())   # Expected: -3
    ms.pop()
    print(ms.top())      # Expected: 0
    print(ms.getMin())   # Expected: -2
