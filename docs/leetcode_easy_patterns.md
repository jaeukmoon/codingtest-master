# LeetCode Easy 패턴별 정리 — 1주차 폭 우선 학습용
# Hash Map/Set + Two Pointers + Sliding Window + Stack + Queue
# 회사에서 보고 집에서 손으로 짜는 용도

---

## 학습 목표

이번 주는 **모든 핵심 패턴의 Easy를 한 번씩 훑고 손에 박는 것**이 목표. 다음 주에 Medium 응용으로 넘어감.

총 13문제. 하루 1~2시간이면 끝나는 분량.

각 문제마다:
1. 풀이 안 보고 30분 시도
2. 막히면 풀이 보고 따라 짜기
3. 풀이 닫고 처음부터 다시
4. 다음 날 한 번 더 짜기

---

## 1. Two Sum (LeetCode 1)

### 문제

정수 배열 `nums`와 정수 `target`이 주어졌을 때, 합이 `target`이 되는 두 수의 **인덱스**를 반환.

### 예시

```
입력: nums = [2, 7, 11, 15], target = 9
출력: [0, 1]   (nums[0] + nums[1] = 2 + 7 = 9)
```

### 핵심 아이디어

dict에 "이미 본 값 → 인덱스"를 저장. 새 값이 들어올 때마다 "complement(target - 현재값)"이 dict에 있는지 확인.

### 풀이

```python
def twoSum(nums, target):
    seen = {}   # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### 왜 dict인가

이중 루프 O(n²)를 dict의 O(1) lookup으로 O(n)으로 떨어뜨림.

### 핵심 패턴

"한 번 순회하면서 이미 본 값을 dict에 저장하고, 매번 짝이 있는지 체크"

### 면접 멘트

"I'll use a hash map to store values I've seen along with their indices. For each number, I check if its complement (target - num) is already in the map. This gives O(n) time."

---

## 2. Contains Duplicate (LeetCode 217)

### 문제

배열에 중복된 원소가 있는지 확인.

### 예시

```
입력: nums = [1, 2, 3, 1]
출력: True

입력: nums = [1, 2, 3, 4]
출력: False
```

### 핵심 아이디어

set에 원소를 하나씩 추가하면서 이미 있으면 True 반환.

### 풀이 1: 명시적 (면접 추천)

```python
def containsDuplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
```

### 풀이 2: Pythonic (한 줄)

```python
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
```

### 왜 set인가

중복 체크는 set의 가장 기본 use case. `in` 연산이 O(1).

### 핵심 패턴

"이미 봤는지" 체크는 무조건 set

### 면접 멘트

"I'll use a set for O(1) duplicate detection. As I iterate through the array, I check if each element is already in the set. If so, I've found a duplicate."

---

## 3. Valid Anagram (LeetCode 242)

### 문제

두 문자열이 anagram(같은 글자로 구성된 단어)인지 확인.

### 예시

```
입력: s = "listen", t = "silent"
출력: True   (같은 글자 구성)

입력: s = "rat", t = "car"
출력: False
```

### 핵심 아이디어

각 문자의 빈도를 세서 비교. 빈도가 같으면 anagram.

### 풀이 1: dict 카운팅 (if-else)

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    counts = {}
    
    # s의 글자 카운트
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    
    # t의 글자로 카운트 차감
    for c in t:
        if c not in counts or counts[c] == 0:
            return False
        counts[c] -= 1
    
    return True
```

### 풀이 2: defaultdict 사용

```python
from collections import defaultdict

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1   # 키 없으면 자동 0부터 시작
    
    for c in t:
        if counts[c] == 0:
            return False
        counts[c] -= 1
    
    return True
```

### 풀이 3: Counter (Pythonic)

```python
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

### 면접 추천

풀이 1이나 2를 메인으로 짜고, 마지막에 "Counter로 한 줄 가능합니다"를 언급.

### 핵심 패턴

"글자 빈도 비교" → 카운팅 dict

### 시간복잡도

O(n)

---

## 4. Intersection of Two Arrays (LeetCode 349)

### 문제

두 배열의 교집합을 중복 없이 반환.

### 예시

```
입력: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
출력: [2]

