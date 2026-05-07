# LeetCode 면접 준비 Repo 셋업 — Claude Code 작업 지시서

## 컨텍스트

Google FDE (Forward Deployed Engineer) 코딩 인터뷰 준비를 위한 LeetCode 풀이 정리 repo를 만들고 싶음. 면접까지 약 2주 남음. 매일 푸는 문제를 패턴별로 정리하면서 면접 직전 빠르게 복습할 수 있는 구조로 만들 것.

---

## 작업 목표

1. 패턴별 폴더 구조 생성
2. 각 문제마다 **풀이 코드 + 핵심 메모**가 한 파일에 들어가는 템플릿 생성
3. README로 전체 진척도와 패턴별 인덱스 관리
4. 기존에 정리한 마크다운 문서들을 `docs/` 폴더로 통합

---

## 작업 환경

- 언어: Python 3
- 작업 디렉토리: `leetcode-prep/`
- Git 사용 (단, push는 사용자가 직접 진행)

---

## 폴더 구조

다음 구조로 폴더와 빈 파일을 생성해주세요:

```
leetcode-prep/
├── README.md
├── docs/
│   ├── python_data_structures_cheatsheet.md   (기존 파일 이동)
│   ├── leetcode_easy_patterns.md              (기존 파일 이동)
│   ├── google_fde_recruiter_call_prep_v2.md   (기존 파일 이동)
│   └── google_fde_rrk_prep.md                 (기존 파일 이동)
├── 01-hash-map-set/
│   ├── 0001-two-sum.py
│   ├── 0217-contains-duplicate.py
│   ├── 0242-valid-anagram.py
│   ├── 0349-intersection-of-two-arrays.py
│   └── 0036-valid-sudoku.py
├── 02-two-pointers/
│   ├── 0125-valid-palindrome.py
│   └── 0167-two-sum-ii.py
├── 03-sliding-window/
│   ├── 0121-best-time-to-buy-and-sell-stock.py
│   └── 0053-maximum-subarray.py
├── 04-stack/
│   ├── 0020-valid-parentheses.py
│   └── 0155-min-stack.py
├── 05-queue/
│   ├── 0232-implement-queue-using-stacks.py
│   └── 0933-number-of-recent-calls.py
├── 06-binary-search/
├── 07-tree/
├── 08-linked-list/
├── 09-dp/
├── 10-heap/
└── 11-design/
```

빈 폴더(06~11)는 다음 주에 채울 패턴들이라 일단 폴더만 만들어두면 됩니다. `.gitkeep` 파일을 넣어서 git에 추적되게 해주세요.

---

## 풀이 파일 템플릿

각 `.py` 파일은 다음 형식으로 작성해주세요. 코드만이 아니라 **상단 docstring에 메모**를 포함하는 게 핵심입니다. 면접 직전 빠르게 훑을 수 있도록.

### 템플릿

```python
"""
[문제 번호] [문제 제목] (Difficulty)
링크: https://leetcode.com/problems/two-sum/

문제:
    한국어로 짧게 요약 (1~2줄)

핵심 아이디어:
    무엇을 활용해서 어떻게 푸는지 (1~3줄)

자료구조 / 패턴:
    - dict (Hash Map)
    - 또는 set, two pointers 등

시간복잡도: O(n)
공간복잡도: O(n)

영어 멘트 (면접용):
    "I'll use a hash map to store values along with their indices.
     For each number, I check if its complement is already in the map."

엣지 케이스:
    - 빈 입력
    - 음수
    - 중복 값
    - 답이 없는 경우
"""


def twoSum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


# 테스트
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(twoSum([3, 2, 4], 6))        # [1, 2]
    print(twoSum([3, 3], 6))           # [0, 1]
```

### 13문제 모두 이 템플릿으로 채워주세요

기존에 사용자가 업로드할 `leetcode_easy_patterns.md`에 13문제의 풀이가 다 있으니, 그걸 참고해서 13개 파일을 다 채워주세요. 각 파일마다:

1. 상단 docstring (위 형식)
2. 함수 또는 클래스 풀이
3. `if __name__ == "__main__":` 블록에 테스트 케이스 2~3개

---

## README.md 작성

루트 `README.md`는 다음 구조로 작성해주세요:

