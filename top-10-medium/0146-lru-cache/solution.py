"""
[0146] LRU Cache — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **get/put 모두 O(1)이 강제 요구사항** — 문제에 박혀 있음. 이게 자료구조 선택을 결정.
- **capacity는 항상 양수?** 네 (1 이상).
- **thread-safe?** 보통 단일 스레드 가정. 멀티 스레드면 락이 필요하다는 점 언급할 수 있음.
- **put(같은 key)는 LRU 갱신도 같이?** 네 — get/put 둘 다 "최근 사용"으로 마킹.

## 2. 자료구조 선택 — 왜 HashMap + Doubly Linked List 인가

### 요구사항 분해
- "최근 사용 항목 빠르게 갱신" → 양 끝에서 추가/제거 빠른 자료구조 필요 → Linked List.
- "특정 key를 O(1)에 찾기" → HashMap.
- "리스트 중간 노드를 O(1)에 제거" → **Doubly** Linked List (prev 포인터 없으면 O(n)).

### 둘을 합치면:
- HashMap: `key -> Node` (Node는 DLL 노드)
- DLL: head(most recent) ↔ ... ↔ tail(least recent)
- get(key): 해시맵에서 노드 찾기 → DLL에서 떼서 head로 옮기기 → 값 반환.
- put(key, val):
  - 존재: 값 갱신 후 head로.
  - 미존재: 새 노드 생성, head에 추가, 해시맵에 등록.
    크기 초과 시: tail.prev 제거 + 해시맵에서도 삭제.

### Sentinel(dummy) head/tail 사용
- 빈 리스트, 단일 노드 등의 경계 케이스에서 if/else 분기를 없애줌.
- head.next가 실제 most-recent, tail.prev가 실제 least-recent.

### Python의 OrderedDict로도 가능
- `move_to_end`, `popitem(last=False)`가 정확히 LRU 동작.
- 실무 코드는 OrderedDict가 깔끔. 다만 면접에서 "직접 구현해 보세요"라고 요구하는 경우가 많음.
- 두 가지 다 알면 좋음. 여기선 직접 구현으로 작성.

## 3. 엣지 케이스

- capacity=1 (가장 작음) — eviction이 매번 발생
- 같은 key를 여러 번 put — 사이즈 증가하면 안 됨
- get(없는 key) → -1
- put 직후 같은 key get → 방금 값
- capacity 도달 후 기존 key를 put → eviction 발생하면 안 됨 (사이즈 그대로)

## 4. 복잡도

- get/put: O(1) — 해시맵 O(1) + DLL 포인터 수술 O(1)
- 공간: O(capacity)
"""


class _Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev: "_Node | None" = None
        self.next: "_Node | None" = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, _Node] = {}
        # sentinel head/tail로 경계 분기 제거
        self.head = _Node()   # head.next = most recently used
        self.tail = _Node()   # tail.prev = least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- DLL 헬퍼 (모두 O(1)) ---
    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: _Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    # --- API ---
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)   # 최근 사용으로 갱신
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._move_to_front(node)
            return

        node = _Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        if len(self.map) > self.capacity:
            # LRU 제거: tail 직전 노드
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


if __name__ == "__main__":
    # === 흐름 추적 (capacity=2) ===
    lru = LRUCache(2)
    # DLL: head ↔ tail (빈 상태)

    lru.put(1, 1)
    # DLL: head ↔ [1:1] ↔ tail
    # map: {1: Node(1,1)}

    lru.put(2, 2)
    # DLL: head ↔ [2:2] ↔ [1:1] ↔ tail  (2가 최신 → front)
    # map: {1: Node(1,1), 2: Node(2,2)}

    print(lru.get(1))    # 1 → [1:1]을 front로 이동
    # DLL: head ↔ [1:1] ↔ [2:2] ↔ tail

    lru.put(3, 3)         # capacity 초과! → tail.prev = [2:2] 제거 (LRU)
    # DLL: head ↔ [3:3] ↔ [1:1] ↔ tail
    # map: {1: Node(1,1), 3: Node(3,3)}  (2 삭제됨)

    print(lru.get(2))    # -1 (이미 evict됨)

    lru.put(4, 4)         # capacity 초과! → tail.prev = [1:1] 제거 (LRU)
    # DLL: head ↔ [4:4] ↔ [3:3] ↔ tail
    # map: {3: Node(3,3), 4: Node(4,4)}

    print(lru.get(1))    # -1 (이미 evict됨)
    print(lru.get(3))    # 3
    print(lru.get(4))    # 4

    # 같은 key put — 사이즈 증가 X
    lru2 = LRUCache(2)
    lru2.put(1, 1)
    lru2.put(1, 10)
    print(lru2.get(1))   # 10
