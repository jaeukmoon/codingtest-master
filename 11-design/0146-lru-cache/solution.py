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
    """DLL의 노드. dict의 value와 DLL의 원소를 겸함 (같은 객체를 양쪽이 참조).

    왜 Node 클래스가 필요한가:
      1) DLL을 만들려면 prev/next 포인터를 매달 객체가 필요. (int만 들면 순서 추적 불가)
      2) key를 함께 저장해야 evict 시 dict에서 O(1)로 지울 수 있음.
         - evict 절차: tail.prev로 LRU 노드 발견 → DLL에서 떼기 → dict에서도 삭제
         - dict 삭제에 'key'가 필요 → 노드 안에 key를 들고 있어야 lru.key 한 번에 가능
         - key 없으면 "이 노드가 어느 key인지" 찾으려고 dict 전체 순회 O(N)이 됨.
      3) 같은 Node 객체가 cache[key]의 value이자 DLL의 원소 → 한 곳만 옮기면 됨.
    """
    def __init__(self, key=0, val=0):
        self.key = key                    # evict 시 dict[key] 삭제에 사용
        self.val = val                    # get이 반환할 실제 값
        self.prev = None                  # DLL 앞 노드 (head 방향)
        self.next = None                  # DLL 뒤 노드 (tail 방향)


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                  # key → Node (O(1) 노드 위치 조회)

        # Dummy head/tail: 실제 데이터가 없는 경계 노드.
        # 덕분에 "맨 앞/맨 뒤 삽입·삭제" 시 prev/next가 None인 경우를 따로 처리할 필요 없음.
        # 모든 실제 노드는 head와 tail '사이'에만 존재.
        self.head = Node()               # head.next = 가장 최근에 쓴 노드
        self.tail = Node()               # tail.prev = 가장 오래된 노드 (LRU)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """DLL에서 node를 떼어낸다. O(1).

        node의 참조를 이미 들고 있고, DLL이라 prev도 즉시 알 수 있어서 포인터 2개만 수술.
            ... ⇄ A ⇄ node ⇄ C ⇄ ...    →    ... ⇄ A ⇄ C ⇄ ...
        """
        node.prev.next = node.next       # A.next = C
        node.next.prev = node.prev       # C.prev = A
        # node의 prev/next는 굳이 None으로 안 만들어도 됨 (어차피 참조 끊겨 GC됨)

    def _add_to_front(self, node):
        """node를 head 바로 뒤(가장 최근 자리)에 삽입. O(1).

        삽입 전:  head ⇄ X ⇄ ...           (X = head.next, 기존 최근)
        삽입 후:  head ⇄ node ⇄ X ⇄ ...
        """
        node.next = self.head.next       # node → X
        node.prev = self.head            # head ← node
        self.head.next.prev = node       # X.prev = node
        self.head.next = node            # head.next = node
        # 순서 주의: head.next를 갱신하기 전에 'X.prev = node'를 먼저 해야 X 참조를 잃지 않음.

    def get(self, key: int) -> int:
        # 1) dict로 노드 참조를 O(1)에 획득 (없으면 -1)
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 2) "방금 썼다" → DLL에서 떼서 맨 앞으로 이동 (O(1) + O(1))
        self._remove(node)
        self._add_to_front(node)
        # dict는 건드릴 필요 없음: cache[key]는 여전히 같은 node 객체를 가리킴.
        return node.val

    def put(self, key: int, value: int) -> None:
        # 기존 키면 먼저 떼어낸다 (위치 갱신 + 값 갱신을 위해 새 노드로 교체).
        # 새 노드를 만드는 대신 node.val만 바꾸고 _move_to_front 해도 동작은 같음 — 취향 차이.
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
            # 주의: dict에서 지우지 않음. 바로 아래에서 같은 key로 덮어쓸 거라 불필요.
            # (만약 지웠다가 다시 넣으면 dict 두 번 만지는 셈)

        new_node = Node(key, value)
        self.cache[key] = new_node       # dict 등록
        self._add_to_front(new_node)     # DLL 맨 앞에 삽입 (= "방금 썼다")

        # 용량 초과 시 LRU evict.
        # 기존 키 갱신 경로에선 len이 늘지 않아 이 분기를 안 탐 → if 하나로 충분.
        if len(self.cache) > self.cap:
            lru = self.tail.prev         # tail 바로 앞 = 가장 오래된 노드
            self._remove(lru)            # DLL에서 제거
            del self.cache[lru.key]      # ← 여기서 lru.key가 필요 (Node가 key를 들고 있는 이유)


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
