"""
[0155] Min Stack (Medium)
링크: https://leetcode.com/problems/min-stack/

문제:
    push, pop, top, getMin을 모두 O(1)에 지원하는 스택 구현.

핵심 아이디어:
    스택 두 개: 일반 스택 + min 추적 스택.
    push 시 새 값이 현재 최솟값 이하면 min_stack에도 push.
    pop 시 꺼낸 값이 현재 최솟값이면 min_stack에서도 pop.

자료구조 / 패턴:
    - Stack (보조 자료구조로 추가 정보 추적) / OOP 설계

시간복잡도: O(1) all operations
공간복잡도: O(n)

영어 멘트 (면접용):
    "I maintain two stacks: the main stack and a min-tracking stack.
     The min stack's top always holds the current minimum.
     I push to min stack when the new value is <= current min, and pop from it
     when the popped value equals the current min. All operations are O(1)."

엣지 케이스:
    - 중복 최솟값: [2,0,3,0] → pop 후에도 min은 0이어야 함 (이래서 <= 사용)
    - push 하나 후 getMin: 그 값이 최솟값
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())   # -3
    ms.pop()
    print(ms.top())      # 0
    print(ms.getMin())   # -2

    # 중복 최솟값 케이스
    ms2 = MinStack()
    ms2.push(2)
    ms2.push(0)
    ms2.push(3)
    ms2.push(0)
    print(ms2.getMin())  # 0
    ms2.pop()
    print(ms2.getMin())  # 0  (중복이라 아직 0)
