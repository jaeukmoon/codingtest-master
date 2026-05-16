"""
[0146] LRU Cache (Medium)
https://leetcode.com/problems/lru-cache/

## 문제

LRU(Least Recently Used) 캐시를 설계하라.

`LRUCache` 클래스를 구현:
- `LRUCache(int capacity)`: 양의 정수 용량으로 캐시 초기화
- `int get(int key)`: 키가 존재하면 값 반환, 없으면 -1 반환. 호출 시 해당 항목을 "최근 사용"으로 표시.
- `void put(int key, int value)`: 키가 존재하면 값 갱신, 없으면 새로 추가.
  추가 후 캐시 크기가 capacity를 초과하면 가장 오래 사용 안 한 항목을 제거.

`get`과 `put`은 모두 평균 O(1) 시간복잡도여야 한다.

## 예시

Example 1:
    Input:
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output:
        [null, null, null, 1, null, -1, null, -1, 3, 4]
    Explanation:
        LRUCache lru = new LRUCache(2);
        lru.put(1, 1);    // 캐시: {1=1}
        lru.put(2, 2);    // 캐시: {1=1, 2=2}
        lru.get(1);       // 1 반환, 1을 최근 사용으로 표시. LRU순: 2, 1
        lru.put(3, 3);    // 2 제거 (LRU). 캐시: {1=1, 3=3}
        lru.get(2);       // -1 (없음)
        lru.put(4, 4);    // 1 제거 (LRU). 캐시: {3=3, 4=4}
        lru.get(1);       // -1
        lru.get(3);       // 3
        lru.get(4);       // 4

## 조건

- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- get, put 합쳐서 최대 2 * 10^5번 호출
"""
# head <-> tail
# cache = {key: Node}

class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # head <-> tail
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # head <-> X <-> head.next
    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head # head <- node -> head.next
        self.head.next.prev = node
        self.head.next = node

    
    # Y <-> node <-> X
    
    def remove(self, node):
        node.prev.next = node.next # Y.next = X
        node.next.prev = node.prev # X.prev = Y

        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node) 
        self.add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        new_node = Node(key,value)
        self.cache[key] = new_node
        self.add_front(new_node)

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # Expected: 1
    lru.put(3, 3)        # 2 제거
    print(lru.get(2))    # Expected: -1
    lru.put(4, 4)        # 1 제거
    print(lru.get(1))    # Expected: -1
    print(lru.get(3))    # Expected: 3
    print(lru.get(4))    # Expected: 4
