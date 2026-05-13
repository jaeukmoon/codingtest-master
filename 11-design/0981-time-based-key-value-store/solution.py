"""
[0981] Time Based Key-Value Store (Medium)
링크: https://leetcode.com/problems/time-based-key-value-store/

## 문제

set(key, value, timestamp): 저장
get(key, timestamp): timestamp_prev <= timestamp 중 최대 timestamp_prev의 value 반환,
                     없으면 ""

조건: set 호출 시 timestamp는 항상 증가.

## 예시

Example: set("foo","bar",1), set("foo","bar2",4)
  get("foo",3) → "bar"
  get("foo",4) → "bar2"
  get("foo",5) → "bar2"

## 조건

- 1 <= timestamp <= 10^7
- set은 timestamp 오름차순으로 호출
- 최대 2*10^5번 호출

---

핵심 아이디어 (Dict + Binary Search):
    - dict<key, list>: 각 key마다 (timestamp, value) 쌍의 리스트를 들고 있음
    - set이 timestamp 오름차순 → list가 자동으로 timestamp 기준 정렬됨 (append만 함)
    - get(key, t): 그 key의 list에서 "timestamp <= t인 가장 큰 timestamp" 찾기
      → **Binary Search (경계 탐색, 정확히 Search Insert Position 패턴)**

자료구조 / 패턴:
    - Hash Map + Binary Search (경계 탐색)
    - 답 공간 binary search의 친척: "조건 만족하는 마지막 위치"

시간복잡도: set O(1), get O(log n)
공간복잡도: O(전체 set 호출 수)

영어 멘트 (면접용):
    "I store each key's history as a sorted list of (timestamp, value), exploiting
     the fact that set is called in increasing order. For get, I binary search the
     list for the largest timestamp ≤ query — this is the canonical 'rightmost
     ≤ target' binary search. O(log n) per get."

엣지 케이스:
    - key가 dict에 없음 → ""
    - 첫 timestamp가 query보다 큼 → ""
    - 정확히 일치하는 timestamp 있음 → 그 value

## 손 추적 (Hand Trace)
# 호출: set("foo","bar",1), set("foo","bar2",4), get("foo", 3), get("foo", 5)
#
# set("foo","bar",1):  store["foo"] = [(1,"bar")]
# set("foo","bar2",4): store["foo"] = [(1,"bar"), (4,"bar2")]
#
# get("foo", 3):
#   list = [(1,"bar"), (4,"bar2")]
#   목표: timestamp <= 3인 마지막 인덱스
#
#   Binary search (lo=0, hi=len=2, 반열린 구간):
#     - lo=0, hi=2, mid=1, list[1].ts=4 > 3 → hi=1
#     - lo=0, hi=1, mid=0, list[0].ts=1 <= 3 → lo=1
#     - lo==hi → 종료, lo=1
#   답 인덱스 = lo - 1 = 0 → list[0] = (1,"bar") → return "bar"
#
# get("foo", 5):
#   list = [(1,"bar"), (4,"bar2")]
#   - lo=0, hi=2, mid=1, ts=4 <= 5 → lo=2
#   - lo==hi → lo=2
#   답 인덱스 = lo - 1 = 1 → "bar2"
#
# 패턴: bisect_right로 "내가 들어갈 자리" 찾고 -1 하면 "이하 중 최대" 인덱스.
"""
from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        # key → list of (timestamp, value), timestamp 오름차순
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # set이 timestamp 오름차순으로 호출된다는 조건 → 그냥 append
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        # arr에서 timestamp 이하 중 가장 큰 timestamp의 인덱스 찾기
        # bisect_right((timestamp, "")): timestamp 초과인 첫 인덱스 반환
        # → 그 인덱스 - 1이 답
        idx = bisect.bisect_right(arr, (timestamp, chr(127)))

        if idx == 0:
            return ""    # timestamp 이하인 원소가 없음
        return arr[idx - 1][1]


# bisect 안 쓰고 직접 binary search 버전 (대안 — 면접 후 언급용)
# class TimeMap:
#     def __init__(self):
#         self.store = defaultdict(list)
#
#     def set(self, key, value, timestamp):
#         self.store[key].append((timestamp, value))
#
#     def get(self, key, timestamp):
#         if key not in self.store: return ""
#         arr = self.store[key]
#         lo, hi = 0, len(arr)
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if arr[mid][0] <= timestamp:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         if lo == 0: return ""
#         return arr[lo - 1][1]


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))    # "bar"
    print(tm.get("foo", 3))    # "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))    # "bar2"
    print(tm.get("foo", 5))    # "bar2"

    tm2 = TimeMap()
    print(tm2.get("none", 1))  # ""

    tm3 = TimeMap()
    tm3.set("a", "x", 5)
    print(tm3.get("a", 3))     # ""
