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

### 8. Linked List (3)
- [x] [0206. Reverse Linked List](./08-linked-list/0206-reverse-linked-list/)
- [x] [0021. Merge Two Sorted Lists](./08-linked-list/0021-merge-two-sorted-lists/)
- [x] [0141. Linked List Cycle](./08-linked-list/0141-linked-list-cycle/)

### 9. DP (1)
- [x] [0070. Climbing Stairs](./09-dp/0070-climbing-stairs/)

### 10. Heap (1)
- [x] [0703. Kth Largest Element in a Stream](./10-heap/0703-kth-largest-element-in-a-stream/)

### 11. Design — see Top 10 / Rest Medium folders (146, 380, 981)

### 12. 2D Grid (4)
- [x] [0733. Flood Fill](./12-2d-grid/0733-flood-fill/)
- [x] [0200. Number of Islands](./12-2d-grid/0200-number-of-islands/) — solution.py 포함 (top-10에도 있음)
- [x] [0695. Max Area of Island](./12-2d-grid/0695-max-area-of-island/)
- [x] [0994. Rotting Oranges](./12-2d-grid/0994-rotting-oranges/) — solution.py 포함 (rest-medium에도 있음)

### 13. Backtracking (2)
- [x] [0078. Subsets](./13-backtracking/0078-subsets/)
- [x] [0046. Permutations](./13-backtracking/0046-permutations/)

---

## Medium 문제 (주제 라벨 없음 — 풀이 시 패턴 직접 식별)

### Top 10 Medium (필수)
- [ ] [0146. LRU Cache](./top-10-medium/0146-lru-cache/)
- [ ] [0200. Number of Islands](./top-10-medium/0200-number-of-islands/)
- [ ] [0049. Group Anagrams](./top-10-medium/0049-group-anagrams/)
- [ ] [0003. Longest Substring Without Repeating Characters](./top-10-medium/0003-longest-substring-without-repeating-characters/)
- [ ] [0015. 3Sum](./top-10-medium/0015-3sum/)
- [ ] [0098. Validate Binary Search Tree](./top-10-medium/0098-validate-binary-search-tree/)
- [ ] [0347. Top K Frequent Elements](./top-10-medium/0347-top-k-frequent-elements/)
- [ ] [0739. Daily Temperatures](./top-10-medium/0739-daily-temperatures/)
- [ ] [0033. Search in Rotated Sorted Array](./top-10-medium/0033-search-in-rotated-sorted-array/)
- [ ] [0322. Coin Change](./top-10-medium/0322-coin-change/)

### Rest Medium (24문제, Top 10 마친 후)
[`./rest-medium/`](./rest-medium/) — 0002, 0011, 0019, 0022, 0034, 0074, 0075, 0128, 0143, 0150, 0198, 0199, 0207, 0230, 0236, 0300, 0380, 0424, 0438, 0535, 0560, 0567, 0981, 0994

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
