# LeetCode Interview Prep

Google FDE 면접 준비를 위한 LeetCode 풀이 정리.

## 진척도

- [x] Week 1: Easy 패턴별 마스터 (13/13)
- [ ] Week 2: Medium 응용 + OOP Design + Mock Interview

## 패턴별 인덱스

### 1. Hash Map / Set (5)
- [x] [0001. Two Sum](./01-hash-map-set/0001-two-sum.py)
- [x] [0217. Contains Duplicate](./01-hash-map-set/0217-contains-duplicate.py)
- [x] [0242. Valid Anagram](./01-hash-map-set/0242-valid-anagram_REVIEW)
- [x] [0349. Intersection of Two Arrays](./01-hash-map-set/0349-intersection-of-two-arrays.py)
- [x] [0036. Valid Sudoku](./01-hash-map-set/0036-valid-sudoku.py)

### 2. Two Pointers (2)
- [x] [0125. Valid Palindrome](./02-two-pointers/0125-valid-palindrome.py)
- [x] [0167. Two Sum II](./02-two-pointers/0167-two-sum-ii.py)

### 3. Sliding Window (2)
- [x] [0121. Best Time to Buy and Sell Stock](./03-sliding-window/0121-best-time-to-buy-and-sell-stock/)
- [x] [0053. Maximum Subarray](./03-sliding-window/0053-maximum-subarray/)

### 4. Stack (2)
- [x] [0020. Valid Parentheses](./04-stack/0020-valid-parentheses.py)
- [x] [0155. Min Stack](./04-stack/0155-min-stack_REDO/)

### 5. Queue (2)
- [x] [0232. Implement Queue using Stacks](./05-queue/0232-implement-queue-using-stacks.py)
- [x] [0933. Number of Recent Calls](./05-queue/0933-number-of-recent-calls_REDO/)

### 6. Binary Search (2)
- [ ] [0704. Binary Search](./06-binary-search/0704-binary-search/)
- [ ] [0278. First Bad Version](./06-binary-search/0278-first-bad-version/)

### 7. Tree (4)
- [x] [0104. Maximum Depth of Binary Tree](./07-tree/0104-maximum-depth-of-binary-tree/)
- [x] [0100. Same Tree](./07-tree/0100-same-tree/)
- [x] [0102. Binary Tree Level Order Traversal](./07-tree/0102-binary-tree-level-order-traversal/)
- [x] [0226. Invert Binary Tree](./07-tree/0226-invert-binary-tree/)

### 8. Linked List (2)
- [x] [0206. Reverse Linked List](./08-linked-list/0206-reverse-linked-list/)
- [x] [0021. Merge Two Sorted Lists](./08-linked-list/0021-merge-two-sorted-lists/)

### 9~11. (예정)
- [ ] DP
- [ ] Heap
- [ ] Design (LRU Cache 등)

## 자료

- [Easy 13문제 패턴 정리](./docs/leetcode_easy_patterns.md)
- [Claude Code 셋업 지시서](./docs/claude_code_setup_instructions.md)

## 사용 방법

각 문제 파일을 직접 실행:

```bash
python 01-hash-map-set/0001-two-sum.py
```

각 파일에는 상단 docstring에 다음이 포함됨:
- 한국어 문제 요약
- 핵심 아이디어
- 자료구조 / 패턴
- 시간/공간 복잡도
- 면접용 영어 멘트
- 엣지 케이스

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
| 9 | Maximum Subarray | Kadane's (DP) | 새로 시작 vs 이어가기 |
| 10 | Valid Parentheses | Stack | 여는 push, 닫는 pop+비교 |
| 11 | Min Stack | Stack (OOP) | 보조 스택으로 최솟값 추적 |
| 12 | Queue using Stacks | Stack/Queue (OOP) | 두 스택으로 FIFO 흉내 |
| 13 | Recent Counter | Queue (deque) | 시간 윈도우 관리 |
