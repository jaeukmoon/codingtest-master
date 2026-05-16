"""
[0739] Daily Temperatures — Solution

================================================================
면접 접근법
================================================================

## 1. 먼저 확인할 것

- **"더 높은 날" — strictly greater?**
  → 네. 같은 기온은 카운트 안 함.
- **"일수"는 다음 날까지의 차이?**
  → 인덱스 차이 (j - i).
- **그런 날 없으면?**
  → 0.
- **음수 기온/입력 범위?**
  → 30~100. 별 문제 안 됨.

## 2. 엣지 케이스

- 단일 원소 [50] → [0]
- 단조 증가 [30,40,50] → [1,1,0]
- 단조 감소 [50,40,30] → [0,0,0]
- 모두 같은 값 [50,50,50] → [0,0,0]  (strictly greater)
- 매우 긴 입력(10^5) — O(n²) brute force는 위험

## 3. 알고리즘 선택

### Brute force O(n²)
각 i에 대해 i+1부터 더 큰 값 찾기 → 10^5에서 10^10 연산, 시간 초과.

### Monotonic Stack ← 채택 (이 문제의 정석)
**패턴 신호**: "다음 더 큰 원소(next greater element)" → 거의 항상 monotonic stack.

핵심 아이디어:
- 스택에 **아직 답을 못 찾은 날의 인덱스**들을 저장. (값이 아니라 인덱스)
- 스택은 **단조 감소(non-increasing)** 상태 유지 (값 기준).
- 새 날 i를 보면, 스택 top의 기온보다 i의 기온이 더 높으면:
    - top을 pop하고 answer[top] = i - top.
    - 계속 반복하며 i보다 작은 스택 항목 모두 처리.
- 그 후 i를 스택에 push.

### 왜 O(n)인가
각 인덱스는 스택에 한 번 push되고 최대 한 번 pop됨 → amortized O(1) per index → 전체 O(n).

### 왜 단조 "감소"인가
새로 들어오는 i가 스택 top보다 작거나 같으면, i는 top의 답이 될 수 없음(strict).
top의 답을 찾으려면 더 큰 값이 나타나야 함 → top은 그때까지 스택에 남음 → 단조성 유지.

## 4. 복잡도

- 시간: O(n) — 각 원소 push/pop 최대 1번씩
- 공간: O(n) — 최악 스택에 전부 (단조 감소 입력)
"""
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # 예시: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    n = len(temperatures)
    answer = [0] * n
    stack: List[int] = []   # 인덱스 저장, 값 기준 단조 감소

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # i=0, t=73: stack=[] → push → stack=[0]              (73)
    # i=1, t=74: 73<74 → pop 0, answer[0]=1-0=1 → push → stack=[1]   (74)
    # i=2, t=75: 74<75 → pop 1, answer[1]=2-1=1 → push → stack=[2]   (75)
    # i=3, t=71: 75>71 → push → stack=[2,3]               (75,71)
    # i=4, t=69: 71>69 → push → stack=[2,3,4]             (75,71,69)
    # i=5, t=72: 69<72 → pop 4, answer[4]=5-4=1
    #            71<72 → pop 3, answer[3]=5-3=2
    #            75>72 → stop, push → stack=[2,5]          (75,72)
    # i=6, t=76: 72<76 → pop 5, answer[5]=6-5=1
    #            75<76 → pop 2, answer[2]=6-2=4
    #            push → stack=[6]                          (76)
    # i=7, t=73: 76>73 → push → stack=[6,7]               (76,73)
    # 스택에 남은 6,7 → answer[6]=0, answer[7]=0 (이미 0)
    # answer = [1, 1, 4, 2, 1, 1, 0, 0]

    return answer


if __name__ == "__main__":
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # [1,1,4,2,1,1,0,0]
    print(dailyTemperatures([30, 40, 50, 60]))                     # [1,1,1,0]
    print(dailyTemperatures([30, 60, 90]))                          # [1,1,0]
    print(dailyTemperatures([50]))                                   # [0]
    print(dailyTemperatures([50, 50, 50]))                           # [0,0,0] — strict
    print(dailyTemperatures([90, 80, 70, 60]))                       # [0,0,0,0]
