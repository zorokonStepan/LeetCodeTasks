"""
    Determine if a 9 x 9 Sudoku board is valid.
    Only the filled cells need to be validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain
        the digits 1-9 without repetition.

    Note:
        1. A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        2. Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if not self._validate_rows(board):
            return False
        if not self._validate_columns(board):
            return False
        if not self._validate_sub_boxes(board):
            return False
        return True

    def _validate_rows(self, board: list[list[str]]) -> bool:
        for row in board:
            items = [item for item in row if item.isdigit()]
            if len(items) != len(set(items)):
                return False
        return True

    def _validate_columns(self, board: list[list[str]]) -> bool:
        for ind in range(len(board)):
            items = [row[ind] for row in board if row[ind].isdigit()]
            if len(items) != len(set(items)):
                return False
        return True

    def _validate_sub_boxes(self, board: list[list[str]]) -> bool:
        for ind_row in (0, 3, 6):
            for column_row in (0, 3, 6):
                sub_boxe = self._exclude_sub_boxe(board, ind_row, column_row)
                items = [item for item in sub_boxe if item.isdigit()]
                if len(items) != len(set(items)):
                    return False
        return True

    def _exclude_sub_boxe(self, board: list[list[str]], ind_row: int, column_row: int) -> list[str]:
        return [
            board[ind_row][column_row],
            board[ind_row][column_row + 1],
            board[ind_row][column_row + 2],
            board[ind_row + 1][column_row],
            board[ind_row + 1][column_row + 1],
            board[ind_row + 1][column_row + 2],
            board[ind_row + 2][column_row],
            board[ind_row + 2][column_row + 1],
            board[ind_row + 2][column_row + 2],
        ]
