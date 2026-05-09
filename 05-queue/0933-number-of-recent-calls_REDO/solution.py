"""
[0933] Number of Recent Calls (Easy)
링크: https://leetcode.com/problems/number-of-recent-calls/

## 문제

`ping(t)` 호출 시, [t - 3000, t] 범위 내의 ping 수를 반환하라.
t는 항상 이전 ping보다 크다 (strictly increasing).

## 예시

    ping(1)    → 1
    ping(100)  → 2
    ping(3001) → 3
    ping(3002) → 3  (1ms는 범위 [2, 3002] 밖)

## 조건

- 1 <= t <= 10^9, strictly increasing
- ping()은 최대 10^4번 호출된다.

---

핵심 아이디어:
    deque로 시간 윈도우 관리. 새 ping 추가 후, 윈도우 밖(t - 3000 이전) 원소는
    popleft로 제거. 남은 길이가 곧 개수.

자료구조 / 패턴:
    - deque (슬라이딩 윈도우 + 양 끝 O(1) 연산)

시간복잡도: O(1) amortized (각 원소는 최대 1번 push, 1번 pop)
공간복잡도: O(3000) = O(1) (윈도우 최대 크기 고정)

영어 멘트 (면접용):
    "I use a deque as a sliding window. On each ping, I add the timestamp and remove
     any timestamps older than t - 3000 from the front. The deque length is the answer.
     deque is chosen over list because popleft is O(1) vs O(n) for list."

엣지 케이스:
    - 연속 호출 없이 3000ms 이상 지나면 이전 ping 모두 제거
    - ping(1) → 1, ping(100) → 2, ping(3001) → 3, ping(3002) → 3
"""
from collections import deque


## 손 추적 (Hand Trace)
# ping(1), ping(100), ping(3001), ping(3002)
#
#  t    | append 후 q      | 제거 조건(q[0] < t-3000) | 제거 후 q    | len
# ------|------------------|--------------------------|-------------|----
#  1    | [1]              | q[0]=1 < -2999? NO       | [1]         |  1
#  100  | [1,100]          | q[0]=1 < -2900? NO       | [1,100]     |  2
#  3001 | [1,100,3001]     | q[0]=1 < 1? NO           | [1,100,3001]|  3
#  3002 | [1,100,3001,3002]| q[0]=1 < 2? YES→popleft  | [100,3001,3002]| 3
#       |                  | q[0]=100 < 2? NO  → stop |             |


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))     # 1
    print(rc.ping(100))   # 2
    print(rc.ping(3001))  # 3
    print(rc.ping(3002))  # 3
