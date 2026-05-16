"""
[0347] Top K Frequent Elements — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **k는 항상 유효한가?** (1 <= k <= 고유 원소 개수) → 네.
- **빈도가 같으면 tie-break?** → 답이 유일하다고 가정 → 신경 안 써도 됨.
- **출력 순서?** → 무관.
- **n과 k의 관계?** → k가 매우 작은 경우(예: 1~10)이면 heap이 강점.

## 2. 엣지 케이스

- nums=[1], k=1 → [1]
- 모두 유일한 원소 [1,2,3,4], k=2 → 빈도 다 1, 답은 임의의 두 개
- 음수 포함
- 큰 n (10^5) — O(n log n) sort는 가능하지만, follow-up은 더 좋은 걸 요구

## 3. 알고리즘 선택

### 옵션 비교
| 방법 | 시간 | 공간 | 비고 |
|---|---|---|---|
| Counter + sort | O(n log n) | O(n) | 가장 단순 |
| **Min-heap 크기 k** | **O(n log k)** | **O(n+k)** | follow-up 답 |
| **Bucket sort** | **O(n)** | **O(n)** | 최적, 면접 어필 |
| Quickselect | O(n) avg | O(n) | 구현 복잡 |

### Bucket Sort ← 채택 (면접에서 가장 좋은 답)
핵심 통찰: **빈도는 최대 n까지**. 인덱스를 빈도로 쓰는 길이 n+1 배열을 만들 수 있다.
- buckets[freq] = [그 빈도를 가진 숫자들]
- 뒤(높은 freq)부터 훑어서 k개 모으면 끝.

이 발상은 counting sort와 같음. "값의 범위가 제한적이라 인덱스로 쓸 수 있다"는 패턴은
면접에서 자주 강점으로 작용함.

### Heap도 알면 좋음 — 언급용
heapq에 음수 freq로 push해서 nlargest(k, counter.items())로도 한 줄. 실용적.

## 4. 복잡도

- 시간: O(n) — Counter O(n) + bucket 채우기 O(n) + 뒤에서 k 모으기 O(n)
- 공간: O(n)
"""
from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # 예시: nums = [1,1,1,2,2,3], k = 2
    freq = Counter(nums)
    # freq = {1:3, 2:2, 3:1}
    n = len(nums)   # 6

    buckets: List[List[int]] = [[] for _ in range(n + 1)]
    for num, f in freq.items():
        buckets[f].append(num)
    # buckets = [[], [3], [2], [1], [], [], []]
    #            f=0  f=1  f=2  f=3  f=4  f=5 f=6
    # → 빈도 1인 숫자: [3], 빈도 2인 숫자: [2], 빈도 3인 숫자: [1]

    result: List[int] = []
    for f in range(n, 0, -1):
        for num in buckets[f]:
            result.append(num)
            if len(result) == k:
                return result
    # f=6: buckets[6]=[] → skip
    # f=5: buckets[5]=[] → skip
    # f=4: buckets[4]=[] → skip
    # f=3: buckets[3]=[1] → result=[1], len=1 < 2 → 계속
    # f=2: buckets[2]=[2] → result=[1,2], len=2 == k → return [1,2]

    return result


if __name__ == "__main__":
    print(sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2)))   # [1, 2]
    print(topKFrequent([1], 1))                            # [1]
    print(sorted(topKFrequent([1, 2, 3, 4], 2)))          # 임의 두 개
    print(sorted(topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)))   # [-1, 2]
