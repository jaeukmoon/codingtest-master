# LeetCode Interview Prep

Google FDE 면접 준비를 위한 LeetCode 풀이 정리.

## 진척도

- [x] Week 1: Easy 패턴별 마스터 (13/13)
- [x] Week 2: Top 10 Medium (10/10)
- [ ] Week 3: Rest Medium (3/24) + OOP Design 심화 + Mock Interview

> **마커 범례**
> - `[x]` = 커리큘럼 진행 완료 (solution.py 존재, 기본 풀이 끝남)
> - `**(직접)**` = problem.py에 직접 풀이 작성 (`python scan_attempts.py`로 자동 감지)
> - 폴더명에 `_REDO` / `-REDO` / `_REVIEW` = 재연습 대상 (아래 [REDO 목록](#redo-목록-재연습-대상-10개) 참고)

## 패턴별 인덱스

### 1. Hash Map / Set (5)
- [x] [0001. Two Sum](./01-hash-map-set/0001-two-sum/)
- [x] [0217. Contains Duplicate](./01-hash-map-set/0217-contains-duplicate/) **(직접)**
- [x] [0242. Valid Anagram](./01-hash-map-set/0242-valid-anagram_REVIEW/) **(직접)**
- [x] [0349. Intersection of Two Arrays](./01-hash-map-set/0349-intersection-of-two-arrays/) **(직접)**
- [x] [0036. Valid Sudoku](./01-hash-map-set/0036-valid-sudoku/) **(직접)**

### 2. Two Pointers (2)
- [x] [0125. Valid Palindrome](./02-two-pointers/0125-valid-palindrome/) **(직접)**
- [x] [0167. Two Sum II](./02-two-pointers/0167-two-sum-ii/) **(직접)**

### 3. Sliding Window (2)
- [x] [0121. Best Time to Buy and Sell Stock](./03-sliding-window/0121-best-time-to-buy-and-sell-stock_REDO/) **(직접)**
- [x] [0053. Maximum Subarray](./03-sliding-window/0053-maximum-subarray/)

### 4. Stack (2)
- [x] [0020. Valid Parentheses](./04-stack/0020-valid-parentheses/) **(직접)**
- [x] [0155. Min Stack](./04-stack/0155-min-stack_REDO/) **(직접)**

### 5. Queue (2)
- [x] [0232. Implement Queue using Stacks](./05-queue/0232-implement-queue-using-stacks/) **(직접)**
- [x] [0933. Number of Recent Calls](./05-queue/0933-number-of-recent-calls_REDO/) **(직접)**

### 6. Binary Search (2)
- [x] [0704. Binary Search](./06-binary-search/0704-binary-search/) **(직접)**
- [x] [0278. First Bad Version](./06-binary-search/0278-first-bad-version/) **(직접)**

### 7. Tree (4)
- [x] [0104. Maximum Depth of Binary Tree](./07-tree/0104-maximum-depth-of-binary-tree/)
- [x] [0100. Same Tree](./07-tree/0100-same-tree/)
- [x] [0102. Binary Tree Level Order Traversal](./07-tree/0102-binary-tree-level-order-traversal/)
- [x] [0226. Invert Binary Tree](./07-tree/0226-invert-binary-tree/) **(직접)**

### 8. Linked List (3)
- [x] [0206. Reverse Linked List](./08-linked-list/0206-reverse-linked-list-REDO/) **(직접)**
- [x] [0021. Merge Two Sorted Lists](./08-linked-list/0021-merge-two-sorted-lists/) **(직접)**
- [x] [0141. Linked List Cycle](./08-linked-list/0141-linked-list-cycle/) **(직접)**

### 9. DP (3)
- [x] [0070. Climbing Stairs](./09-dp/0070-climbing-stairs/)
- [x] [0198. House Robber](./09-dp/0198-house-robber/) — solution.py 포함 (rest-medium에도 있음)
- [x] [0322. Coin Change](./09-dp/0322-coin-change-REDO/) — solution.py 포함 (top-10에도 있음)

### 10. Heap (2)
- [x] [0703. Kth Largest Element in a Stream](./10-heap/0703-kth-largest-element-in-a-stream/) **(직접)**
- [x] [1046. Last Stone Weight](./10-heap/1046-last-stone-weight/) **(직접)**

### 11. Design (2)
- [x] [0146. LRU Cache](./11-design/0146-lru-cache/) **(직접)** — solution.py 포함 (top-10에도 있음)
- [x] [0981. Time Based Key-Value Store](./11-design/0981-time-based-key-value-store/) — solution.py 포함 (rest-medium에도 있음)

### 12. 2D Grid (4)
- [x] [0733. Flood Fill](./12-2d-grid/0733-flood-fill/)
- [x] [0200. Number of Islands](./12-2d-grid/0200-number-of-islands/) — solution.py 포함 (top-10에도 있음)
- [x] [0695. Max Area of Island](./12-2d-grid/0695-max-area-of-island-REDO/) **(직접)**
- [x] [0994. Rotting Oranges](./12-2d-grid/0994-rotting-oranges/) **(직접)** — solution.py 포함 (rest-medium에도 있음)

### 13. Backtracking (2)
- [x] [0078. Subsets](./13-backtracking/0078-subsets/)
- [x] [0046. Permutations](./13-backtracking/0046-permutations/)

---

## REDO 목록 (재연습 대상, 10개)

> 이미 한 번 푼 문제 중 **다시 풀어볼** 항목. 폴더명에 `_REDO`/`-REDO` 또는 `_REVIEW` 접미사로 표시.
> 체크박스는 "재연습 완료" 기준 (재풀이 후 `[x]`).

### Easy / Pattern (§1-§12, 7개)
- [ ] [0242. Valid Anagram](./01-hash-map-set/0242-valid-anagram_REVIEW/) — REVIEW
- [ ] [0121. Best Time to Buy and Sell Stock](./03-sliding-window/0121-best-time-to-buy-and-sell-stock_REDO/)
- [ ] [0155. Min Stack](./04-stack/0155-min-stack_REDO/)
- [ ] [0933. Number of Recent Calls](./05-queue/0933-number-of-recent-calls_REDO/)
- [ ] [0206. Reverse Linked List](./08-linked-list/0206-reverse-linked-list-REDO/)
- [ ] [0322. Coin Change](./09-dp/0322-coin-change-REDO/)
- [ ] [0695. Max Area of Island](./12-2d-grid/0695-max-area-of-island-REDO/)

### Top 10 Medium (3개)
- [ ] [0003. Longest Substring Without Repeating Characters](./top-10-medium/0003-longest-substring-without-repeating-characters_REDO/)
- [ ] [0015. 3Sum](./top-10-medium/0015-3sum_REDO/)
- [ ] [0049. Group Anagrams](./top-10-medium/0049-group-anagrams_REDO/)

---

## Medium 문제 (주제 라벨 없음 — 풀이 시 패턴 직접 식별)

### Top 10 Medium (필수)
- [x] [0146. LRU Cache](./top-10-medium/0146-lru-cache/) **(직접)**
- [x] [0200. Number of Islands](./top-10-medium/0200-number-of-islands/)
- [x] [0049. Group Anagrams](./top-10-medium/0049-group-anagrams_REDO/) **(직접)**
- [x] [0003. Longest Substring Without Repeating Characters](./top-10-medium/0003-longest-substring-without-repeating-characters_REDO/) **(직접)**
- [x] [0015. 3Sum](./top-10-medium/0015-3sum_REDO/) **(직접)**
- [x] [0098. Validate Binary Search Tree](./top-10-medium/0098-validate-binary-search-tree/)
- [x] [0347. Top K Frequent Elements](./top-10-medium/0347-top-k-frequent-elements/)
- [x] [0739. Daily Temperatures](./top-10-medium/0739-daily-temperatures/)
- [x] [0033. Search in Rotated Sorted Array](./top-10-medium/0033-search-in-rotated-sorted-array/)
- [x] [0322. Coin Change](./top-10-medium/0322-coin-change/)

### Rest Medium (24문제, Top 10 마친 후)
- [ ] [0002. Add Two Numbers](./rest-medium/0002-add-two-numbers/) **(직접)**
- [ ] [0011. Container With Most Water](./rest-medium/0011-container-with-most-water/)
- [ ] [0019. Remove Nth Node From End of List](./rest-medium/0019-remove-nth-node-from-end-of-list/) **(직접)**
- [ ] [0022. Generate Parentheses](./rest-medium/0022-generate-parentheses/)
- [ ] [0034. Find First and Last Position](./rest-medium/0034-find-first-and-last-position/)
- [ ] [0074. Search a 2D Matrix](./rest-medium/0074-search-a-2d-matrix/)
- [ ] [0075. Sort Colors](./rest-medium/0075-sort-colors/)
- [ ] [0128. Longest Consecutive Sequence](./rest-medium/0128-longest-consecutive-sequence/)
- [ ] [0143. Reorder List](./rest-medium/0143-reorder-list/) **(직접)**
- [ ] [0150. Evaluate Reverse Polish Notation](./rest-medium/0150-evaluate-reverse-polish-notation/)
- [ ] [0198. House Robber](./rest-medium/0198-house-robber/)
- [ ] [0199. Binary Tree Right Side View](./rest-medium/0199-binary-tree-right-side-view/)
- [ ] [0207. Course Schedule](./rest-medium/0207-course-schedule/)
- [ ] [0230. Kth Smallest Element in a BST](./rest-medium/0230-kth-smallest-element-in-bst/)
- [ ] [0236. Lowest Common Ancestor of a Binary Tree](./rest-medium/0236-lowest-common-ancestor-of-a-binary-tree/)
- [ ] [0300. Longest Increasing Subsequence](./rest-medium/0300-longest-increasing-subsequence/)
- [ ] [0380. Insert/Delete/GetRandom O(1)](./rest-medium/0380-insert-delete-getrandom-o1/)
- [ ] [0424. Longest Repeating Character Replacement](./rest-medium/0424-longest-repeating-character-replacement/)
- [ ] [0438. Find All Anagrams in a String](./rest-medium/0438-find-all-anagrams-in-a-string/)
- [ ] [0535. Encode and Decode TinyURL](./rest-medium/0535-encode-and-decode-tinyurl/)
- [ ] [0560. Subarray Sum Equals K](./rest-medium/0560-subarray-sum-equals-k/)
- [ ] [0567. Permutation in String](./rest-medium/0567-permutation-in-string/)
- [ ] [0981. Time Based Key-Value Store](./rest-medium/0981-time-based-key-value-store/)
- [ ] [0994. Rotting Oranges](./rest-medium/0994-rotting-oranges/)

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
