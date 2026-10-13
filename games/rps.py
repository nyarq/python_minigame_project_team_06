"""가위바위보 — 담당: 팀원 D.

[규칙]
- 컴퓨터와 3판 2선승제로 대결한다.
- 입력: 1(가위) 2(바위) 3(보)
"""

import random

GAME_NAME = "가위바위보"
CHOICES = {"1": "가위", "2": "바위", "3": "보"}
ART = {
    "가위": """
  ✌
 가위
""",
    "바위": """
  ✊
 바위
""",
    "보": """
  ✋
  보
""",
}


def decide(player: str, computer: str) -> str:
    """플레이어의 결과를 ``win``, ``lose``, ``draw`` 중 하나로 반환한다."""
    if player not in CHOICES.values() or computer not in CHOICES.values():
        raise ValueError("선택은 가위, 바위, 보 중 하나여야 합니다.")

    if player == computer:
        return "draw"

    wins_against = {"가위": "보", "바위": "가위", "보": "바위"}
    return "win" if wins_against[player] == computer else "lose"


def play() -> None:
    """한 판(3판 2선승)을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    player_wins = 0
    computer_wins = 0

    print(f"\n[{GAME_NAME}] 3판 2선승입니다.")
    while player_wins < 2 and computer_wins < 2:
        choice = input("1. ✌ 가위  2. ✊ 바위  3. ✋ 보: ").strip()
        player = CHOICES.get(choice)
        if player is None:
            print("1, 2, 3 중에서 선택하세요.")
            continue

        computer = random.choice(list(CHOICES.values()))
        result = decide(player, computer)
        print("\n나의 선택:", ART[player], sep="")
        print("컴퓨터의 선택:", ART[computer], sep="")

        if result == "draw":
            print("무승부입니다. 다시 진행합니다.")
        elif result == "win":
            player_wins += 1
            print("이번 판 승리!")
        else:
            computer_wins += 1
            print("이번 판 패배!")

        print(f"현재 점수 - 나 {player_wins} : {computer_wins} 컴퓨터")

    if player_wins == 2:
        print("최종 승리입니다!")
    else:
        print("최종 패배입니다.")
