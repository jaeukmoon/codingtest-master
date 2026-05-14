"""
[0146] LRU Cache (Medium)
링크: https://leetcode.com/problems/lru-cache/

## 문제

LRU 캐시: get/put 모두 O(1). capacity 초과 시 가장 오래 안 쓴 항목 제거.

## 예시

Example: capacity=2, put(1,1), put(2,2), get(1)→1, put(3,3)는 2를 제거(LRU)

## 조건

- 1 <= capacity <= 3000
- get/put 합쳐서 최대 2*10^5번 호출

---

핵심 아이디어 (Hash Map + Doubly Linked List):
    - Hash Map: key → Node (O(1) 조회)
    - Doubly Linked List: 노드들을 사용 순서대로 정렬 (앞 = 최근, 뒤 = 오래됨)
    - Dummy head/tail 노드로 경계 처리 단순화

    각 연산:
    - get: dict에서 노드 찾기 → DLL에서 떼서 맨 앞으로 이동 → 값 반환
    - put 신규: 노드 만들어 dict에 등록, DLL 맨 앞에 추가. capacity 초과면 tail 직전 노드 제거
    - put 기존: 노드 값 갱신, 맨 앞으로 이동

    DLL이 필요한 이유: 단순 List는 임의 위치 삭제가 O(n). DLL은 prev 포인터 덕에 O(1).

자료구조 / 패턴:
    - Hash Map + Doubly Linked List (OOP Design 정석)

시간복잡도: get O(1), put O(1)
공간복잡도: O(capacity)

영어 멘트 (면접용):
    "I combine a hash map and a doubly linked list. The hash map gives O(1) lookup
     by key. The DLL maintains usage order — front is most recent, back is least.
     On every access, I unlink the node and move it to the front. Dummy head/tail
     nodes simplify edge cases. When capacity is exceeded, I evict the node before
     tail."

엣지 케이스:
    - 기존 키 put: 값 갱신 + 최근으로 이동 (capacity 체크 안 함)
    - capacity == 1: 매번 evict
    - get 없는 키: -1, DLL 변동 없음

## 손 추적 (Hand Trace) — capacity = 2
# 표기: head ⇄ [노드] ⇄ ... ⇄ tail   (head=가장 최근 쪽, tail=가장 오래된 쪽)
#       ⇄는 prev/next 양방향 포인터. (key:val) 형식.
#
# 초기:
#   dict = {}
#   head ⇄ tail
#
# ─────────────────────────────────────────────────────────────
# put(1, 1):  새 노드 추가
#   dict = {1: N1}
#   head ⇄ (1:1) ⇄ tail
#
# ─────────────────────────────────────────────────────────────
# put(2, 2):  새 노드 추가, head 쪽에
#   dict = {1: N1, 2: N2}
#   head ⇄ (2:2) ⇄ (1:1) ⇄ tail
#         ^ 최근                    ^ 오래됨
#
# ─────────────────────────────────────────────────────────────
# get(1) → 1:  N1을 head 쪽으로 이동
#   dict = {1: N1, 2: N2}  (그대로)
#   head ⇄ (1:1) ⇄ (2:2) ⇄ tail
#         ^ 방금 사용
#
# ─────────────────────────────────────────────────────────────
# put(3, 3):  capacity=2 초과 → tail 직전(2:2) 제거
#   dict = {1: N1, 3: N3}  (2 제거)
#   head ⇄ (3:3) ⇄ (1:1) ⇄ tail
#         ^ 새로 추가          ^ 2가 있던 자리
#
# ─────────────────────────────────────────────────────────────
# get(2) → -1:  dict에 2 없음, DLL 변동 없음
#   head ⇄ (3:3) ⇄ (1:1) ⇄ tail
#
# ─────────────────────────────────────────────────────────────
# put(4, 4):  capacity 초과 → tail 직전(1:1) 제거
#   dict = {3: N3, 4: N4}
#   head ⇄ (4:4) ⇄ (3:3) ⇄ tail
#
# ─────────────────────────────────────────────────────────────
# get(1) → -1:  dict에 1 없음
#
# ─────────────────────────────────────────────────────────────
# get(3) → 3:  N3을 head 쪽으로 이동
#   head ⇄ (3:3) ⇄ (4:4) ⇄ tail
#
# ─────────────────────────────────────────────────────────────
# get(4) → 4:  N4를 head 쪽으로 이동
#   head ⇄ (4:4) ⇄ (3:3) ⇄ tail
#
# 한 줄 요약:
#   head 쪽 = "최근 사용" (touch될 때마다 여기로 이동)
#   tail 쪽 = "오래됨"  (capacity 넘으면 여기서 제거)
#   dummy head/tail 덕에 "맨 앞 / 맨 끝" 경계 처리 if문 없음

## 대안 — OrderedDict로 풀기 (Pythonic, 면접 후 언급용)
# from collections import OrderedDict
# class LRUCache:
#     def __init__(self, capacity):
#         self.cap = capacity
#         self.cache = OrderedDict()
#     def get(self, key):
#         if key not in self.cache: return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.cap:
#             self.cache.popitem(last=False)
#
# OrderedDict가 내부적으로 DLL을 들고 있어서 본질은 같음. 면접에선 직접 DLL 구현이
# 더 점수가 높지만, "Python에선 OrderedDict로도 가능하다"고 한 마디 첨언하면 좋음.
"""


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                  # key → Node
        # Dummy head/tail로 경계 처리 단순화
        self.head = Node()               # 가장 최근 쪽
        self.tail = Node()               # 가장 오래된 쪽
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """DLL에서 노드 떼기"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        """DLL 맨 앞(head 바로 뒤)에 노드 삽입"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)         # 최근 사용으로 갱신
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 기존 키: 노드 제거 후 새로 만들어 다시 넣기 (값 갱신 + 위치 갱신)
            old_node = self.cache[key]
            self._remove(old_node)

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        if len(self.cache) > self.cap:
            # tail 바로 앞 노드가 LRU → 제거
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # 1
    lru.put(3, 3)        # 2 제거
    print(lru.get(2))    # -1
    lru.put(4, 4)        # 1 제거
    print(lru.get(1))    # -1
    print(lru.get(3))    # 3
    print(lru.get(4))    # 4
