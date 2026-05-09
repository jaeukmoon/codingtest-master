"""
[0933] Number of Recent Calls (Easy)
https://leetcode.com/problems/number-of-recent-calls/

## 문제

`RecentCounter` 클래스를 구현하라.
  - RecentCounter(): 카운터를 초기화한다.
  - ping(t): 시각 t(ms)에 ping을 추가하고, [t - 3000, t] 범위 내 ping 수를 반환한다.
    (t는 항상 이전 ping보다 크다)

## 예시

Example 1:
    Input:
        ["RecentCounter","ping","ping","ping","ping"]
        [[],[1],[100],[3001],[3002]]
    Output:
        [null,1,2,3,3]
    Explanation:
        RecentCounter recentCounter = new RecentCounter();
        recentCounter.ping(1);     → 1  ([1,1] 범위: 1개)
        recentCounter.ping(100);   → 2  ([-2900,100] 범위: 1, 100 → 2개)
        recentCounter.ping(3001);  → 3  ([1,3001] 범위: 1, 100, 3001 → 3개)
        recentCounter.ping(3002);  → 3  ([2,3002] 범위: 100, 3001, 3002 → 3개)

## 조건 (Constraints)

- 1 <= t <= 10^9
- 각 ping() 호출 시 t는 이전 호출보다 항상 크다 (strictly increasing).
- ping()은 최대 10^4번 호출된다.
"""

from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.count = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        self.count.append(t)
        while self.count[0]< t-3000:
            self.count.popleft()
        return len(self.count)


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))     # Expected: 1
    print(rc.ping(100))   # Expected: 2
    print(rc.ping(3001))  # Expected: 3
    print(rc.ping(3002))  # Expected: 3
