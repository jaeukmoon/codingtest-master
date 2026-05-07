"""
[0933] Number of Recent Calls (Easy)
링크: https://leetcode.com/problems/number-of-recent-calls/

문제:
    ping(t) 호출 시, 최근 3000ms 내의 ping 개수 반환.
    (범위: [t - 3000, t])

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
