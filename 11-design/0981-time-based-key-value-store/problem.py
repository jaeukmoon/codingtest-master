"""
[0981] Time Based Key-Value Store (Medium)
https://leetcode.com/problems/time-based-key-value-store/

## 문제

타임스탬프 기반 key-value 저장소를 설계하라.

`TimeMap` 클래스:
- `TimeMap()`: 객체 초기화
- `void set(String key, String value, int timestamp)`: timestamp에 value를 key에 저장
- `String get(String key, int timestamp)`:
    - timestamp_prev <= timestamp인 set 호출 중 **가장 큰 timestamp_prev**의 value 반환
    - 그런 호출이 없으면 빈 문자열 ""

`set`은 timestamp가 항상 증가하는 순서로 호출된다 (같은 key든 다른 key든).

## 예시

Example 1:
    Input:
        ["TimeMap","set","get","get","set","get","get"]
        [[], ["foo","bar",1], ["foo",1], ["foo",3], ["foo","bar2",4], ["foo",4], ["foo",5]]
    Output:
        [null, null, "bar", "bar", null, "bar2", "bar2"]
    Explanation:
        TimeMap timeMap = new TimeMap();
        timeMap.set("foo","bar",1);   // ("foo","bar")를 t=1에 저장
        timeMap.get("foo",1);          // "bar" (t=1에 set됨)
        timeMap.get("foo",3);          // "bar" (t<=3 중 최대인 t=1의 값)
        timeMap.set("foo","bar2",4);   // ("foo","bar2")를 t=4에 저장
        timeMap.get("foo",4);          // "bar2"
        timeMap.get("foo",5);          // "bar2" (t<=5 중 최대인 t=4)

## 조건

- 1 <= key.length, value.length <= 100
- key, value는 소문자/숫자/'-' 만 포함
- 1 <= timestamp <= 10^7
- set은 timestamp 오름차순으로 호출됨 (strictly increasing)
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
    print(tm.get("foo", 1))    # "bar"
    print(tm.get("foo", 3))    # "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))    # "bar2"
    print(tm.get("foo", 5))    # "bar2"

    # 없는 key
    tm2 = TimeMap()
    print(tm2.get("none", 1))  # ""

    # timestamp가 첫 set보다 작은 경우
    tm3 = TimeMap()
    tm3.set("a", "x", 5)
    print(tm3.get("a", 3))     # ""
