"""
[0232] Implement Queue using Stacks (Easy)
링크: https://leetcode.com/problems/implement-queue-using-stacks/

## 문제

스택 두 개만 사용하여 FIFO 큐를 구현하라.
push(x), pop(), peek(), empty() 지원.

## 예시

    MyQueue q = new MyQueue();
    q.push(1); q.push(2);
    q.peek()  → 1
    q.pop()   → 1
    q.empty() → false

## 조건

- 1 <= x <= 9
- push, pop, peek, empty 각각 최대 100번 호출된다.
- pop()과 peek()은 항상 유효한 큐에서만 호출된다.

---

핵심 아이디어:
    in_stack(push용) + out_stack(pop용). out_stack이 비었을 때만 in_stack 전체를
    옮김 → 순서가 뒤집혀서 FIFO 구현됨. 이미 out_stack에 원소 있으면 그냥 씀.

자료구조 / 패턴:
    - Stack 두 개로 Queue 흉내 / OOP 설계

시간복잡도: push O(1), pop amortized O(1)
공간복잡도: O(n)

영어 멘트 (면접용):
    "I use two stacks: one for push, one for pop. When the pop stack is empty,
     I transfer all elements from push stack — this reverses the order, giving FIFO.
     Each element is moved at most once, so pop is amortized O(1)."

엣지 케이스:
    - pop할 때 out_stack 비어있고 in_stack에도 없으면 에러 (문제에서 valid ops 보장)
    - push 여러 번 후 pop: 먼저 push한 게 먼저 나와야 함
"""


## 손 추적 (Hand Trace)
# push(1), push(2), peek, pop, pop
#
#  op      | in_stack | out_stack | 반환
# ---------|----------|-----------|------
#  push(1) | [1]      | []        |
#  push(2) | [1,2]    | []        |
#  peek()  | []       | [2,1]     | 1   ← out 비어서 이동: [1,2]→pop→[2,1]
#  pop()   | []       | [2]       | 1   ← out에서 pop
#  pop()   | []       | []        | 2   ← out에서 pop
#
# 핵심: out_stack이 비었을 때만 이동 (이미 있으면 그냥 씀)
# push(3) 후 pop() → out 비었으므로 이동: in[3]→out[3] → pop→3


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self._move_if_needed()
        return self.out_stack.pop()

    def peek(self):
        self._move_if_needed()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def _move_if_needed(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())    # 1
    print(q.pop())     # 1
    print(q.empty())   # False
    print(q.pop())     # 2
    print(q.empty())   # True
