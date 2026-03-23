from difflib import unified_diff


class DiffService:
    def build_diff(self, before_text: str | None, after_text: str, file_path: str) -> str:
        before_lines = (before_text or "").splitlines(keepends=True)
        after_lines = after_text.splitlines(keepends=True)
        return "".join(
            unified_diff(before_lines, after_lines, fromfile=f"a/{file_path}", tofile=f"b/{file_path}")
        )
