"""problem.py 자동 스캔 — 함수 본문이 'pass'/docstring만이 아니면 '직접 푼' 것으로 간주.

헬퍼 클래스(TreeNode, ListNode, Node)는 스캐폴딩이라 제외.
"""
import ast
import pathlib

HELPER_CLASSES = {"TreeNode", "ListNode", "Node"}


def func_is_real(func: ast.FunctionDef) -> bool:
    body = func.body
    if (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        body = body[1:]
    if not body:
        return False
    if len(body) == 1 and isinstance(body[0], ast.Pass):
        return False
    return True


def is_attempted(path: pathlib.Path) -> bool:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    saw_func = False
    # 최상위 함수 + 헬퍼 클래스가 아닌 클래스의 메서드만 본다
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            saw_func = True
            if func_is_real(node):
                return True
        elif isinstance(node, ast.ClassDef) and node.name not in HELPER_CLASSES:
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    saw_func = True
                    if func_is_real(sub):
                        return True
    return False


def main():
    for p in sorted(pathlib.Path(".").glob("**/problem.py")):
        sp = str(p).replace("\\", "/")
        flag = "YES" if is_attempted(p) else "NO "
        print(f"{flag}  {sp}")


if __name__ == "__main__":
    main()