```markdown
# LeetCode Interview Prep

Google FDE 면접 준비를 위한 LeetCode 풀이 정리.

## 진척도

- [x] Week 1: Easy 패턴별 마스터 (13/13)
- [ ] Week 2: Medium 응용 + OOP Design + Mock Interview

## 패턴별 인덱스

### 1. Hash Map / Set (5)
- [x] [0001. Two Sum](./01-hash-map-set/0001-two-sum.py)
- [x] [0217. Contains Duplicate](./01-hash-map-set/0217-contains-duplicate.py)
- [x] [0242. Valid Anagram](./01-hash-map-set/0242-valid-anagram.py)
- [x] [0349. Intersection of Two Arrays](./01-hash-map-set/0349-intersection-of-two-arrays.py)
- [x] [0036. Valid Sudoku](./01-hash-map-set/0036-valid-sudoku.py)

### 2. Two Pointers (2)
- [x] [0125. Valid Palindrome](./02-two-pointers/0125-valid-palindrome.py)
- [x] [0167. Two Sum II](./02-two-pointers/0167-two-sum-ii.py)

### 3. Sliding Window (2)
- [x] [0121. Best Time to Buy and Sell Stock](./03-sliding-window/0121-best-time-to-buy-and-sell-stock.py)
- [x] [0053. Maximum Subarray](./03-sliding-window/0053-maximum-subarray.py)

### 4. Stack (2)
- [x] [0020. Valid Parentheses](./04-stack/0020-valid-parentheses.py)
- [x] [0155. Min Stack](./04-stack/0155-min-stack.py)

### 5. Queue (2)
- [x] [0232. Implement Queue using Stacks](./05-queue/0232-implement-queue-using-stacks.py)
- [x] [0933. Number of Recent Calls](./05-queue/0933-number-of-recent-calls.py)

### 6~11. (Week 2)
- [ ] Binary Search
- [ ] Tree
- [ ] Linked List
- [ ] DP
- [ ] Heap
- [ ] Design (LRU Cache 등)

## 자료

- [Python 자료구조 치트시트](./docs/python_data_structures_cheatsheet.md)
- [Easy 13문제 패턴 정리](./docs/leetcode_easy_patterns.md)
- [Google FDE RRK 면접 대비](./docs/google_fde_rrk_prep.md)
- [Google FDE 리쿠르터 콜 정리](./docs/google_fde_recruiter_call_prep_v2.md)

## 사용 방법

각 문제 파일을 직접 실행:

```bash
python 01-hash-map-set/0001-two-sum.py
```
```

---

## 추가 작업

### 1. `.gitignore` 생성

```
__pycache__/
*.pyc
.DS_Store
.vscode/
.idea/
*.egg-info/
.pytest_cache/
```

### 2. 모든 풀이 파일 검증

`if __name__ == "__main__":` 블록을 포함했으니, **모든 13개 파일을 직접 실행**해서 출력이 예상과 맞는지 확인해주세요. 각 파일 실행 결과를 마지막에 보고해주세요.

### 3. Git 초기화

```bash
git init
git add .
git commit -m "Initial commit: Week 1 Easy patterns (13 problems)"
```

push는 사용자가 직접 GitHub에서 repo 만든 다음 진행할 거니까 거기까지만 해주세요.

---

## 우선순위

이 순서로 진행해주세요:

1. 폴더 구조 + 빈 파일 생성
2. 13문제 풀이 파일 작성 (사용자가 업로드한 `leetcode_easy_patterns.md` 참고)
3. 13문제 모두 실행 검증
4. README.md 작성
5. `.gitignore` 작성
6. 기존 마크다운 문서들을 `docs/` 폴더로 이동
7. Git 초기화 + 첫 커밋

---

## 참고: 사용자 컨텍스트

- 사용자는 박사 학위 보유 (시계열 + LLM)
- 삼성 코테 프로 자격 보유 → 알고리즘 사고력은 충분
- 최근 1년간 손 코딩 양이 줄어 패턴 회상이 다소 느린 상태
- 이번 주: Easy 패턴 13개 손에 박기 (이 repo의 목표)
- 다음 주: Medium 응용 + OOP Design 추가 예정
- 스타일: 명확한 코드 + 영어 멘트 준비 + 엣지 케이스 고려

따라서 풀이 파일은 **단순 정답 코드가 아니라 면접 직전에 빠르게 훑을 수 있는 메모 + 코드** 형태로 작성하는 게 핵심입니다.

---

## 마무리 후 보고

작업 완료되면 다음을 알려주세요:

1. 생성된 폴더와 파일 목록 (tree 명령 결과)
2. 13문제 실행 결과 요약 (정답 맞는지)
3. 누락되거나 애매했던 부분이 있다면 그것도

화이팅.
