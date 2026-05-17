# LeetCode Interview Prep

Google FDE 면접 준비를 위한 LeetCode 풀이 정리.

## 진척도

- [x] Week 1: Easy 패턴별 마스터 (13/13)
- [x] Week 2: Top 10 Medium (10/10)
- [ ] Week 3: Rest Medium (0/24) + OOP Design 심화 + Mock Interview

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
- [x] [0704. Binary Search](./06-binary-search/0704-binary-search/)
- [x] [0278. First Bad Version](./06-binary-search/0278-first-bad-version/)

### 7. Tree (4)
- [x] [0104. Maximum Depth of Binary Tree](./07-tree/0104-maximum-depth-of-binary-tree/)
- [x] [0100. Same Tree](./07-tree/0100-same-tree/)
- [x] [0102. Binary Tree Level Order Traversal](./07-tree/0102-binary-tree-level-order-traversal/)
- [x] [0226. Invert Binary Tree](./07-tree/0226-invert-binary-tree/)

### 8. Linked List (3)
- [x] [0206. Reverse Linked List](./08-linked-list/0206-reverse-linked-list/)
- [x] [0021. Merge Two Sorted Lists](./08-linked-list/0021-merge-two-sorted-lists/)
- [x] [0141. Linked List Cycle](./08-linked-list/0141-linked-list-cycle/)

### 9. DP (3)
- [x] [0070. Climbing Stairs](./09-dp/0070-climbing-stairs/)
- [x] [0198. House Robber](./09-dp/0198-house-robber/) — solution.py 포함 (rest-medium에도 있음)
- [x] [0322. Coin Change](./09-dp/0322-coin-change/) — solution.py 포함 (top-10에도 있음)

### 10. Heap (2)
- [x] [0703. Kth Largest Element in a Stream](./10-heap/0703-kth-largest-element-in-a-stream/)
- [x] [1046. Last Stone Weight](./10-heap/1046-last-stone-weight/)

### 11. Design (2)
- [x] [0146. LRU Cache](./11-design/0146-lru-cache/) — solution.py 포함 (top-10에도 있음)
- [x] [0981. Time Based Key-Value Store](./11-design/0981-time-based-key-value-store/) — solution.py 포함 (rest-medium에도 있음)

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
- [x] [0146. LRU Cache](./top-10-medium/0146-lru-cache/)
- [x] [0200. Number of Islands](./top-10-medium/0200-number-of-islands/)
- [x] [0049. Group Anagrams](./top-10-medium/0049-group-anagrams_REDO/)
- [x] [0003. Longest Substring Without Repeating Characters](./top-10-medium/0003-longest-substring-without-repeating-characters_REDO/)
- [x] [0015. 3Sum](./top-10-medium/0015-3sum/)
- [x] [0098. Validate Binary Search Tree](./top-10-medium/0098-validate-binary-search-tree/)
- [x] [0347. Top K Frequent Elements](./top-10-medium/0347-top-k-frequent-elements/)
- [x] [0739. Daily Temperatures](./top-10-medium/0739-daily-temperatures/)
- [x] [0033. Search in Rotated Sorted Array](./top-10-medium/0033-search-in-rotated-sorted-array/)
- [x] [0322. Coin Change](./top-10-medium/0322-coin-change/)

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
| 14 | LRU Cache | Hash Map + DLL | dict로 O(1) 조회, DLL로 O(1) 순서 갱신 |
| 15 | Number of Islands | 2D Grid DFS | 1 만나면 DFS로 한 섬 통째 방문 처리 |
| 16 | Group Anagrams | Hash Map | sorted(word) 또는 카운트 튜플을 키로 그룹핑 |
| 17 | Longest Substring | Sliding Window (가변) | 중복 만나면 left를 dict 기반으로 점프 |
| 18 | 3Sum | Sort + Two Pointers | i 고정 + 양 끝 포인터, 세 위치 모두 dedup |
| 19 | Validate BST | Tree DFS + 경계 전달 | 각 노드에 (lo, hi) 범위 전파 |
| 20 | Top K Frequent | Heap / Bucket Sort | 빈도 카운트 후 size-k min-heap or 빈도-인덱스 버킷 |
| 21 | Daily Temperatures | Monotonic Stack | 감소 스택에 인덱스 보관, 크면 pop하며 거리 계산 |
| 22 | Search in Rotated | Binary Search 변형 | mid 기준 어느 쪽이 정렬됐는지 판별 후 분기 |
| 23 | Coin Change | 1D DP | dp[i] = min(dp[i-c]+1) for c in coins |
