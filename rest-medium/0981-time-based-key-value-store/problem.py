"""
[0981] Time Based Key-Value Store (Medium)
https://leetcode.com/problems/time-based-key-value-store/

## 문제

타임스탬프 기반의 key-value 저장 구조 `TimeMap`을 구현하라:
- `void set(String key, String value, int timestamp)`: 저장
- `String get(String key, int timestamp)`:
  - timestamp_prev <= timestamp인 set 호출 중 timestamp_prev가 가장 큰 것의 value 반환
  - 그런 값 없으면 ""

## 예시

Example 1:
    Input:
        ["TimeMap", "set", "get", "get", "set", "get", "get"]
        [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output:
        [null, null, "bar", "bar", null, "bar2", "bar2"]

## 조건 (Constraints)

- 1 <= key.length, value.length <= 100
- key, value는 소문자/숫자
- 1 <= timestamp <= 10^7
- 같은 key에 대한 set 호출은 timestamp가 strictly increasing
- set, get 합쳐서 최대 2 * 10^5번 호출
"""


class TimeMap:

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))   # "bar"
    print(tm.get("foo", 3))   # "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))   # "bar2"
    print(tm.get("foo", 5))   # "bar2"
