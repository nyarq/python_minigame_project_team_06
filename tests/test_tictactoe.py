
from games import tictactoe


# 가로 승리 테스트
def test_row_win():
    board = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "]
    ]
    assert tictactoe.check_winner(board) == "X"


# 세로 승리 테스트
def test_column_win():
    board = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["O", " ", "X"]
    ]
    assert tictactoe.check_winner(board) == "O"


# 대각선 승리 테스트
def test_diagonal_win():
    board = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", " ", "X"]
    ]
    assert tictactoe.check_winner(board) == "X"


# 반대 방향 대각선 승리 테스트
def test_reverse_diagonal_win():
    board = [
        [" ", "O", "X"],
        ["O", "X", " "],
        ["X", " ", "O"]
    ]
    assert tictactoe.check_winner(board) == "X"


# 승리자가 없는 경우
def test_no_winner():
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert tictactoe.check_winner(board) is None


# 게임판이 가득 찬 경우
def test_board_full():
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert tictactoe.is_full(board) is True


# 게임판에 빈칸이 있는 경우
def test_board_not_full():
    board = [
        ["X", "O", "X"],
        ["O", " ", "O"],
        ["X", "O", "X"]
    ]
    assert tictactoe.is_full(board) is False
