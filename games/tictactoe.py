
"""틱택토 — 담당: 팀원 E

[규칙]
- 2명이 번갈아 X, O를 3x3 판에 놓는다.
- 가로·세로·대각선으로 세 칸을 먼저 채우면 승리한다.
- 판이 가득 차면 무승부이다.
"""

GAME_NAME = "틱택토"


# 승리 여부 확인
def check_winner(board: list[list[str]]) -> str | None:
    # 가로와 세로 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


# 게임판이 가득 찼는지 확인
def is_full(board: list[list[str]]) -> bool:
    return all(cell != " " for row in board for cell in row)


# 게임판 출력
def print_board(board: list[list[str]]) -> None:
    print("\n    1   2   3")
    for i in range(3):
        print(f"{i + 1}   " + " | ".join(board[i]))
        if i < 2:
            print("   ---+---+---")
    print()


# 틱택토 게임 실행
def play() -> None:
    """한 판을 진행한다. 끝나면 메인 메뉴로 돌아간다."""

    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print(f"\n[{GAME_NAME}] 게임을 시작합니다!")
    print("2명이 번갈아 X와 O를 놓습니다.")
    print("행과 열에 각각 1~3을 입력하세요.")
    print("0을 입력하면 메인 메뉴로 돌아갑니다.")

    while True:
        print_board(board)
        print(f"[{player} 차례]")

        try:
            row = int(input("행 입력 (1~3): "))
            if row == 0:
                return

            col = int(input("열 입력 (1~3): "))
            if col == 0:
                return

        except ValueError:
            print("숫자만 입력해주세요.")
            continue

        # 입력 범위 확인
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("1부터 3까지의 숫자를 입력해주세요.")
            continue

        row -= 1
        col -= 1

        # 이미 선택된 칸인지 확인
        if board[row][col] != " ":
            print("이미 선택된 칸입니다. 다시 입력해주세요.")
            continue

        # 게임판에 X 또는 O 표시
        board[row][col] = player

        # 승리 판정
        winner = check_winner(board)

        if winner is not None:
            print_board(board)
            print(f"축하합니다! {winner} 플레이어 승리!")
            return

        # 무승부 판정
        if is_full(board):
            print_board(board)
            print("무승부입니다!")
            return

        # 플레이어 교체
        player = "O" if player == "X" else "X"
