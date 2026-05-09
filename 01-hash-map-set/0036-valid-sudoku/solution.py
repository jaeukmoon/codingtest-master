"""
[0036] Valid Sudoku (Medium-ish Easy)
링크: https://leetcode.com/problems/valid-sudoku/

## 문제

9x9 스도쿠 보드가 유효한지 확인하라. 유효한 조건:
  1. 각 행에 1~9가 중복 없이 있어야 한다.
  2. 각 열에 1~9가 중복 없이 있어야 한다.
  3. 9개의 3x3 박스 각각에 1~9가 중복 없이 있어야 한다.
빈 칸은 '.'으로 표시. 보드가 완성될 필요는 없다.

## 예시

Example 1:
    유효한 보드 → true
Example 2:
    같은 행/열/박스에 중복 숫자 존재 → false

## 조건

- board.length == 9, board[i].length == 9
- board[i][j]는 숫자('1'~'9') 또는 '.'이다.

---

핵심 아이디어:
    행/열/박스를 각각 set으로 관리. 한 번 순회하면서 세 set에 동시에 체크.
    박스 번호: box_idx = (r // 3) * 3 + (c // 3)

자료구조 / 패턴:
    - set 여러 개 병렬 관리

시간복잡도: O(81) = O(1) — 보드 크기 고정
공간복잡도: O(81) = O(1)

영어 멘트 (면접용):
    "I'll maintain three arrays of sets — one for rows, one for columns, one for 3x3 boxes.
     For each cell, I check all three constraints simultaneously and add the value if valid.
     The box index is computed as (r // 3) * 3 + (c // 3)."

엣지 케이스:
    - 빈 칸('.')은 스킵
    - 같은 숫자가 같은 행/열/박스에 두 번 나오면 False
    - 보드가 완성되지 않아도 유효할 수 있음 (현재 배치만 체크)
"""


## 손 추적 (Hand Trace)
# 핵심: box_idx 계산만 직접 추적
# box_idx = (r//3)*3 + (c//3)
#
#  r,c  | r//3 | c//3 | box_idx
# ------|------|------|--------
#  0,0  |  0   |  0   |   0
#  0,8  |  0   |  2   |   2
#  4,4  |  1   |  1   |   4     ← 중앙 박스
#  8,8  |  2   |  2   |   8
#  4,7  |  1   |  2   |   5
#
# 중복 감지 예시: r=3, c=0, val="8"
#   rows[3]에 "8" 없음 → add
#   cols[0]에 "8" 있음(r=0에서 추가됨) → return False


def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            box_idx = (r // 3) * 3 + (c // 3)

            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False

            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)

    return True


if __name__ == "__main__":
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    print(isValidSudoku(valid_board))   # True

    invalid_board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],  # 8 중복 (열 0)
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    print(isValidSudoku(invalid_board))  # False