입력: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
출력: [9, 4]   (또는 [4, 9])
```

### 핵심 아이디어

두 배열을 set으로 변환하고 교집합 연산.

### 풀이 1: 명시적 (면접 추천)

```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()
    
    for num in nums2:
        if num in set1:
            result.add(num)
    
    return list(result)
```

### 풀이 2: set 연산자 (Pythonic)

```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```

### 면접 추천

풀이 1을 짜고, 마지막에 "set 연산자로 한 줄도 가능합니다"를 언급.

### 핵심 패턴

"두 컬렉션의 공통 원소" → set 교집합

### 시간복잡도

O(n + m)

---

## 5. Valid Sudoku (LeetCode 36)

### 문제

9x9 스도쿠 보드가 유효한지 확인. 각 행, 각 열, 각 3x3 박스에 1~9가 중복 없이 들어가야 함. 빈 칸은 `'.'`로 표시.

### 핵심 아이디어

행, 열, 박스를 각각 set으로 관리. 보드를 한 번 순회하면서 세 set에 동시에 체크/추가.

### 풀이

```python
def isValidSudoku(board):
    rows = [set() for _ in range(9)]      # 9개 행 set
    cols = [set() for _ in range(9)]      # 9개 열 set
    boxes = [set() for _ in range(9)]     # 9개 3x3 박스 set
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            
            box_idx = (r // 3) * 3 + (c // 3)   # 박스 번호 계산
            
            # 셋 중 하나라도 이미 있으면 invalid
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            
            # 세 set에 모두 추가
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    
    return True
```

### 박스 번호 계산 트릭

```
box_idx = (r // 3) * 3 + (c // 3)

  c=0,1,2 │ c=3,4,5 │ c=6,7,8
─────────┼─────────┼─────────
   box 0 │  box 1  │  box 2     (r=0,1,2)
─────────┼─────────┼─────────
   box 3 │  box 4  │  box 5     (r=3,4,5)
─────────┼─────────┼─────────
   box 6 │  box 7  │  box 8     (r=6,7,8)

예: r=4, c=7 → (4//3)*3 + (7//3) = 1*3 + 2 = 5번 박스
```

### 핵심 패턴

"여러 제약 조건을 동시에 체크" → 여러 set을 병렬로 관리

### 시간복잡도

O(81) = O(1) (보드 크기 고정)

---

# 패턴 2: Two Pointers

## 핵심 개념

두 포인터를 양 끝 또는 같은 위치에서 시작해서 조건에 따라 이동시키는 패턴.

**언제 쓰나:**
- 정렬된 배열에서 두 수 찾기
- 팰린드롬 체크
- 배열 안에서 짝/조합 찾기

**왜 쓰나:** 이중 루프 O(n²)를 O(n)으로 줄임.

---

## 6. Valid Palindrome (LeetCode 125)

### 문제

문자열이 팰린드롬인지 확인 (영숫자만 고려, 대소문자 무시).

### 예시

```
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False
```

### 핵심 아이디어

양 끝에서 포인터 두 개. 안쪽으로 좁혀가며 비교. 영숫자 아닌 문자는 skip.

### 풀이

```python
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # 영숫자 아닌 문자 skip (왼쪽)
        while left < right and not s[left].isalnum():
            left += 1
        # 영숫자 아닌 문자 skip (오른쪽)
        while left < right and not s[right].isalnum():
            right -= 1
        
        # 비교 (대소문자 무시)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

### 자주 쓰는 메서드

- `s.isalnum()`: 영숫자(알파벳 + 숫자)인지 체크
- `s.lower()`: 소문자 변환

### 핵심 패턴

양 끝 포인터 → 안쪽으로 좁혀가기. 두 포인터가 만나면 종료.

---

## 7. Two Sum II - Input Array is Sorted (LeetCode 167)

### 문제

**정렬된** 배열에서 합이 target이 되는 두 수의 인덱스(1-indexed) 반환.

### 예시

```
입력: numbers = [2, 7, 11, 15], target = 9
출력: [1, 2]
```

### 핵심 아이디어

배열이 정렬되어 있다는 점이 핵심. 합이 작으면 left++, 크면 right--.

### 풀이

```python
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]   # 1-indexed
        elif current_sum < target:
            left += 1                       # 합 늘려야 함
        else:
            right -= 1                      # 합 줄여야 함
    
    return []
```

### Two Sum (1번)과의 차이

| | Two Sum (1) | Two Sum II (167) |
|---|---|---|
| 입력 | 정렬 안 됨 | **정렬됨** |
| 풀이 | dict 활용 | Two Pointers |
| 공간복잡도 | O(n) | **O(1)** |

### 핵심 패턴

정렬 + 양 끝 포인터. 조건에 따라 left/right 이동.

---

# 패턴 3: Sliding Window

## 핵심 개념

배열/문자열에서 "고정 또는 가변 크기 구간"을 슬라이딩하면서 처리.

**언제 쓰나:**
- "연속된 부분 배열/부분 문자열" 문제
- "최대/최소 길이의 substring 찾기"
- "최근 K개 평균"

**왜 쓰나:** 이중 루프 O(n²)를 O(n)으로 줄임.

---

## 8. Best Time to Buy and Sell Stock (LeetCode 121)

### 문제

각 날의 주가 배열. 하루 사고 다른 날 팔 때 최대 이익.

### 예시

```
입력: prices = [7, 1, 5, 3, 6, 4]
출력: 5   (1에 사서 6에 팔기)

입력: prices = [7, 6, 4, 3, 1]
출력: 0   (이익 못 봄, 0 반환)
```

### 핵심 아이디어

한 번 순회하면서 "지금까지의 최저가"와 "현재가에서 팔 때 이익"을 동시에 추적.

### 풀이

```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # 최저가 업데이트
        if price < min_price:
            min_price = price
        # 현재 팔 때 이익이 더 크면 업데이트
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit
```

### 핵심 패턴

한 번 순회하면서 "지금까지의 최선"과 "현재 답" 동시 추적.

---

## 9. Maximum Subarray (LeetCode 53)

### 문제

정수 배열에서 합이 가장 큰 연속 부분 배열의 합.

### 예시

```
입력: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
출력: 6   (부분 배열 [4, -1, 2, 1])
```

### 핵심 아이디어 (Kadane's Algorithm)

각 위치에서 "여기서 새로 시작" vs "이전부터 이어가기" 중 더 큰 쪽을 선택.

### 풀이

```python
def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        # 새로 시작 vs 이어가기
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### 핵심 패턴

"이 자리에서 새로 시작할지, 이어갈지" 매 자리에서 결정.

### 면접 단골

Kadane's Algorithm은 면접 자주 나옴. 알아두면 좋음.

---

# 패턴 4: Stack

## 핵심 개념

LIFO (Last In, First Out). 마지막에 넣은 게 먼저 나옴.

**언제 쓰나:**
- 괄호 매칭, 짝 맞추기
- "이전 상태를 저장해 둬야 할 때"
- 거꾸로 처리해야 할 때

**Python에서:** 그냥 `list` 사용. `append()` push, `pop()` pop, `[-1]` peek.

---

## 10. Valid Parentheses (LeetCode 20)

### 문제

괄호 문자열이 유효한지.

### 예시

```
입력: "()[]{}"
출력: True

입력: "(]"
출력: False

입력: "([{}])"
출력: True
```

### 핵심 아이디어

여는 괄호 → push. 닫는 괄호 → pop해서 매칭 확인.

### 풀이

```python
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for c in s:
        if c in '([{':                       # 여는 괄호
            stack.append(c)
        else:                                 # 닫는 괄호
            if not stack or stack.pop() != pairs[c]:
                return False
    
    return len(stack) == 0                   # 다 매칭됐으면 비어 있어야
```

### 엣지 케이스

- 빈 문자열: True
- `"]"`처럼 닫는 괄호로 시작: stack 비어서 False
- `"("`처럼 안 닫힌 채 끝: 마지막에 stack 안 비어서 False

### 핵심 패턴

여는 건 push, 닫는 건 pop + 비교.

---

## 11. Min Stack (LeetCode 155) — OOP 연습용

### 문제

push, pop, top, getMin을 모두 O(1)에 지원하는 스택 구현.

### 핵심 아이디어

스택 두 개 사용. 하나는 일반 스택, 하나는 "현재까지의 최솟값" 추적.

### 풀이

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        # 새 값이 현재 최솟값보다 작거나 같으면 push
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        val = self.stack.pop()
        # pop한 값이 현재 최솟값이었으면 min_stack에서도 pop
        if val == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
```

### 왜 `<=` 인가 (`<`가 아니라)

중복값 처리 때문. `[2, 0, 3, 0]` push 후 마지막 0을 pop했을 때, min_stack에 0이 한 번만 있으면 잘못된 최솟값 반환.

### 핵심 패턴

보조 자료구조로 추가 정보 추적. **OOP 설계 연습**.

### FDE 면접 중요

PDF가 OOP 강조했으니까 이 문제는 꼭 익혀두세요.

---

# 패턴 5: Queue

## 핵심 개념

FIFO (First In, First Out). 먼저 넣은 게 먼저 나옴.

**언제 쓰나:**
- BFS (Breadth-First Search)
- 순서대로 처리해야 할 때
- "최근 K개 요소" 관리

**Python에서:** `collections.deque` 사용. `list`로 queue 만들면 `pop(0)`이 **O(n)**이라 느림. 면접에서 이거 쓰면 감점.

```python
from collections import deque
q = deque()
q.append(x)        # enqueue, O(1)
q.popleft()        # dequeue, O(1)
```

---

## 12. Implement Queue using Stacks (LeetCode 232)

### 문제

Stack 두 개로 Queue 구현.

### 핵심 아이디어

push용 스택, pop용 스택 두 개. pop할 때 push 스택에서 pop 스택으로 옮기면 순서 뒤집어짐.

### 풀이

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []      # push용
        self.out_stack = []     # pop용
    
    def push(self, x):
        self.in_stack.append(x)
    
    def pop(self):
        self._move_if_needed()
        return self.out_stack.pop()
    
    def peek(self):
        self._move_if_needed()
        return self.out_stack[-1]
    
    def empty(self):
        return not self.in_stack and not self.out_stack
    
    def _move_if_needed(self):
        # out_stack이 비었을 때만 in_stack 내용 옮김
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```

### 핵심 패턴

두 자료구조로 다른 자료구조 흉내. **OOP 설계 연습**.

### FDE 면접 중요

OOP 설계 + 두 stack 활용. PDF에서 강조한 OOP 사고를 보여주기 좋은 문제.

---

## 13. Number of Recent Calls (LeetCode 933)

### 문제

`ping(t)` 호출 시, 최근 3000ms 내의 호출 개수 반환.

### 예시

```
RecentCounter()
ping(1)     → 1   (1ms 시점, 최근 3000ms 호출 1개)
ping(100)   → 2   (100ms 시점, 최근 3000ms 호출 2개)
ping(3001)  → 3   (3001ms 시점, 1~3001ms 호출 3개)
ping(3002)  → 3   (3002ms 시점, 1ms는 윈도우 밖이라 제거)
```

### 핵심 아이디어

deque로 시간 윈도우 관리. 3000ms 이전 호출은 popleft로 제거.

### 풀이

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
    
    def ping(self, t):
        self.q.append(t)
        # 3000ms 이전 호출들 제거
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```

### 왜 deque인가

양 끝 모두 O(1) 접근 필요. `list`는 `pop(0)`이 O(n)이라 부적합.

### 핵심 패턴

시간 윈도우를 deque로 관리. 윈도우 밖 원소는 popleft.

---

## 패턴 한눈 정리

| # | 문제 | 패턴 | 핵심 |
|---|------|------|------|
| 1 | Two Sum | Hash Map | value → index 매핑, complement 체크 |
| 2 | Contains Duplicate | Set | "이미 봤나" 체크 |
| 3 | Valid Anagram | Hash Map (Counter) | 글자 빈도 카운팅 |
| 4 | Intersection | Set | 두 set 교집합 |
| 5 | Valid Sudoku | Set 여러 개 | 여러 제약을 병렬 set으로 |
| 6 | Valid Palindrome | Two Pointers | 양 끝에서 안쪽으로 |
| 7 | Two Sum II | Two Pointers | 정렬 + 양 끝 포인터 |
| 8 | Best Time Buy Sell | Sliding Window | 최저가/최대 이익 동시 추적 |
| 9 | Maximum Subarray | Kadane (DP/SW) | 새로 시작 vs 이어가기 |
| 10 | Valid Parentheses | Stack | 여는 push, 닫는 pop+비교 |
| 11 | Min Stack | Stack (OOP) | 보조 스택으로 정보 추적 |
| 12 | Queue using Stacks | Stack/Queue (OOP) | 두 스택으로 FIFO 흉내 |
| 13 | Recent Counter | Queue (deque) | 시간 윈도우 관리 |

---

## 1주차 일정 (13문제)

| 요일 | 패턴 | 문제 | 분량 |
|-----|------|------|------|
| 월 | Hash Map/Set | Two Sum, Contains Duplicate, Valid Anagram | 3개 |
| 화 | Hash Map/Set | Intersection, Valid Sudoku | 2개 |
| 수 | Two Pointers | Valid Palindrome, Two Sum II | 2개 |
| 목 | Sliding Window | Best Time Buy Sell, Maximum Subarray | 2개 |
| 금 | Stack | Valid Parentheses, Min Stack | 2개 |
| 토 | Queue | Queue using Stacks, Recent Counter | 2개 |
| 일 | 복습 | 못 풀거나 헷갈리는 문제 다시 짜기 | 자유 |

하루 1~2시간이면 끝남. 무리 없는 페이스.

---

## 자주 쓰는 dict/set 메서드 빠른 참조

### dict
```python
d = {}
d[key] = value           # 추가/수정
if key in d:             # 존재 체크 O(1)
del d[key]               # 삭제
d.get(key, default)      # 안전한 조회
d.items() / .keys() / .values()  # 순회

# defaultdict
from collections import defaultdict
d = defaultdict(int)     # 기본값 0
d = defaultdict(list)    # 기본값 []

# Counter
from collections import Counter
c = Counter("abcabc")    # {'a':2, 'b':2, 'c':2}
c.most_common(2)         # 상위 2개
```

### set
```python
s = set()
s.add(x)                 # 추가
x in s                   # 존재 체크 O(1)
s.remove(x)              # 삭제 (없으면 에러)
s.discard(x)             # 안전한 삭제

# 집합 연산
a | b                    # 합집합
a & b                    # 교집합
a - b                    # 차집합
```

---

## 손으로 짜는 순서 추천

### 1차: 막혀도 직접 시도

5문제 각각 30분 안에 직접 짜보기. 막히면 풀이 안 보고 끙끙대기.

### 2차: 풀이 보고 따라 짜기

30분 넘어가도 안 풀리면 풀이 보고 그대로 짜기. 그다음 풀이 닫고 처음부터 다시.

### 3차: 다음 날 다시 짜기

같은 문제를 다음 날 다시 짜면 손에 박힘. 박사 과정에서 모델 구현할 때 했던 그 방식.

---

## 면접 사고 프로세스 (모든 문제 공통)

1. **명확화 질문**: 입력 범위, 엣지 케이스 (빈 입력, 음수, 중복 등)
2. **Brute Force 언급**: "First, brute force would be O(n²)..." 짧게
3. **최적화 아이디어**: "We can use a hash map for O(1) lookup..."
4. **코드 작성**: 명확한 변수명, 깔끔한 구조
5. **테스트**: 정상 케이스 + 엣지 케이스 한두 개

---

## 마무리

이 5문제 손에 박히면 dict + set 패턴은 끝. 다음은 Two Pointer, Sliding Window 단계로 넘어가면 됩니다.

화이팅.
