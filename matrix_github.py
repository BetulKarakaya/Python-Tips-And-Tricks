from typing import List, Any

class Matrix:
    def __init__(self, rows: List[List[Any]]):
        self.rows = rows

    def transpose(self) -> "Matrix":
        """Transpose the matrix using the zip(*) trick."""
        transposed = [list(col) for col in zip(*self.rows)]
        return Matrix(transposed)

    def _col_widths(self, rows):
        """Calculate column widths for pretty alignment."""
        cols = list(zip(*rows))
        return [max(len(str(x)) for x in c) for c in cols]

    def _format_rows(self, rows) -> List[str]:
        """Return each row as a formatted aligned string."""
        col_widths = self._col_widths(rows)
        formatted = []
        for r in rows:
            parts = [str(v).rjust(w) for v, w in zip(r, col_widths)]
            formatted.append("  ".join(parts))
        return formatted

    def display_with_transpose(self):
        t = self.transpose()

        left = self._format_rows(self.rows)
        right = self._format_rows(t.rows)

        print("🟦 ORIGINAL MATRIX        |       🟩 TRANSPOSED MATRIX\n")
        for l, r in zip(left, right):
            print(f"{l}    |    {r}")

    def __repr__(self):
        return f"<Matrix {len(self.rows)}x{len(self.rows[0]) if self.rows else 0}>"

def main():
    mat = Matrix([
        [1,  2,  3],
        [10, 20, 30],
        [100, 200, 300],
    ])

    mat.display_with_transpose()

if __name__ == "__main__":
    main()
