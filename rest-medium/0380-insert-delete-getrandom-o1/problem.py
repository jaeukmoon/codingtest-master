"""
[0380] Insert Delete GetRandom O(1) (Medium)
https://leetcode.com/problems/insert-delete-getrandom-o1/

## 문제

다음 연산을 모두 **평균 O(1)**에 지원하는 데이터 구조 `RandomizedSet`을 구현하라:
- `bool insert(int val)`: val이 없으면 추가하고 true, 있으면 false
- `bool remove(int val)`: val이 있으면 제거하고 true, 없으면 false
- `int getRandom()`: 현재 원소 중 무작위로 하나 반환 (균등 확률)

## 예시

Example 1:
    Input:
        ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
        [[],[1],[2],[2],[],[1],[2],[]]
    Output:
        [null,true,false,true,2,true,false,2]

## 조건 (Constraints)

- -2^31 <= val <= 2^31 - 1
- insert, remove, getRandom 합쳐서 최대 2 * 10^5번 호출
- getRandom은 적어도 한 원소가 있을 때만 호출됨
"""


class RandomizedSet:

    def __init__(self):
        pass

    def insert(self, val: int) -> bool:
        pass

    def remove(self, val: int) -> bool:
        pass

    def getRandom(self) -> int:
        pass


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))    # True
    print(rs.remove(2))    # False
    print(rs.insert(2))    # True
    print(rs.getRandom())  # 1 또는 2
    print(rs.remove(1))    # True
    print(rs.insert(2))    # False
    print(rs.getRandom())  # 2
