"""
[0232] Implement Queue using Stacks (Easy)
https://leetcode.com/problems/implement-queue-using-stacks/

## 문제

스택 두 개만 사용하여 FIFO 큐를 구현하라.
다음 연산을 지원해야 한다:
  - push(x): 원소를 큐의 뒤에 추가
  - pop(): 큐의 앞 원소를 제거하고 반환
  - peek(): 큐의 앞 원소를 반환 (제거 없이)
  - empty(): 큐가 비어있으면 true, 아니면 false

## 예시

Example 1:
    Input:
        ["MyQueue","push","push","peek","pop","empty"]
        [[],[1],[2],[],[],[]]
    Output:
        [null,null,null,1,1,false]
    Explanation:
        MyQueue myQueue = new MyQueue();
        myQueue.push(1);
        myQueue.push(2);
        myQueue.peek();   → 1
        myQueue.pop();    → 1
        myQueue.empty();  → false

## 조건 (Constraints)

- 1 <= x <= 9
- push, pop, peek, empty 각각 최대 100번 호출된다.
- pop()과 peek()은 항상 유효한 큐에서만 호출된다.

## Follow-up

각 연산의 amortized 시간복잡도가 O(1)이 되도록 구현할 수 있는가?
"""


class MyQueue:

    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())    # Expected: 1
    print(q.pop())     # Expected: 1
    print(q.empty())   # Expected: False
    print(q.pop())     # Expected: 2
    print(q.empty())   # Expected: True
