"""
[0232] Implement Queue using Stacks (Easy)
링크: https://leetcode.com/problems/implement-queue-using-stacks/

문제:
    Stack 두 개만 써서 Queue(FIFO) 구현.
    push, pop, peek, empty 지원.

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
